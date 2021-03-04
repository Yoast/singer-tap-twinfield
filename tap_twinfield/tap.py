"""Adyen tap."""
# -*- coding: utf-8 -*-
import logging
from argparse import Namespace

import pkg_resources
from singer import get_logger, utils
from singer.catalog import Catalog

from tap_twinfield.discover import discover
from tap_twinfield.sync import sync
from tap_twinfield.twinfield import Twinfield

VERSION: str = pkg_resources.get_distribution('tap-adyen').version
LOGGER: logging.RootLogger = get_logger()
REQUIRED_CONFIG_KEYS: tuple = (
    'username',
    'password',
    'organisation',
    'office',
)


@utils.handle_top_exception(LOGGER)
def main() -> None:
    """Run tap."""
    # Parse command line arguments
    args: Namespace = utils.parse_args(REQUIRED_CONFIG_KEYS)

    LOGGER.info(f'>>> Running tap-twinfield v{VERSION}')

    # If discover flag was passed, run discovery mode and dump output to stdout
    if args.discover:
        catalog: Catalog = discover()
        catalog.dump()
        return

    # Otherwise run in sync mode
    if args.catalog:
        # Load command line catalog
        catalog = args.catalog
    else:
        # Loadt the  catalog
        catalog = discover()

    # Initialize Twinfield client
    twinfield: Twinfield = Twinfield(
        args.config['username'],
        args.config['password'],
        args.config['organisation'],
        args.config['office'],
    )

    sync(twinfield, args.state, catalog, args.config['start_date'])


if __name__ == '__main__':
    main()
