"""Twinfield API."""
# -*- coding: utf-8 -*-

import logging
import os

import pandas as pd
from defusedxml import ElementTree
from lxml import etree, html
from lxml.html import HtmlElement
from zeep import Client


logging.getLogger('zeep').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)


LOGIN_URL: str = 'https://login.twinfield.com/webservices/session.asmx?wsdl'
ENDPOINT_SESSION: str = '/webservices/session.asmx?wsdl'
ENDPOINT_PROCESSXML: str = '/webservices/processxml.asmx?wsdl'


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
        self._setup_logging()

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
                'Must create a session before company can be switched'
            )

        # Query API
        self.session.service.SelectCompany(
            company,
            _soapheaders={'Header': self._auth_header},
        )

        self.logger.info(f'Switched to company: {company}')

    def export_data(self, query: str) -> pd.DataFrame:
        """Export data from Twinfield.

        Arguments:
            query {str} -- Browse query

        Raises:
            RuntimeError: When not logged in

        Returns:
            pd.DataFrame -- Query output
        """
        if not self._logged_in:
            raise RuntimeError('Must login before data can be exported')

        self.logger.info('Export query')

        # Query API
        proces: Client = Client(self.cluster + ENDPOINT_PROCESSXML)
        response: str = proces.service.ProcessXmlString(
            query,
            _soapheaders={'Header': self._auth_header},
        )

        # Parse data
        
        self.logger.debug(response[:1000])
        root: ElementTree.Element = ElementTree.fromstring(response)
        columns: list = [element.attrib['label'] for element in root[0]]
        columns.append('?')
        twin_data: list = [[field.text for field in row] for row in root[1::]]
        self.logger.debug(columns)
        # self.logger.debug(twin_data)

        # Convert to DataFrame
        df: pd.DataFrame = pd.DataFrame(twin_data, columns=columns)
        return df.drop('?', axis=1)

    def get_all_browse_fields(self) -> str:
        """Retrieve all possible browse fields.

        Returns:
            str -- All possible browse fields
        """
        query: str = '''
        <list>
            <type>browsefields</type>
        </list>
        '''
        self.logger.info('Retrieve all possible browse fields')

        # Query API
        proces: Client = Client(self.cluster + ENDPOINT_PROCESSXML)
        response: str = proces.service.ProcessXmlString(
            query,
            _soapheaders={'Header': self._auth_header},
        )

        # Prettify output
        root: HtmlElement = html.fromstring(response)
        return etree.tostring(root, encoding='unicode', pretty_print=True)

    def get_browse_fields(self, code: str, to_file: bool = False) -> str:
        """Retrieve all possible browse fields for a code.

        Arguments:
            code {str} -- Browse code

        Keyword Arguments:
            to_file {bool} -- Whether to save output to file (default: {False})

        Returns:
            str -- Browse fields for the browse code
        """
        query: str = f'''
        <read>
            <type>browse</type>
            <office>{self.office}</office>
            <code>{code}</code>
        </read>'''
        self.logger.info(f'Retrieving browse fields for browse code: {code}')

        # Query API
        proces: Client = Client(self.cluster + ENDPOINT_PROCESSXML)
        response: str = proces.service.ProcessXmlString(
            query,
            _soapheaders={'Header': self._auth_header},
        )

        # Prettify output
        root: HtmlElement = html.fromstring(response)
        out: str = etree.tostring(root, encoding='unicode', pretty_print=True)

        # Save output to a file
        if to_file:
            if not os.path.isdir('fields'):
                os.mkdir('fields')

            with open(f'fields/{code}.txt', 'w') as output_file:
                output_file.write(out)

        return out

    def _setup_logging(self) -> None:
        """Set up logging."""
        self.logger: logging.Logger = logging.getLogger('twinfield')
        stream_handler: logging.StreamHandler = logging.StreamHandler()
        formatter: logging.Formatter = logging.Formatter(
            '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        )
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)
        self.logger.setLevel(logging.DEBUG)

    def _login(self) -> None:
        """Authenticate with the API."""
        login: Client = Client(LOGIN_URL)

        auth: dict = login.service.Logon(
            self.username,
            self.password,
            self.organisation,
        )

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
        return Client(self.cluster + ENDPOINT_SESSION)
