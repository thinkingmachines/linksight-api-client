# -*- coding: utf-8 -*-

# Import standard library
import logging

# Import from package
import coloredlogs

from ..common.settings import ENDPOINT
from ..common.utils import urljoin

# Create a logger
logger = logging.getLogger(__name__)
coloredlogs.install(level=logging.INFO, logger=logger)


class Resource(dict):
    """Base Resource class"""

    @classmethod
    def create(cls, client, **kwargs):
        """Create a POST request to LinkSight endpoint

        Parameters
        ----------
        client : requests.Session
            An instance of the client

        Returns
        -------
        dict
            An instance of itself with the appropriate response
        """
        url = urljoin(ENDPOINT, cls.url)
        resp = client.request('post', url, **kwargs)
        resp.raise_for_status()
        return cls(client, resp)

    @classmethod
    def retrieve(cls, client, id):
        """Create a GET request to LinkSight endpoint

        Parameters
        ----------
        client : requests.Session
            An instance of the client
        id : string
            ID of the user

        Returns
        -------
        dict
            An instance of itself with the appropriate response
        """
        url = urljoin(ENDPOINT, cls.url, id)
        resp = client.request('get', url)
        resp.raise_for_status()
        return cls(client, resp)

    def __init__(self, client, resp):
        super().__init__(resp.json())
        self.client = client
        self.response = resp

    def create_instance_url(self, *args):
        """Create the instance url to pass the request onto

        Parameters
        ----------
        args : strings

        Returns
        -------
        string
            The instance url
        """
        return urljoin(ENDPOINT, self.url, self['id'], *args)
