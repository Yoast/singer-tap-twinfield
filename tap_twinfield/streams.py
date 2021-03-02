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
            }
        },
    },
})
