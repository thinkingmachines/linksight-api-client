# -*- coding: utf-8 -*-

"""Tests all methods on Client"""

# Import standard library
import glob

# Import modules
import pytest
import pandas as pd

# Import from package
import linksight as ls


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


def test_client_create_dataset_from_df(mock_api, client, dataset_response):
    """Test if Client.create_dataset() works given a Dataframe input"""
    file = glob.glob('./**/test_areas.csv', recursive=True)
    df = pd.read_csv(file[0])
    resp = client.create_dataset(df)
    assert isinstance(resp, ls.resource.resources.Dataset)
    assert resp.keys() == dataset_response.keys()


@pytest.mark.webtest
def test_client_get_user_web(client):
    """Test if Client.get_user() returns the expected type"""
    resp = client.get_user()
    assert isinstance(resp, ls.resource.resources.User)


@pytest.mark.webtest
def test_client_create_dataset_web(client):
    """Test if Client.create_dataset() returns the expected value and type"""
    file = glob.glob('./**/test_areas.csv', recursive=True)
    with open(file[0], 'r') as fp:
        resp = client.create_dataset(fp)
    assert isinstance(resp, ls.resource.resources.Dataset)


@pytest.mark.webtest
def test_client_create_dataset_from_df_web(client):
    """Test if Client.create_dataset() works given a Dataframe input"""
    file = glob.glob('./**/test_areas.csv', recursive=True)
    df = pd.read_csv(file[0])
    resp = client.create_dataset(df)
    assert isinstance(resp, ls.resource.resources.Dataset)
