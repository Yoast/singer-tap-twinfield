"""Streams metadata."""
# -*- coding: utf-8 -*-

from datetime import datetime
from decimal import Decimal
from types import MappingProxyType

from dateutil.parser import parse as parse_date

# Helper constants for timezone parsing
HOUR: int = 3600
TIMEZONES: MappingProxyType = MappingProxyType({
    'A': HOUR,
    'ACDT': 10.5 * HOUR,  # noqa: WPS432
    'ACST': 9.5 * HOUR,  # noqa: WPS432
    'ACT': -5 * HOUR,  # noqa: WPS432
    'ACWST': 8.75 * HOUR,  # noqa: WPS432
    'ADT': 4 * HOUR,  # noqa: WPS432
    'AEDT': 11 * HOUR,  # noqa: WPS432
    'AEST': 10 * HOUR,  # noqa: WPS432
    'AET': 10 * HOUR,
    'AFT': 4.5 * HOUR,  # noqa: WPS432
    'AKDT': -8 * HOUR,
    'AKST': -9 * HOUR,
    'ALMT': 6 * HOUR,  # noqa: WPS432
    'AMST': -3 * HOUR,  # noqa: WPS432
    'AMT': -4 * HOUR,  # noqa: WPS432
    'ANAST': 12 * HOUR,  # noqa: WPS432
    'ANAT': 12 * HOUR,  # noqa: WPS432
    'AQTT': 5 * HOUR,  # noqa: WPS432
    'ART': -3 * HOUR,
    'AST': 3 * HOUR,  # noqa: WPS432
    'AT': -4 * HOUR,
    'AWDT': 9 * HOUR,  # noqa: WPS432
    'AWST': 8 * HOUR,  # noqa: WPS432
    'AZOST': 0,
    'AZOT': -1 * HOUR,
    'AZST': 5 * HOUR,
    'AZT': 4 * HOUR,
    'AoE': -12 * HOUR,  # noqa: WPS432
    'B': 2 * HOUR,
    'BNT': 8 * HOUR,
    'BOT': -4 * HOUR,
    'BRST': -2 * HOUR,
    'BRT': -3 * HOUR,
    'BST': 6 * HOUR,
    'BTT': 6 * HOUR,
    'C': 3 * HOUR,
    'CAST': 8 * HOUR,
    'CAT': 2 * HOUR,
    'CCT': 6.5 * HOUR,  # noqa: WPS432
    'CDT': -5 * HOUR,
    'CEST': 2 * HOUR,
    'CET': HOUR,
    'CHADT': 13.75 * HOUR,  # noqa: WPS432
    'CHAST': 12.75 * HOUR,  # noqa: WPS432
    'CHOST': 9 * HOUR,
    'CHOT': 8 * HOUR,
    'CHUT': 10 * HOUR,
    'CIDST': -4 * HOUR,
    'CIST': -5 * HOUR,
    'CKT': -10 * HOUR,
    'CLST': -3 * HOUR,
    'CLT': -4 * HOUR,
    'COT': -5 * HOUR,
    'CST': -6 * HOUR,
    'CT': -6 * HOUR,
    'CVT': -1 * HOUR,
    'CXT': 7 * HOUR,
    'ChST': 10 * HOUR,
    'D': 4 * HOUR,
    'DAVT': 7 * HOUR,
    'DDUT': 10 * HOUR,
    'E': 5 * HOUR,
    'EASST': -5 * HOUR,
    'EAST': -6 * HOUR,
    'EAT': 3 * HOUR,
    'ECT': -5 * HOUR,
    'EDT': -4 * HOUR,
    'EEST': 3 * HOUR,
    'EET': 2 * HOUR,
    'EGST': 0,
    'EGT': -1 * HOUR,
    'EST': -5 * HOUR,
    'ET': -5 * HOUR,
    'F': 6 * HOUR,
    'FET': 3 * HOUR,
    'FJST': 13 * HOUR,  # noqa: WPS432
    'FJT': 12 * HOUR,  # noqa: WPS432
    'FKST': -3 * HOUR,
    'FKT': -4 * HOUR,
    'FNT': -2 * HOUR,
    'G': 7 * HOUR,
    'GALT': -6 * HOUR,
    'GAMT': -9 * HOUR,
    'GET': 4 * HOUR,
    'GFT': -3 * HOUR,
    'GILT': 12 * HOUR,  # noqa: WPS432
    'GMT': 0,
    'GST': 4 * HOUR,
    'GYT': -4 * HOUR,
    'H': 8 * HOUR,
    'HDT': -9 * HOUR,
    'HKT': 8 * HOUR,
    'HOVST': 8 * HOUR,
    'HOVT': 7 * HOUR,
    'HST': -10 * HOUR,
    'I': 9 * HOUR,
    'ICT': 7 * HOUR,
    'IDT': 3 * HOUR,
    'IOT': 6 * HOUR,
    'IRDT': 4.5 * HOUR,  # noqa: WPS432
    'IRKST': 9 * HOUR,
    'IRKT': 8 * HOUR,
    'IRST': 3.5 * HOUR,  # noqa: WPS432
    'IST': 5.5 * HOUR,  # noqa: WPS432
    'JST': 9 * HOUR,
    'K': 10 * HOUR,
    'KGT': 6 * HOUR,
    'KOST': 11 * HOUR,  # noqa: WPS432
    'KRAST': 8 * HOUR,
    'KRAT': 7 * HOUR,
    'KST': 9 * HOUR,
    'KUYT': 4 * HOUR,
    'L': 11 * HOUR,  # noqa: WPS432
    'LHDT': 11 * HOUR,  # noqa: WPS432
    'LHST': 10.5 * HOUR,  # noqa: WPS432
    'LINT': 14 * HOUR,  # noqa: WPS432
    'M': 12 * HOUR,  # noqa: WPS432
    'MAGST': 12 * HOUR,  # noqa: WPS432
    'MAGT': 11 * HOUR,  # noqa: WPS432
    'MART': 9.5 * HOUR,  # noqa: WPS432
    'MAWT': 5 * HOUR,
    'MDT': -6 * HOUR,
    'MHT': 12 * HOUR,  # noqa: WPS432
    'MMT': 6.5 * HOUR,  # noqa: WPS432
    'MSD': 4 * HOUR,
    'MSK': 3 * HOUR,
    'MST': -7 * HOUR,
    'MT': -7 * HOUR,
    'MUT': 4 * HOUR,
    'MVT': 5 * HOUR,
    'MYT': 8 * HOUR,
    'N': -1 * HOUR,
    'NCT': 11 * HOUR,  # noqa: WPS432
    'NDT': 2.5 * HOUR,  # noqa: WPS432
    'NFT': 11 * HOUR,  # noqa: WPS432
    'NOVST': 7 * HOUR,
    'NOVT': 7 * HOUR,
    'NPT': 5.5 * HOUR,  # noqa: WPS432
    'NRT': 12 * HOUR,  # noqa: WPS432
    'NST': 3.5 * HOUR,  # noqa: WPS432
    'NUT': -11 * HOUR,  # noqa: WPS432
    'NZDT': 13 * HOUR,  # noqa: WPS432
    'NZST': 12 * HOUR,  # noqa: WPS432
    'O': -2 * HOUR,
    'OMSST': 7 * HOUR,
    'OMST': 6 * HOUR,
    'ORAT': 5 * HOUR,
    'P': -3 * HOUR,
    'PDT': -7 * HOUR,
    'PET': -5 * HOUR,
    'PETST': 12 * HOUR,  # noqa: WPS432
    'PETT': 12 * HOUR,  # noqa: WPS432
    'PGT': 10 * HOUR,
    'PHOT': 13 * HOUR,  # noqa: WPS432
    'PHT': 8 * HOUR,
    'PKT': 5 * HOUR,
    'PMDT': -2 * HOUR,
    'PMST': -3 * HOUR,
    'PONT': 11 * HOUR,  # noqa: WPS432
    'PST': -8 * HOUR,
    'PT': -8 * HOUR,
    'PWT': 9 * HOUR,
    'PYST': -3 * HOUR,
    'PYT': -4 * HOUR,
    'Q': -4 * HOUR,
    'QYZT': 6 * HOUR,
    'R': -5 * HOUR,
    'RET': 4 * HOUR,
    'ROTT': -3 * HOUR,
    'S': -6 * HOUR,
    'SAKT': 11 * HOUR,  # noqa: WPS432
    'SAMT': 4 * HOUR,
    'SAST': 2 * HOUR,
    'SBT': 11 * HOUR,  # noqa: WPS432
    'SCT': 4 * HOUR,
    'SGT': 8 * HOUR,
    'SRET': 11 * HOUR,  # noqa: WPS432
    'SRT': -3 * HOUR,
    'SST': -11 * HOUR,  # noqa: WPS432
    'SYOT': 3 * HOUR,
    'T': -7 * HOUR,
    'TAHT': -10 * HOUR,
    'TFT': 5 * HOUR,
    'TJT': 5 * HOUR,
    'TKT': 13 * HOUR,  # noqa: WPS432
    'TLT': 9 * HOUR,
    'TMT': 5 * HOUR,
    'TOST': 14 * HOUR,  # noqa: WPS432
    'TOT': 13 * HOUR,  # noqa: WPS432
    'TRT': 3 * HOUR,
    'TVT': 12 * HOUR,  # noqa: WPS432
    'U': -8 * HOUR,
    'ULAST': 9 * HOUR,
    'ULAT': 8 * HOUR,
    'UTC': 0,
    'UYST': -2 * HOUR,
    'UYT': -3 * HOUR,
    'UZT': 5 * HOUR,
    'V': -9 * HOUR,
    'VET': -4 * HOUR,
    'VLAST': 11 * HOUR,  # noqa: WPS432
    'VLAT': 10 * HOUR,
    'VOST': 6 * HOUR,
    'VUT': 11 * HOUR,  # noqa: WPS432
    'W': -10 * HOUR,
    'WAKT': 12 * HOUR,  # noqa: WPS432
    'WARST': -3 * HOUR,
    'WAST': 2 * HOUR,
    'WAT': HOUR,
    'WEST': HOUR,
    'WET': 0,
    'WFT': 12 * HOUR,  # noqa: WPS432
    'WGST': -2 * HOUR,
    'WGT': -3 * HOUR,
    'WIB': 7 * HOUR,
    'WIT': 9 * HOUR,
    'WITA': 8 * HOUR,
    'WST': 14 * HOUR,  # noqa: WPS432
    'WT': 0,
    'X': -11 * HOUR,  # noqa: WPS432
    'Y': -12 * HOUR,  # noqa: WPS432
    'YAKST': 10 * HOUR,
    'YAKT': 9 * HOUR,
    'YAPT': 10 * HOUR,
    'YEKST': 6 * HOUR,
    'YEKT': 5 * HOUR,
    'Z': 0,
})


def date_parser(input_date: str) -> str:
    """Help function to parse timezones correctly in strings.

    Arguments:
        input_date {str} -- Input date as string

    Returns:
        {str} -- Date in isoformat
    """
    parsed_date: datetime = parse_date(input_date, tzinfos=TIMEZONES)
    return parsed_date.isoformat()


# Streams metadata
STREAMS: MappingProxyType = MappingProxyType({
    'bank_transactions': {
        'key_properties': 'id',
        'replication_method': 'INCREMENTAL',
        'replication_key': 'id',
        'bookmark': 'start_date',
        'mapping': {
            'id': {
                'map': 'id', 'null': False,
            },
            'Periode': {
                'map': 'yearperiod', 'null': False,
            },
            'Bank': {
                'map': 'bank_code', 'null': False,
            },
            'Bank Naam': {
                'map': 'bank_shortname', 'null': False,
            },
            'Boekst.nr.': {
                'map': 'entry_number', 'type': int, 'null': False,
            },
            'Afschriftnr.': {
                'map': 'statement_number', 'type': int, 'null': False,
            },
            'Grootboek': {
                'map': 'ledger', 'null': False,
            },
            'Grootboek Naam': {
                'map': 'ledger_name', 'null': False,
            },
            'Valuta': {
                'map': 'curcode', 'null': False,
            },
            'Bedrag': {
                'map': 'value_signed', 'type': Decimal, 'null': False,
            },
            'Euro': {
                'map': 'basevalue_signed', 'type': Decimal, 'null': False,
            },
            'Vorig saldo': {
                'map': 'startvalue', 'type': Decimal, 'null': False,
            },
            'Eindsaldo': {
                'map': 'closevalue', 'type': Decimal, 'null': False,
            },
            'Status': {
                'map': 'status', 'null': False,
            },
        },
    },
    'transaction_list': {
        'key_properties': 'id',
        'replication_method': 'INCREMENTAL',
        'replication_key': 'id',
        'bookmark': 'start_date',
        'mapping': {
            'id': {
                'map': 'id', 'null': False,
            },
            'Periode': {
                'map': 'yearperiod', 'null': False,
            },
            'Dagboek': {
                'map': 'journal', 'null': False,
            },
            'Naam': {
                'map': 'journal_name', 'null': False,
            },
            'Boekst.nr.': {
                'map': 'booking_number', 'type': int, 'null': False,
            },
            'Status': {
                'map': 'booking_status', 'null': False,
            },
            'Boekdatum': {
                'map': 'booking_date', 'type': date_parser, 'null': False,
            },
            'Grootboek': {
                'map': 'ledger', 'type': int, 'null': False,
            },
            'Relatie': {
                'map': 'relation', 'null': True,
            },
            'Project': {
                'map': 'project', 'null': True,
            },
            'Valuta': {
                'map': 'curcode', 'null': False,
            },
            'Bedrag': {
                'map': 'valuesigned', 'type': Decimal, 'null': False,
            },
            'Euro': {
                'map': 'base_valuesigned', 'type': Decimal, 'null': False,
            },
            'Factuurnr.': {
                'map': 'invoice_number', 'null': True,
            },
            'Invoerdatum': {
                'map': 'entry_date', 'type': date_parser, 'null': False,
            },
            'Omschrijving': {
                'map': 'description', 'null': True,
            },
            'Regime': {
                'map': 'regime', 'null': True,
            }
        },
    },
    'general_ledger_transactions': {
        'key_properties': 'id',
        'replication_method': 'INCREMENTAL',
        'replication_key': 'id',
        'bookmark': 'start_date',
        'mapping': {
            'id': {
                'map': 'id', 'null': False,
            },
            'Periode': {
                'map': 'yearperiod', 'null': False,
            },
            'Dagboek': {
                'map': 'journal', 'null': False,
            },
            'Naam': {
                'map': 'journal_name', 'null': False,
            },
            'Boekst.nr.': {
                'map': 'booking_number', 'type': int, 'null': False,
            },
            'Status': {
                'map': 'booking_status', 'null': False,
            },
            'Grootboek': {
                'map': 'ledger', 'type': int, 'null': False,
            },
            'Valuta': {
                'map': 'curcode', 'null': False,
            },
            'Bedrag': {
                'map': 'valuesigned', 'type': Decimal, 'null': False,
            },
            'Euro': {
                'map': 'base_valuesigned', 'type': Decimal, 'null': False,
            },
            'Omschrijving': {
                'map': 'description', 'null': True,
            },
            'Regime': {
                'map': 'regime', 'null': True,
            }
        },
    },
    'transactions_to_be_matched': {
        'key_properties': 'id',
        'replication_method': 'INCREMENTAL',
        'replication_key': 'id',
        'bookmark': 'start_date',
        'mapping': {
            'id': {
                'map': 'id', 'null': False,
            },
            'Periode': {
                'map': 'yearperiod', 'null': False,
            },
            'Grootboek': {
                'map': 'ledger', 'type': int, 'null': False,
            },
            'Naam': {
                'map': 'ledger_name', 'null': False,
            },
            'Dagboek': {
                'map': 'journal', 'null': False,
            },
            'Boekst.nr.': {
                'map': 'booking_number', 'type': int, 'null': False,
            },
            'Valuta': {
                'map': 'curcode', 'null': False,
            },
            'Bedrag': {
                'map': 'valuesigned', 'type': Decimal, 'null': False,
            },
            'Euro': {
                'map': 'base_valuesigned', 'type': Decimal, 'null': False,
            },
            'Openstaand bedrag': {
                'map': 'openbase_valuesigned', 'type': Decimal, 'null': False,
            },
            'Betaalstatus': {
                'map': 'payment_status', 'null': False,
            },
            'Regime': {
                'map': 'regime', 'null': True,
            }
        },
    },
    'general_ledger_details': {
        'key_properties': 'id',
        'replication_method': 'INCREMENTAL',
        'replication_key': 'id',
        'bookmark': 'start_date',
        'mapping': {
            'id': {
                'map': 'id', 'null': False,
            },
            'Administratie': {
                'map': 'office', 'null': False,
            },
            'Adm.naam': {
                'map': 'office_name', 'null': False,
            },
            'Jaar': {
                'map': 'year', 'type': int, 'null': False,
            },
            'Periode': {
                'map': 'period', 'type': int, 'null': False,
            },
            'Dagboek': {
                'map': 'journal', 'null': False,
            },
            'Boekingsnummer': {
                'map': 'booking_number', 'type': int, 'null': False,
            },
            'Status': {
                'map': 'status', 'null': False,
            },
            'Boekdatum': {
                'map': 'book_date', 'type': date_parser, 'null': False,
            },
            'Valuta': {
                'map': 'curcode', 'null': False,
            },
            'Relatie': {
                'map': 'relation', 'null': True,
            },
            'Relatienaam': {
                'map': 'relation_name', 'null': True,
            },
            'Invoerdatum': {
                'map': 'input_date', 'type': date_parser, 'null': False,
            },
            'Gebruikersnaam': {
                'map': 'username', 'null': False,
            },
            'Grootboekrek.': {
                'map': 'ledger', 'type': int, 'null': False,
            },
            'Grootboekrek.naam': {
                'map': 'ledger_name', 'null': False,
            },
            'Dimensietype 1': {
                'map': 'ledger_type', 'null': False,
            },
            'Kpl./rel.': {
                'map': 'cost_centre', 'null': True,
            },
            'Kpl.-/rel.naam': {
                'map': 'cost_centre_name', 'null': True,
            },
            'Dimensietype 2': {
                'map': 'cost_centre_type', 'null': True,
            },
            'Act./proj.': {
                'map': 'project', 'null': True,
            },
            'Act.-/proj.naam': {
                'map': 'project_name', 'null': True,
            },
            'Dimensietype 3': {
                'map': 'project_type', 'null': True,
            },
            'Bedrag': {
                'map': 'valuesigned', 'type': Decimal, 'null': False,
            },
            'Basisbedrag': {
                'map': 'base_valuesigned', 'type': Decimal, 'null': False,
            },
            'Rapportagebedrag': {
                'map': 'report_valuesigned', 'type': Decimal, 'null': True,
            },
            'D/C': {
                'map': 'debitcredit', 'null': False,
            },
            'Btw-code': {
                'map': 'vatcode', 'null': True,
            },
            'Btw-bedrag': {
                'map': 'vatbasevaluesigned', 'type': Decimal, 'null': True,
            },
            'Aantal': {
                'map': 'quantity', 'type': int, 'null': True,
            },
            'Cheque': {
                'map': 'cheque_number', 'null': True,
            },
            'Omschrijving': {
                'map': 'description', 'null': True,
            },
            'Factuurnummer': {
                'map': 'invoice_number', 'null': True,
            },
            'groups': {
                'map': 'groups', 'null': True,
            },
            'Vrij tekstveld 1': {
                'map': 'freetext1', 'null': True,
            },
            'Vrij tekstveld 2': {
                'map': 'freetext2', 'null': True,
            },
            'Vrij tekstveld 3': {
                'map': 'freetext3', 'null': True,
            },
            'Boekingsoorsprong': {
                'map': 'origin', 'null': False,
            },
            'transactie type groep': {
                'map': 'type', 'null': False,
            },
        },
    },
    'annual_report': {
        'key_properties': 'id',
        'replication_method': 'INCREMENTAL',
        'replication_key': 'id',
        'bookmark': 'start_date',
        'mapping': {
            'id': {
                'map': 'id', 'null': False,
            },
            'Administratie': {
                'map': 'office', 'null': False,
            },
            'Adm.naam': {
                'map': 'office_name', 'null': False,
            },
            'Jaar': {
                'map': 'year', 'type': int, 'null': False,
            },
            'Periode': {
                'map': 'period', 'type': int, 'null': False,
            },
            'Grootboekrek.': {
                'map': 'ledger', 'type': int, 'null': False,
            },
            'Grootboekrek.naam': {
                'map': 'ledger_name', 'null': False,
            },
            'Dimensietype 1': {
                'map': 'ledger_type', 'null': False,
            },
            'Kpl./rel.': {
                'map': 'cost_centre', 'null': True,
            },
            'Kpl.-/rel.naam': {
                'map': 'cost_centre_name', 'null': True,
            },
            'Act./proj.': {
                'map': 'project', 'null': True,
            },
            'Act.-/proj.naam': {
                'map': 'project_name', 'null': True,
            },
            'Dimensietype 3': {
                'map': 'project_type', 'null': True,
            },
            'Basisbedrag': {
                'map': 'base_valuesigned', 'type': Decimal, 'null': False,
            },
            'Rapportagebedrag': {
                'map': 'report_valuesigned', 'type': Decimal, 'null': True,
            },
            'D/C': {
                'map': 'debitcredit', 'null': False,
            },
            'Aantal': {
                'map': 'quantity', 'type': int, 'null': True,
            },
            'groups': {
                'map': 'groups', 'null': True,
            },
        },
    },
    'annual_report_multicurrency': {
        'key_properties': 'id',
        'replication_method': 'INCREMENTAL',
        'replication_key': 'id',
        'bookmark': 'start_date',
        'mapping': {
            'id': {
                'map': 'id', 'null': False,
            },
            'Administratie': {
                'map': 'office', 'null': False,
            },
            'Adm.naam': {
                'map': 'office_name', 'null': False,
            },
            'Jaar': {
                'map': 'year', 'type': int, 'null': False,
            },
            'Periode': {
                'map': 'period', 'type': int, 'null': False,
            },
            'Type': {
                'map': 'ledger_type', 'null': False,
            },
            'Grootboekrek.': {
                'map': 'ledger', 'type': int, 'null': False,
            },
            'Grootboekrek.naam': {
                'map': 'ledger_name', 'null': False,
            },
            'Valuta': {
                'map': 'curcode', 'null': False,
            },
            'Bedrag': {
                'map': 'valuesigned', 'type': Decimal, 'null': False,
            },
            'Basisbedrag': {
                'map': 'base_valuesigned', 'type': Decimal, 'null': False,
            },
            'Rapportagebedrag': {
                'map': 'report_valuesigned', 'type': Decimal, 'null': True,
            },
            'D/C': {
                'map': 'debitcredit', 'null': False,
            },
            'Status': {
                'map': 'status', 'null': False,
            },
            'groups': {
                'map': 'groups', 'null': True,
            },
        },
    },
    'suppliers': {
        'key_properties': 'id',
        'replication_method': 'INCREMENTAL',
        'replication_key': 'id',
        'bookmark': 'start_date',
        'mapping': {
            'id': {
                'map': 'id', 'null': False,
            },
            'Administratie': {
                'map': 'office', 'null': False,
            },
            'Adm.naam': {
                'map': 'office_name', 'null': False,
            },
            'Jaar': {
                'map': 'year', 'type': int, 'null': False,
            },
            'Periode': {
                'map': 'period', 'type': int, 'null': False,
            },
            'Dagboek': {
                'map': 'journal', 'null': False,
            },
            'Dagboeknaam': {
                'map': 'journal_name', 'null': False,
            },
            'Boekingsnummer': {
                'map': 'booking_number', 'type': int, 'null': False,
            },
            'Status': {
                'map': 'booking_status', 'null': False,
            },
            'Boekdatum': {
                'map': 'booking_date', 'type': date_parser, 'null': False,
            },
            'Vervaldatum': {
                'map': 'expire_date', 'type': date_parser, 'null': True,
            },
            'Factuurnummer': {
                'map': 'invoice_number', 'null': True,
            },
            'Valuta': {
                'map': 'curcode', 'null': False,
            },
            'Grootboekrek.': {
                'map': 'ledger', 'type': int, 'null': False,
            },
            'Grootboekrek.naam': {
                'map': 'ledger_name', 'null': False,
            },
            'Kpl./rel.': {
                'map': 'cost_centre', 'type': int, 'null': False,
            },
            'Kpl.-/rel.naam': {
                'map': 'cost_centre_name', 'null': False,
            },
            'Bedrag': {
                'map': 'valuesigned', 'type': Decimal, 'null': False,
            },
            'Basisbedrag': {
                'map': 'base_valuesigned', 'type': Decimal, 'null': False,
            },
            'Rapportagebedrag': {
                'map': 'report_valuesigned', 'type': Decimal, 'null': True,
            },
            'Open amount transaction value': {
                'map': 'open_valuesigned', 'type': Decimal, 'null': True,
            },
            'Open amount base value': {
                'map': 'openbase_valuesigned', 'type': Decimal, 'null': True,
            },
            'Betaalstatus': {
                'map': 'payment_status', 'null': False,
            },
            'Betaaldatum': {
                'map': 'payment_date', 'type': date_parser, 'null': False,
            },
            'Afletternummer': {
                'map': 'affiliation_number', 'type': int, 'null': False,
            },
            'Betaalnummer': {
                'map': 'payment_number', 'null': True,
            },
            'Wijzigingsdatum': {
                'map': 'modification_date', 'type': date_parser, 'null': False,
            },
            'Vrij tekstveld 1': {
                'map': 'freetext1', 'null': True,
            },
            'Vrij tekstveld 2': {
                'map': 'freetext2', 'null': True,
            },
            'Vrij tekstveld 3': {
                'map': 'freetext3', 'null': True,
            },
        },
    },
    'transaction_summary': {
        'key_properties': 'id',
        'replication_method': 'INCREMENTAL',
        'replication_key': 'id',
        'bookmark': 'start_date',
        'mapping': {
            'id': {
                'map': 'id', 'null': False,
            },
            'Administratie': {
                'map': 'office', 'null': False,
            },
            'Adm.naam': {
                'map': 'office_name', 'null': False,
            },
            'Dagboek': {
                'map': 'journal', 'null': False,
            },
            'Jaar/periode (JJJJ/PP)': {
                'map': 'yearperiod', 'null': False,
            },
            'Aantal transacties': {
                'map': 'transaction_count', 'type': int, 'null': False,
            },
            'Aantal transactie regels': {
                'map': 'transaction_line_count', 'type': int, 'null': False,
            },
        },
    },
})
