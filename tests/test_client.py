# -*- coding: utf-8 -*-

"""Tests all methods on Client"""

# Import standard library
import glob

# Import modules
import responses

# Import from package
import linksight as ls
from linksight.common.settings import ENDPOINT
from linksight.common.utils import urljoin


def test_client_get_user(mock_api, client, user_response):
    """Test if Client.get_user() returns the expected value and type"""
    resp = client.get_user()
    assert isinstance(resp, ls.resource.resources.User)
    assert resp.keys() == user_response.keys()


def test_client_create_dataset(mock_api, client, dataset_response):
    """Test if Client.create_dataset() returns the expected value and type"""
    file = glob.glob('./**/test_areas.csv', recursive=True)
    with open(file[0], 'r') as fp:
        resp = client.create_dataset(fp)
    assert isinstance(resp, ls.resource.resources.Dataset)
    assert resp.keys() == dataset_response.keys()
