"""Cleaner functions."""
# -*- coding: utf-8 -*-

from types import MappingProxyType
from typing import Any, Optional
import hashlib

from tap_twinfield.streams import STREAMS


class ConvertionError(ValueError):
    """Failed to convert value."""


def to_type_or_null(
    input_value: Any,
    data_type: Optional[Any] = None,
    nullable: bool = True,
) -> Optional[Any]:
    """Convert the input_value to the data_type.

    The input_value can be anything. This function attempts to convert the
    input_value to the data_type. The data_type can be a data type such as str,
    int or Decimal or it can be a function. If nullable is True, the value is
    converted to None in cases where the input_value == None. For example:
    a '' == None, {} == None and [] == None.

    Arguments:
        input_value {Any} -- Input value

    Keyword Arguments:
        data_type {Optional[Any]} -- Data type to convert to (default: {None})
        nullable {bool} -- Whether to convert empty to None (default: {True})

    Returns:
        Optional[Any] -- The converted value
    """
    # If the input_value is not equal to None and a data_type input exists
    if input_value and data_type:
        # Convert the input value to the data_type
        try:
            return data_type(input_value)
        except ValueError as err:
            raise ConvertionError(
                f'Could not convert {input_value} to {data_type}: {err}',
            )

    # If the input_value is equal to None and Nullable is True
    elif not input_value and nullable:
        # Convert '', {}, [] to None
        return None

    # If the input_value is equal to None, but nullable is False
    # Return the original value
    return input_value


def clean_row(row: dict, mapping: dict) -> dict:
    """Clean the row according to the mapping.

    The mapping is a dictionary with optional keys:
    - map: The name of the new key/column
    - type: A data type or function to apply to the value of the key
    - nullable: Whether to convert empty values, such as '', {} or [] to None

    Arguments:
        row {dict} -- Input row
        mapping {dict} -- Input mapping

    Returns:
        dict -- Cleaned row
    """
    cleaned: dict = {}

    key: str
    key_mapping: dict

    # For every key and value in the mapping
    for key, key_mapping in mapping.items():

        # Retrieve the new mapping or use the original
        new_mapping: str = key_mapping.get('map') or key

        # Convert the value
        cleaned[new_mapping] = to_type_or_null(
            row[key],
            key_mapping.get('type'),
            key_mapping.get('null', True),
        )

    return cleaned


def clean_bank_transactions(
    row: dict,
    row_number: int,
) -> dict:
    """Clean bank transactions.

    Arguments:
        row {dict} -- Input row
        row_number {int} -- Row number, used to construct primary key

    Returns:
        dict -- Cleaned row
    """
    # Get the mapping from the STREAMS
    mapping: Optional[dict] = STREAMS['bank_transactions'].get('mapping')
    
    # Create primary key
    row_string = str(row)
    row['id'] = hashlib.sha1(row_string.encode()).hexdigest()

    # If a mapping has been defined in STREAMS, apply it
    if mapping:
        return clean_row(row, mapping)

    # Else return the original row
    return row


def clean_general_ledger_details(
    row: dict,
    row_number: int,
) -> dict:
    """Clean transaction_details.

    Arguments:
        row {dict} -- Input row
        row_number {int} -- Row number, used to construct primary key

    Returns:
        dict -- Cleaned row
    """
    # Get the mapping from the STREAMS
    mapping: Optional[dict] = STREAMS['general_ledger_details'].get('mapping')

    # Create primary key
    row_string = str(row)

    response_row = {
        'id': hashlib.sha1(row_string.encode()).hexdigest(),
        'Administratie': row.get('Administratie'),
        'Adm.naam': row.get('Adm.naam'),
        'Jaar': row.get('Jaar'),
        'Periode': row.get('Periode'),
        'Dagboek': row.get('Dagboek'),
        'Boekingsnummer': row.get('Boekingsnummer'),
        'Status': row.get('Status'),
        'Boekdatum': row.get('Boekdatum'),
        'Valuta': row.get('Valuta'),
        'Relatie': row.get('Relatie'),
        'Relatienaam': row.get('Relatienaam'),
        'Invoerdatum': row.get('Invoerdatum'),
        'Gebruikersnaam': row.get('Gebruikersnaam'),
        'Grootboekrek.': row.get('Grootboekrek.'),
        'Grootboekrek.naam': row.get('Grootboekrek.naam'),
        'Dimensietype 1': row.get('Dimensietype 1'),
        'Kpl./rel.': row.get('Kpl./rel.'),
        'Kpl.-/rel.naam': row.get('Kpl.-/rel.naam'),
        'Dimensietype 2': row.get('Dimensietype 2'),
        'Act./proj.': row.get('Act./proj.'),
        'Act.-/proj.naam': row.get('Act.-/proj.naam'),
        'Dimensietype 3': row.get('Dimensietype 3'),
        'Bedrag': row.get('Bedrag'),
        'Basisbedrag': row.get('Basisbedrag'),
        'Rapportagebedrag': row.get('Rapportagebedrag'),
        'D/C': row.get('D/C'),
        'Btw-code': row.get('Btw-code'),
        'Btw-bedrag': row.get('Btw-bedrag'),
        'Aantal': row.get('Aantal'),
        'Cheque': row.get('Cheque'),
        'Omschrijving': row.get('Omschrijving'),
        'Factuurnummer': row.get('Factuurnummer'),
        'groups': [
            {
                'group': row.get('Groep 1'),
                'group_name': row.get('Groepnaam 1'),
            },
            {
                'group': row.get('Groep 2'),
                'group_name': row.get('Groepnaam 2'),
            },
            {
                'group': row.get('Groep 3'),
                'group_name': row.get('Groepnaam 3'),
            },
            {
                'group': row.get('Groep 4'),
                'group_name': row.get('Groepnaam 4'),
            },
            {
                'group': row.get('Groep 5'),
                'group_name': row.get('Groepnaam 5'),
            },
        ],
        'Vrij tekstveld 1': row.get('Vrij tekstveld 1'),
        'Vrij tekstveld 2': row.get('Vrij tekstveld 2'),
        'Vrij tekstveld 3': row.get('Vrij tekstveld 3'),
        'Boekingsoorsprong': row.get('Boekingsoorsprong'),
        'transactie type groep': row.get('transactie type groep'),
    }

    # # If a mapping has been defined in STREAMS, apply it
    if mapping:
        return clean_row(response_row, mapping)

    # Else return the original row
    return response_row


def clean_general_ledger_transactions(
    row: dict,
    row_number: int,
) -> dict:
    """Clean general ledger transactions.

    Arguments:
        row {dict} -- Input row
        row_number {int} -- Row number, used to construct primary key

    Returns:
        dict -- Cleaned row
    """
    # Get the mapping from the STREAMS
    mapping: Optional[dict] = STREAMS['general_ledger_transactions'].get(
        'mapping',
    )

    # Create primary key

    row_string = str(row)
    row['id'] = hashlib.sha1(row_string.encode()).hexdigest()

    # If a mapping has been defined in STREAMS, apply it
    if mapping:
        return clean_row(row, mapping)

    # Else return the original row
    return row


def clean_transactions_to_be_matched(
    row: dict,
    row_number: int,
) -> dict:
    """Clean transactions to be matched.

    Arguments:
        row {dict} -- Input row
        row_number {int} -- Row number, used to construct primary key

    Returns:
        dict -- Cleaned row
    """
    # Get the mapping from the STREAMS
    mapping: Optional[dict] = STREAMS['transactions_to_be_matched'].get(
        'mapping',
    )

    # Create primary key

    row_string = str(row)
    row['id'] = hashlib.sha1(row_string.encode()).hexdigest()


    # If a mapping has been defined in STREAMS, apply it
    if mapping:
        return clean_row(row, mapping)

    # Else return the original row
    return row


def clean_annual_report(
    row: dict,
    row_number: int,
) -> dict:
    """Clean annual report.

    Arguments:
        row {dict} -- Input row
        row_number {int} -- Row number, used to construct primary key

    Returns:
        dict -- Cleaned row
    """
    # Get the mapping from the STREAMS
    mapping: Optional[dict] = STREAMS['annual_report'].get(
        'mapping',
    )

    # Create primary key
    row_string = str(row)

    response_row = {
        'id': hashlib.sha1(row_string.encode()).hexdigest(),
        'Administratie': row.get('Administratie'),
        'Adm.naam': row.get('Adm.naam'),
        'Jaar': row.get('Jaar'),
        'Periode': row.get('Periode'),
        'Grootboekrek.': row.get('Grootboekrek.'),
        'Grootboekrek.naam': row.get('Grootboekrek.naam'),
        'Dimensietype 1': row.get('Dimensietype 1'),
        'Kpl./rel.': row.get('Kpl./rel.'),
        'Kpl.-/rel.naam': row.get('Kpl.-/rel.naam'),
        'Act./proj.': row.get('Act./proj.'),
        'Act.-/proj.naam': row.get('Act.-/proj.naam'),
        'Dimensietype 3': row.get('Dimensietype 3'),
        'Basisbedrag': row.get('Basisbedrag'),
        'Rapportagebedrag': row.get('Rapportagebedrag'),
        'D/C': row.get('D/C'),
        'Aantal': row.get('Aantal'),
        'groups': [
            {
                'group': row.get('Groep 1'),
                'group_name': row.get('Groepnaam 1'),
            },
            {
                'group': row.get('Groep 2'),
                'group_name': row.get('Groepnaam 2'),
            },
            {
                'group': row.get('Groep 3'),
                'group_name': row.get('Groepnaam 3'),
            },
            {
                'group': row.get('Groep 4'),
                'group_name': row.get('Groepnaam 4'),
            },
            {
                'group': row.get('Groep 5'),
                'group_name': row.get('Groepnaam 5'),
            },
        ],
    }

    # If a mapping has been defined in STREAMS, apply it
    if mapping:
        return clean_row(response_row, mapping)

    # Else return the original row
    return response_row


def clean_annual_report_multicurrency(
    row: dict,
    row_number: int,
) -> dict:
    """Clean annual report multicurrency.

    Arguments:
        row {dict} -- Input row
        row_number {int} -- Row number, used to construct primary key

    Returns:
        dict -- Cleaned row
    """
    # Get the mapping from the STREAMS
    mapping: Optional[dict] = STREAMS['annual_report_multicurrency'].get(
        'mapping',
    )

    # Create primary key
    row_string = str(row)

    response_row = {
        'id': hashlib.sha1(row_string.encode()).hexdigest(),
        'Administratie': row.get('Administratie'),
        'Adm.naam': row.get('Adm.naam'),
        'Jaar': row.get('Jaar'),
        'Periode': row.get('Periode'),
        'Type': row.get('Type'),
        'Grootboekrek.': row.get('Grootboekrek.'),
        'Grootboekrek.naam': row.get('Grootboekrek.naam'),
        'Valuta': row.get('Valuta'),
        'Bedrag': row.get('Bedrag'),
        'Basisbedrag': row.get('Basisbedrag'),
        'Rapportagebedrag': row.get('Rapportagebedrag'),
        'D/C': row.get('D/C'),
        'Status': row.get('Status'),
        'groups': [
            {
                'group': row.get('Groep 1'),
                'group_name': row.get('Groepnaam 1'),
            },
            {
                'group': row.get('Groep 2'),
                'group_name': row.get('Groepnaam 2'),
            },
            {
                'group': row.get('Groep 3'),
                'group_name': row.get('Groepnaam 3'),
            },
            {
                'group': row.get('Groep 4'),
                'group_name': row.get('Groepnaam 4'),
            },
            {
                'group': row.get('Groep 5'),
                'group_name': row.get('Groepnaam 5'),
            },
        ],
    }

    # If a mapping has been defined in STREAMS, apply it
    if mapping:
        return clean_row(response_row, mapping)

    # Else return the original row
    return response_row


def clean_suppliers(
    row: dict,
    row_number: int,
) -> dict:
    """Clean annual report multicurrency.

    Arguments:
        row {dict} -- Input row
        row_number {int} -- Row number, used to construct primary key

    Returns:
        dict -- Cleaned row
    """
    # Get the mapping from the STREAMS
    mapping: Optional[dict] = STREAMS['suppliers'].get(
        'mapping',
    )

    # Create primary key
    row_string = str(row)
    row['id'] = hashlib.sha1(row_string.encode()).hexdigest()

    # If a mapping has been defined in STREAMS, apply it
    if mapping:
        return clean_row(row, mapping)

    # Else return the original row
    return row


def clean_transaction_summary(
    row: dict,
    row_number: int,
) -> dict:
    """Clean transaction_summary.

    Arguments:
        row {dict} -- Input row
        row_number {int} -- Row number, used to construct primary key

    Returns:
        dict -- Cleaned row
    """
    # Get the mapping from the STREAMS
    mapping: Optional[dict] = STREAMS['transaction_summary'].get(
        'mapping',
    )

    # Create primary key
    row_string = str(row)
    row['id'] = hashlib.sha1(row_string.encode()).hexdigest()

    # If a mapping has been defined in STREAMS, apply it
    if mapping:
        return clean_row(row, mapping)

    # Else return the original row
    return row


def clean_transaction_list(
    row: dict,
    row_number: int,
) -> dict:
    """Clean transaction_list.

    Arguments:
        row {dict} -- Input row
        row_number {int} -- Row number, used to construct primary key

    Returns:
        dict -- Cleaned row
    """
    # Get the mapping from the STREAMS
    mapping: Optional[dict] = STREAMS['transaction_list'].get(
        'mapping',
    )

    # Create primary key
    row_string = str(row)
    row['id'] = hashlib.sha1(row_string.encode()).hexdigest()

    # If a mapping has been defined in STREAMS, apply it
    if mapping:
        return clean_row(row, mapping)

    # Else return the original row
    return row


# Collect all cleaners
CLEANERS: MappingProxyType = MappingProxyType({
    'bank_transactions': clean_bank_transactions,
    'general_ledger_details': clean_general_ledger_details,
    'general_ledger_transactions': clean_general_ledger_transactions,
    'transactions_to_be_matched': clean_transactions_to_be_matched,
    'annual_report': clean_annual_report,
    'annual_report_multicurrency': clean_annual_report_multicurrency,
    'suppliers': clean_suppliers,
    'transaction_summary': clean_transaction_summary,
    'transaction_list': clean_transaction_list,
})
