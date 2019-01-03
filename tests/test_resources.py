# -*- coding: utf-8 -*-

"""Tests all methods on Client"""

# Import standard library
import glob

# Import modules
import pytest

# Import from package
import linksight as ls


def test_dataset_match(mock_api, client, match_response):
    """Test if Dataset.match() returns the expected value and type"""
    file = glob.glob('./**/test_areas.csv', recursive=True)
    with open(file[0], 'r') as fp:
        ds = client.create_dataset(fp)
    resp = ds.match(source_prov_col='Province')
    assert isinstance(resp, ls.resource.resources.Match)
    assert resp.keys() == match_response.keys()


@pytest.mark.webtest
def test_dataset_match_web(client):
    """Test if Dataset.match() returns the expected type"""
    file = glob.glob('./**/test_areas.csv', recursive=True)
    with open(file[0], 'r') as fp:
        ds = client.create_dataset(fp)
    resp = ds.match(source_prov_col='Province')
    assert isinstance(resp, ls.resource.resources.Match)
