# -*- coding: utf-8 -*-

"""Global-wide constants for package settings

This file contains various constants that are used to configure package
interaction with the LinkSight API. These constants include:

    - :code:`VERSION`: The LinkSight version it interacts upon.
    - :code:`USER_AGENT`: The URL for the user agent proxy.
    - :code:`ENDPOINT`: The base URL for interacting with the API.
"""

VERSION = '0.1'
USER_AGENT = 'linksight-api-client/{}'.format(VERSION)
ENDPOINT = 'https://linksight-stg.thinkingmachin.es/api'
