"""Tools."""
# -*- coding: utf-8 -*-
from typing import Optional

import singer
from singer.catalog import CatalogEntry

from tap_twinfield.streams import STREAMS


def clear_currently_syncing(state: dict) -> dict:
    """Clear the currently syncing from the state.

    Arguments:
        state (dict) -- State file

    Returns:
        dict -- New state file
    """
    return state.pop('currently_syncing', None)


def get_stream_state(state: dict, tap_stream_id: str) -> dict:
    """Return the state of the stream.

    Arguments:
        state {dict} -- The state
        tap_stream_id {str} -- The id of the stream

    Returns:
        dict -- The state of the stream
    """
    return state.get(
        'bookmarks',
        {},
    ).get(tap_stream_id)


def get_bookmark_value(
    stream_name: str,
    row: dict,
) -> Optional[str]:
    """Retrieve bookmark value from record.

    Arguments:
        stream_name {str} -- Stream name
        row {dict} -- Record

    Returns:
        str -- Bookmark value
    """
    if stream_name in {
        'bank_transactions',
        'general_ledger_transactions',
        'transactions_to_be_matched',
    }:
        # YYYY-MM
        return row['yearperiod'].replace('/', '-')

    elif stream_name in {
        'general_ledger_details',
        'annual_report',
        'multicurrency',
        'suppliers',
    }:
        # YYYY-MM

        year: str = str(row['year'])
        period: str = str(row['period']).rjust(2, '0')
        return f'{year}-{period}'
    return None


def update_bookmark(
    stream: CatalogEntry,
    bookmark: Optional[str],
    state: dict,
) -> None:
    """Update the bookmark.

    Arguments:
        stream {CatalogEntry} -- Stream catalog
        bookmark {Optional[str]} -- Record
        state {dict} -- State
    """
    # Retrieve the value of the bookmark
    if bookmark:
        # Save the bookmark to the state
        singer.write_bookmark(
            state,
            stream.tap_stream_id,
            STREAMS[stream.tap_stream_id]['bookmark'],
            bookmark,
        )

    # Clear currently syncing
    clear_currently_syncing(state)

    # Write the bootmark
    singer.write_state(state)
