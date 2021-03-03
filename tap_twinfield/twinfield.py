"""Twinfield API Client."""
# -*- coding: utf-8 -*-

import logging
import os
from datetime import date, datetime
from typing import Callable, Generator, List

import pandas as pd
import singer
from dateutil.rrule import MONTHLY, rrule
from defusedxml import ElementTree
from lxml import etree  # noqa: S410: lxml is only used for pretty printing
from lxml.html import HtmlElement, fromstring  # noqa: S410
from zeep import Client

from tap_twinfield.cleaners import CLEANERS
from tap_twinfield.queries import QUERIES

# Disable warnings for sub packages
logging.getLogger('zeep').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)


API_SCHEME: str = 'https://'
API_BASE_URL: str = 'login.twinfield.com'
API_BASE_PATH: str = '/webservices'
API_PATH_SESSION: str = '/session.asmx?wsdl'
API_PATH_PROCESS_XML: str = '/processxml.asmx?wsdl'


class Twinfield(object):  # noqa: WPS214, WPS230
    """Twinfield API."""

    def __init__(
        self,
        username: str,
        password: str,
        organisation: str,
        office: str,
    ) -> None:
        """Initialize object.

        Arguments:
            username {str} -- Twinfield username
            password {str} -- Twinfield password
            organisation {str} -- Twinfield organisation
            office {str} -- Twinfield office code
        """
        self.username: str = username
        self.password: str = password
        self.organisation: str = organisation
        self.office: str = office
        self._auth_header: dict = {}
        self.cluser: str
        self._logged_in: bool = False

        # Setup logger
        self.logger: logging.RootLogger = singer.get_logger()

        self._login()
        self.session: Client = self._create_session()

    def select_company(self, company: str) -> None:
        """Select a different company.

        Arguments:
            company {str} --Company name

        Raises:
            RuntimeError: WHen not logged in
        """
        if not self.session:
            raise RuntimeError(
                'Must create a session before company can be switched',
            )

        # Query API
        self.session.service.SelectCompany(
            company,
            _soapheaders={'Header': self._auth_header},
        )

        self.logger.info(f'Switched to company: {company}')

    def export_data(self, query: str) -> List[dict]:  # noqa: WPS210
        """Export data from Twinfield.

        Arguments:
            query {str} -- Browse query

        Raises:
            RuntimeError: When not logged in

        Returns:
            List[dict] -- Query output
        """
        if not self._logged_in:
            raise RuntimeError('Must login before data can be exported')

        self.logger.info('Export query')

        # Query API
        proces: Client = Client(
            f'{self.cluster}{API_BASE_PATH}{API_PATH_PROCESS_XML}',
        )
        response: str = proces.service.ProcessXmlString(
            query,
            _soapheaders={'Header': self._auth_header},
        )

        # Get Twinfield data
        root: ElementTree.Element = ElementTree.fromstring(response)

        # Get columns
        columns: list = [element.attrib['label'] for element in root[0]]
        columns.append('?')

        # Get data
        twin_data: list = [[field.text for field in row] for row in root[1::]]

        # Convert to DataFrame
        df: pd.DataFrame = pd.DataFrame(twin_data, columns=columns)

        # Remove unknown columns
        df.drop('?', axis=1, inplace=True)

        # Return rows
        return df.to_dict(orient='records')

    def get_all_browse_fields(self) -> str:
        """Retrieve all possible browse fields.

        Returns:
            str -- All possible browse fields
        """
        query: str = """
        <list>
            <type>browsefields</type>
        </list>
        """
        self.logger.info('Retrieve all possible browse fields')

        # Query API
        proces: Client = Client(
            f'{self.cluster}{API_BASE_PATH}{API_PATH_PROCESS_XML}',
        )
        response: str = proces.service.ProcessXmlString(
            query,
            _soapheaders={'Header': self._auth_header},
        )

        # Prettify output
        root: HtmlElement = fromstring(response)
        return etree.tostring(root, encoding='unicode', pretty_print=True)

    def get_browse_fields(  # noqa: WPS210
        self,
        code: str,
        to_file: bool = False,
    ) -> str:
        """Retrieve all possible browse fields for a code.

        Arguments:
            code {str} -- Browse code

        Keyword Arguments:
            to_file {bool} -- Whether to save output to file (default: {False})

        Returns:
            str -- Browse fields for the browse code
        """
        query: str = f"""
        <read>
            <type>browse</type>
            <office>{self.office}</office>
            <code>{code}</code>
        </read>"""
        self.logger.info(f'Retrieving browse fields for browse code: {code}')

        # Query API
        proces: Client = Client(
            f'{self.cluster}{API_BASE_PATH}{API_PATH_PROCESS_XML}',
        )
        response: str = proces.service.ProcessXmlString(
            query,
            _soapheaders={'Header': self._auth_header},
        )

        # Prettify output
        root: HtmlElement = fromstring(response)
        out: str = etree.tostring(root, encoding='unicode', pretty_print=True)

        # Save output to a file
        if to_file:
            if not os.path.isdir('fields'):
                os.mkdir('fields')

            with open(f'fields/{code}.txt', 'w') as output_file:
                output_file.write(out)

        return out

    def bank_transactions(  # noqa: WPS210
        self,
        start_date: str,
    ) -> Generator[dict, None, None]:
        """Retrieve bank transactions (code: 410).

        Arguments:
            start_date {str} -- Start date e.g. 2021-01

        Returns:
            Generator[dict, None, None] -- Bank transactions
        """
        # Retrieve query
        query: str = QUERIES['410']

        # Retrieve cleanner
        cleaner: Callable = CLEANERS.get('bank_transactions', {})

        # For every month from start_date until now
        for date_month in self._start_month_till_now(start_date):

            # Replace dates in placeholders
            query = query.replace(':period_lower:', date_month)
            query = query.replace(':period_upper:', date_month)

            # Perform query
            export: List[dict] = self.export_data(query)

            # Yield data after cleaning
            yield from (
                cleaner(row, number)
                for number, row in enumerate(export)
            )

    def _start_month_till_now(self, start_date: str) -> Generator:
        """Yield YYYY/MM for every month until now.

        Arguments:
            start_date {str} -- Start month e.g. 2020-01

        Yields:
            Generator -- Every month until now.
        """
        # Parse input date
        year: int = int(start_date.split('-')[0])
        month: int = int(start_date.split('-')[1].lstrip())

        # Setup start period
        period: date = date(year, month, 1)

        # Setup itterator
        dates: rrule = rrule(
            freq=MONTHLY,
            dtstart=period,
            until=datetime.utcnow(),
        )

        # Yield dates in YYYY/MM format
        yield from (date_month.strftime('%Y/%m') for date_month in dates)

    def _login(self) -> None:
        """Authenticate with the API."""
        url: str = (
            f'{API_SCHEME}{API_BASE_URL}{API_BASE_PATH}{API_PATH_SESSION}'
        )

        # Setup client
        client: Client = Client(url)

        # Login
        auth: dict = client.service.Logon(
            self.username,
            self.password,
            self.organisation,
        )

        # Save headers
        self._auth_header = auth['header']['Header']
        self.cluster: str = auth['body']['cluster']
        self._logged_in = True

        self.logger.info(
            f"Logged in as '{self.username}' on organisation "
            f"'{self.organisation}'",
        )

    def _create_session(self) -> Client:
        """Create a session..

        Raises:
            RuntimeError: When not logged in

        Returns:
            Client -- Client Session object
        """
        if not self._logged_in:
            raise RuntimeError(
                'Must be logged in before a session can be created',
            )

        self.logger.debug('Creating a session')
        return Client(f'{self.cluster}{API_BASE_PATH}{API_PATH_SESSION}')
