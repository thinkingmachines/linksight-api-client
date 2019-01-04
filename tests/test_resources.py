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


def test_dataset_match_no_columns(mock_api, client):
    """Test if ValueError is raised whenever no column names are passed"""
    file = glob.glob('./**/test_areas.csv', recursive=True)
    with open(file[0], 'r') as fp:
        ds = client.create_dataset(fp)
    with pytest.raises(ValueError):
        ds.match()


def test_dataset_match_invalid_columns(mock_api_server_error, client):
    """Test if ValueError is raised given invalid column names (500)"""
    file = glob.glob('./**/test_areas.csv', recursive=True)
    with open(file[0], 'r') as fp:
        ds = client.create_dataset(fp)
    with pytest.raises(ValueError):
        ds.match(source_prov_col='Provence')  # Should be `Province`


@pytest.mark.webtest
def test_dataset_match_web(client):
    """Test if Dataset.match() returns the expected type"""
    file = glob.glob('./**/test_areas.csv', recursive=True)
    with open(file[0], 'r') as fp:
        ds = client.create_dataset(fp)
    resp = ds.match(source_prov_col='Province')
    assert isinstance(resp, ls.resource.resources.Match)


@pytest.mark.webtest
def test_dataset_match_no_columns_web(client):
    """Test if ValueError is raised whenever no column names are passed"""
    file = glob.glob('./**/test_areas.csv', recursive=True)
    with open(file[0], 'r') as fp:
        ds = client.create_dataset(fp)
    with pytest.raises(ValueError):
        ds.match()  # No column names


@pytest.mark.webtest
def test_dataset_match_invalid_columns_web(client):
    """Test if ValueError is raised given invalid column names (500)"""
    file = glob.glob('./**/test_areas.csv', recursive=True)
    with open(file[0], 'r') as fp:
        ds = client.create_dataset(fp)
    with pytest.raises(ValueError):
        ds.match(source_prov_col='Provence')  # Should be `Province`
