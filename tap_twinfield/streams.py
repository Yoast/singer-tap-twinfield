"""Streams metadata."""
# -*- coding: utf-8 -*-

from types import MappingProxyType

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
                'map': 'yearperiod', 'type': date_parser, 'null': False,
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
            }
        },
    },
})
