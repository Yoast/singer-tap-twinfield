"""Tools."""
# -*- coding: utf-8 -*-


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
