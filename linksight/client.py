# -*- coding: utf-8 -*-

"""
The Client module serves as the entrypoint for all our interactions with the
external LinkSight API. The main usage pattern requires us to instantiate a
client, then use that to handle all requests to LinkSight.

Most of the return values are in the form of a :mod:`linksight.resource`, which
inherits a dictionary type.

.. note::

    Needless to say, interacting with the LinkSight API requires an internet
    connection.
"""

# Import standard library
import logging
import tempfile

# Import modules
import coloredlogs
import requests
import pandas as pd

from .common.settings import USER_AGENT
from .resource import Dataset, User


class Client(requests.Session):
    """An object for handling all requests"""

    def __init__(self, token):
        """Initialize the class

        Parameters
        ----------
        token : str
            API token
        """
        super().__init__()
        self.logger = logging.getLogger(__name__)
        coloredlogs.install(level=logging.INFO, logger=self.logger)
        self.headers.update(
            {
                'User-Agent': USER_AGENT,
                'Authorization': 'Token {}'.format(token),
            }
        )

    def get_user(self, id='me'):
        """Get the user creating the request

        Parameters
        ----------
        id : str
            User ID initiating the request

        Returns
        -------
        linksight.resource.resources.User
            The user information retrieved from the API
        """
        self.logger.debug('Retrieving user information...')
        return User.retrieve(self, id)

    def create_dataset(self, data):
        """Create a dataset from a given file

        In order to create a dataset, simply create a context
        from the given CSV file and pass it to this method:

        .. code-block:: python

            from linksight import Client

            API_TOKEN = <Insert your API_TOKEN here>

            ls = Client(API_TOKEN)
            with open('path/to/query/file.csv') as f:
                dataset = ls.create_dataset(f)

        Parameters
        ----------
        data : _io.TextIOWrapper or pandas.DataFrame
            A file handler or a pandas DataFrame

        Returns
        -------
        linksight.resource.resources.Dataset
            The Dataset resource that can be used for matching
        """
        self.logger.debug('Creating dataset...')
        if isinstance(data, pd.DataFrame):
            self.logger.debug('Detected DataFrame, generating tempfile...')
            with tempfile.NamedTemporaryFile(delete=False) as temp:
                filename = '{}.csv'.format(temp.name)  # tempfile is csv
                data.to_csv(filename, index=False)
                with open(filename) as fp:
                    dataset = Dataset.create(self, files={'file': fp})
        else:
            dataset = Dataset.create(self, files={'file': data})
        return dataset
