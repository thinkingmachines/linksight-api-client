# -*- coding: utf-8 -*-

"""Contains various resources for API calls"""

# Import standard library
import logging

# Import from package
import coloredlogs
import pandas as pd

from ..resource.base import Resource

# Create a logger
logger = logging.getLogger(__name__)
coloredlogs.install(level=logging.INFO, logger=logger)


class User(Resource):
    """Resource for handling user-related API calls"""

    url = 'users'


class Match(Resource):
    """Resource for handling resulting dataset matches"""

    url = 'matches'

    def __init__(self, client, resp):
        super().__init__(client, resp)
        self.df = pd.read_csv(self['matched_dataset']['file'])


class Dataset(Resource):
    """Resource for handling dataset-related API calls"""

    url = 'datasets'

    def match(
        self,
        source_bgy_col=None,
        source_municity_col=None,
        source_prov_col=None,
        export=True,
    ):
        """Perform a match using the LinkSight API

        Parameters
        ----------
        source_bgy_col : string
            Column name for the barangays
        source_municity_col : string
            Column name for the municipality
        source_prov_col : string
            Column name for the province
        export : bool
            Export the resulting match (default is True)

        Returns
        -------
        linksight.resource.resources.Match
            The API response containing the match
        """
        if not any([source_bgy_col, source_municity_col, source_prov_col]):
            msg = 'At least one column must be defined!'
            logger.error(msg)
            raise ValueError(msg)
        url = self.create_instance_url('match')
        json_request = {
            'source_bgy_col': source_bgy_col,
            'source_municity_col': source_municity_col,
            'source_prov_col': source_prov_col,
            'export': export,
        }
        resp = self.client.request('post', url, json=json_request)
        return Match(self.client, resp)
