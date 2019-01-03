# -*- coding: utf-8 -*-

"""Tests if the mock data in conftest is consistent with the live server

Our mock data lies on the assumption that the responses will be the same as
with the external API. However, LinkSight's response may change throughout its
development cycle. This set of tests simply checks for consistency
"""

# Import standard library
import glob

# Import modules
import pytest


@pytest.mark.contract
@pytest.mark.webtest
def test_user_responsse(user_response, client):
    """Test contract for user response"""
    resp = client.get_user()
    assert resp.keys() == user_response.keys()


@pytest.mark.contract
@pytest.mark.webtest
def test_dataset_response(dataset_response, client):
    """Test contract for dataset response"""
    file = glob.glob('./**/test_areas.csv', recursive=True)
    with open(file[0], 'r') as fp:
        resp = client.create_dataset(fp)
    assert resp.keys() == dataset_response.keys()


@pytest.mark.contract
@pytest.mark.webtest
def test_match_response(match_response, client):
    """Test contract for match response"""
    file = glob.glob('./**/test_areas.csv', recursive=True)
    with open(file[0], 'r') as fp:
        ds = client.create_dataset(fp)
    resp = ds.match(source_prov_col='Province')
    assert resp.keys() == match_response.keys()
