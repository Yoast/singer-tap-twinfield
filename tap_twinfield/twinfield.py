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

        self.logger.debug('Export query')

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

    def annual_report_multicurrency(  # noqa: WPS210
        self,
        start_date: str,
    ) -> Generator[dict, None, None]:
        """Retrieve annual multicurrency report (code: 060).

        Arguments:
            start_date {str} -- Start date e.g. 2021-01

        Returns:
            Generator[dict, None, None] -- Annual Report (Multicurrency)
        """
        # Retrieve cleaner
        cleaner: Callable = CLEANERS.get('annual_report_multicurrency', {})

        # For every month from start_date until now
        for date_month in self._start_month_till_now(start_date):

            # Retrieve query
            query: str = QUERIES['060']

            # Replace dates in placeholders
            query = query.replace(':period_lower:', date_month)
            query = query.replace(':period_upper:', date_month)

            # Perform query
            self.logger.info(
                'Extracting annual report multicurrency (060) for month '
                f'{date_month}',
            )
            export: List[dict] = self.export_data(query)

            record_count: int = len(export)
            self.logger.info(
                'Received annual report multicurrency (060) for month '
                f'{date_month}: {record_count} records',
            )

            # Yield data after cleaning
            yield from (
                cleaner(row, number)
                for number, row in enumerate(export)
            )

    def annual_report(  # noqa: WPS210
        self,
        start_date: str,
    ) -> Generator[dict, None, None]:
        """Retrieve annual report (code: 040_1).

        Arguments:
            start_date {str} -- Start date e.g. 2021-01

        Returns:
            Generator[dict, None, None] -- Annual Report
        """
        # Retrieve cleaner
        cleaner: Callable = CLEANERS.get('annual_report', {})

        # For every month from start_date until now
        for date_month in self._start_month_till_now(start_date):

            # Retrieve query
            query: str = QUERIES['040_1']

            # Replace dates in placeholders
            query = query.replace(':period_lower:', date_month)
            query = query.replace(':period_upper:', date_month)

            # Perform query
            self.logger.info(
                'Extracting annual report (040_1) for month '
                f'{date_month}',
            )
            export: List[dict] = self.export_data(query)

            record_count: int = len(export)
            self.logger.info(
                'Received annual report (040_1) for month '
                f'{date_month}: {record_count} records',
            )

            # Yield data after cleaning
            yield from (
                cleaner(row, number)
                for number, row in enumerate(export)
            )

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
        # Retrieve cleaner
        cleaner: Callable = CLEANERS.get('bank_transactions', {})

        # For every month from start_date until now
        for date_month in self._start_month_till_now(start_date):

            # Retrieve query
            query: str = QUERIES['410']

            # Replace dates in placeholders
            query = query.replace(':period_lower:', date_month)
            query = query.replace(':period_upper:', date_month)

            # Perform query
            self.logger.info(
                'Extracting bank transactions (410) for month '
                f'{date_month}',
            )
            export: List[dict] = self.export_data(query)

            record_count: int = len(export)
            self.logger.info(
                'Received bank transactions (410) for month '
                f'{date_month}: {record_count} records',
            )

            # Yield data after cleaning
            yield from (
                cleaner(row, number)
                for number, row in enumerate(export)
            )

    def general_ledger_details(  # noqa: WPS210
        self,
        start_date: str,
    ) -> Generator[dict, None, None]:
        """Retrieve transactions details (code: 030_3).

        Arguments:
            start_date {str} -- Start date e.g. 2021-01

        Returns:
            Generator[dict, None, None] -- General Ledger Details (v3)
        """
        # Retrieve cleaner
        cleaner: Callable = CLEANERS.get('general_ledger_details', {})

        # For every month from start_date until now
        for date_month in self._start_month_till_now(start_date):

            # Retrieve query
            query: str = QUERIES['030_3']

            # Replace dates in placeholders
            query = query.replace(':period_lower:', date_month)
            query = query.replace(':period_upper:', date_month)

            # Perform query
            self.logger.info(
                'Extracting general ledger details (030_3) for month '
                f'{date_month}',
            )
            export: List[dict] = self.export_data(query)

            record_count: int = len(export)
            self.logger.info(
                'Received general ledger details (030_3) for month '
                f'{date_month}: {record_count} records',
            )

            # Yield data after cleaning
            yield from (
                cleaner(row, number)
                for number, row in enumerate(export)
            )

    def general_ledger_transactions(  # noqa: WPS210
        self,
        start_date: str,
    ) -> Generator[dict, None, None]:
        """Retrieve general ledger transactions (code: 000).

        Arguments:
            start_date {str} -- Start date e.g. 2021-01

        Returns:
            Generator[dict, None, None] -- General Ledger Transactions
        """
        # Retrieve cleaner
        cleaner: Callable = CLEANERS.get('general_ledger_transactions', {})

        # For every month from start_date until now
        for date_month in self._start_month_till_now(start_date):

            # Retrieve query
            query: str = QUERIES['000']

            # Replace dates in placeholders
            query = query.replace(':period_lower:', date_month)
            query = query.replace(':period_upper:', date_month)

            # Perform query
            self.logger.info(
                'Extracting general ledger transactions (000) for month '
                f'{date_month}',
            )
            export: List[dict] = self.export_data(query)

            record_count: int = len(export)
            self.logger.info(
                'Received general ledger transactions (000) for month '
                f'{date_month}: {record_count} records',
            )

            # Yield data after cleaning
            yield from (
                cleaner(row, number)
                for number, row in enumerate(export)
            )

    def suppliers(  # noqa: WPS210
        self,
        start_date: str,
    ) -> Generator[dict, None, None]:
        """Retrieve suppliers (code: 230_2).

        Arguments:
            start_date {str} -- Start date e.g. 2021-01

        Returns:
            Generator[dict, None, None] -- Supplier Invoices
        """
        # Retrieve cleaner
        cleaner: Callable = CLEANERS.get('suppliers', {})

        # For every month from start_date until now
        for date_month in self._start_month_till_now(start_date):

            # Retrieve query
            query: str = QUERIES['230_2']

            # Replace dates in placeholders
            query = query.replace(':period_lower:', date_month)
            query = query.replace(':period_upper:', date_month)

            # Perform query
            self.logger.info(
                'Extracting suppliers (230_2) for month '
                f'{date_month}',
            )
            export: List[dict] = self.export_data(query)

            record_count: int = len(export)
            self.logger.info(
                'Received suppliers (230_2) for month '
                f'{date_month}: {record_count} records',
            )

            # Yield data after cleaning
            yield from (
                cleaner(row, number)
                for number, row in enumerate(export)
            )

    def transaction_list(  # noqa: WPS210
        self,
        start_date: str,
    ) -> Generator[dict, None, None]:
        """Retrieve transaction list (code: 020).

        Arguments:
            start_date {str} -- Start date e.g. 2021-01

        Returns:
            Generator[dict, None, None] -- Transaction list
        """
        # Retrieve cleaner
        cleaner: Callable = CLEANERS.get('transaction_list', {})

        # For every month from start_date until now
        for date_month in self._start_month_till_now(start_date):

            # Retrieve query
            query: str = QUERIES['020']

            # Replace dates in placeholders
            query = query.replace(':period_lower:', date_month)
            query = query.replace(':period_upper:', date_month)

            # Perform query
            self.logger.info(
                'Extracting transaction list (020) for month '
                f'{date_month}',
            )
            export: List[dict] = self.export_data(query)

            record_count: int = len(export)
            self.logger.info(
                'Received transaction list (020) for month '
                f'{date_month}: {record_count} records',
            )

            # Yield data after cleaning
            yield from (
                cleaner(row, number)
                for number, row in enumerate(export)
            )

    def transaction_summary(  # noqa: WPS210
        self,
        start_date: str,
    ) -> Generator[dict, None, None]:
        """Retrieve transaction summary (code: 670).

        Arguments:
            start_date {str} -- Start date e.g. 2021-01

        Returns:
            Generator[dict, None, None] -- Transaction Summary
        """
        # Retrieve cleaner
        cleaner: Callable = CLEANERS.get('transaction_summary', {})

        # For every month from start_date until now
        for date_month in self._start_month_till_now(start_date):

            # Retrieve query
            query: str = QUERIES['670']

            # Replace dates in placeholders
            query = query.replace(':period_lower:', date_month)
            query = query.replace(':period_upper:', date_month)

            # Perform query
            self.logger.info(
                'Extracting transaction summary (670) for month '
                f'{date_month}',
            )
            export: List[dict] = self.export_data(query)

            record_count: int = len(export)
            self.logger.info(
                'Received transaction summary (670) for month '
                f'{date_month}: {record_count} records',
            )

            # Yield data after cleaning
            yield from (
                cleaner(row, number)
                for number, row in enumerate(export)
            )

    def transactions_to_be_matched(  # noqa: WPS210
        self,
        start_date: str,
    ) -> Generator[dict, None, None]:
        """Retrieve transactions to be matched (code: 010).

        Arguments:
            start_date {str} -- Start date e.g. 2021-01

        Returns:
            Generator[dict, None, None] -- Transactions still to be matched
        """
        # Retrieve cleaner
        cleaner: Callable = CLEANERS.get('transactions_to_be_matched', {})

        # For every month from start_date until now
        for date_month in self._start_month_till_now(start_date):

            # Retrieve query
            query: str = QUERIES['010']

            # Replace dates in placeholders
            query = query.replace(':period_lower:', date_month)
            query = query.replace(':period_upper:', date_month)

            # Perform query
            self.logger.info(
                'Extracting transactions to be matched (010) for month '
                f'{date_month}',
            )
            export: List[dict] = self.export_data(query)

            record_count: int = len(export)
            self.logger.info(
                'Received transactions to be matched (010) for month '
                f'{date_month}: {record_count} records',
            )

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
