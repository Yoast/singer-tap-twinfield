"""Cleaner functions."""
# -*- coding: utf-8 -*-

from types import MappingProxyType
from typing import Any, Optional

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
    number: str = str(row_number).rjust(10, '0')

    period: str = row['Periode']
    period = period.replace('/', '')
    row['id'] = int(period + number)

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
    number: str = str(row_number).rjust(10, '0')

    period: str = row['Periode']
    period = period.replace('/', '')
    row['id'] = int(period + number)

    # If a mapping has been defined in STREAMS, apply it
    if mapping:
        return clean_row(row, mapping)

    # Else return the original row
    return row


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
    number: str = str(row_number).rjust(10, '0')

    period: str = row['Periode']
    period = period.replace('/', '')
    row['id'] = int(period + number)

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
    number: str = str(row_number).rjust(10, '0')

    period: str = row['Periode']
    period = period.replace('/', '')
    row['id'] = int(period + number)

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
    number: str = str(row_number).rjust(10, '0')

    period: str = row['Periode']
    period = period.replace('/', '')
    row['id'] = int(period + number)

    # If a mapping has been defined in STREAMS, apply it
    if mapping:
        return clean_row(row, mapping)

    # Else return the original row
    return row


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
    number: str = str(row_number).rjust(10, '0')

    period: str = row['Periode']
    period = period.replace('/', '')
    row['id'] = int(period + number)

    # If a mapping has been defined in STREAMS, apply it
    if mapping:
        return clean_row(row, mapping)

    # Else return the original row
    return row


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
    number: str = str(row_number).rjust(10, '0')

    period: str = row['Periode']
    period = period.replace('/', '')
    row['id'] = int(period + number)

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
    number: str = str(row_number).rjust(10, '0')

    period: str = row['Jaar/periode (JJJJ/PP)']
    period = period.replace('/', '')
    row['id'] = int(period + number)

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
    number: str = str(row_number).rjust(10, '0')

    period: str = row['Periode']
    period = period.replace('/', '')
    row['id'] = int(period + number)

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
