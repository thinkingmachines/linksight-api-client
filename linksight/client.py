# -*- coding: utf-8 -*-

# Import modules
import requests

from .common.settings import USER_AGENT
from .resource.resources import Dataset, User


class Client(requests.Session):
    """An object for handling all requests"""

    def __init__(self, token):
        """Initialize the class

        Parameters
        ----------
        token : string
            API token
        """
        super().__init__()
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
        dict
        """
        return User.retrieve(self, id)

    def create_dataset(self, file):
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
        file : _io.TextIOWrapper
            A file handler

        Returns
        -------
        dict
        """
        return Dataset.create(self, files={'file': file})
