# -*- coding: utf-8 -*-

"""Tests all methods on Client

For tests involving mock-methods, we are mocking the methods of the Resource
being consumed. For example, in get_user(), we are mocking the resource
User.retrieve() then check if Client really returns the "retrieved" value.
"""

# Import standard library
from unittest.mock import patch
import glob

# Import from package
import linksight


@patch.object(linksight.client.User, 'retrieve')
def test_client_get_user_return_value(mock_user_retrieve, client):
    """Test if Client.get_user() returns the expected value"""
    # Mock return value
    user_info = {
        'username': 'mock-data',
        'email': 'email@mock.org',
        'first_name': 'mock',
        'last_name': 'data',
    }
    # Test proper
    mock_user_retrieve.return_value = user_info
    assert mock_user_retrieve() == client.get_user()


@patch.object(linksight.client.Dataset, 'create')
def test_client_create_dataset_return_value(mock_ds_create, client):
    """Test if Client.create_dataset() returns the expected value"""
    # Mock return value
    dataset = {'file': 'gs://mock-data/mock-output.csv'}
    mock_ds_create.return_value = dataset
    # Test proper
    test_data = glob.glob('./**/data/test_areas.csv', recursive=True)
    with open(test_data[0], 'r') as f:
        assert mock_ds_create() == client.create_dataset(f)
