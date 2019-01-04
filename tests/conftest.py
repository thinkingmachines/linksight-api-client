# -*- coding: utf-8 -*-

# Import standard library
import os

# Import modules
import pytest
import responses
from dotenv import load_dotenv

# Import from package
import linksight
from linksight.common.settings import ENDPOINT
from linksight.common.utils import urljoin

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')


@pytest.fixture
def client():
    """Return a client"""
    return linksight.Client(API_TOKEN)


@pytest.fixture
def user_response():
    """Return the expected response for the user resource"""
    return {
        'username': 'thinkdatasci',
        'email': 'hello@thinkingmachin.es',
        'first_name': 'Thinking Machines',
        'last_name': 'Data Science',
    }


@pytest.fixture
def dataset_response():
    """Return the expected response for the dataset resource"""
    return {
        'id': '6937ce41-ab13-412a-f52e-7f5b435a6ed7',
        'file': 'https://storage.googleapis.com/linksight/datasets/test_areas_V8u4xEO.csv',  # NOQA
        'name': 'test_areas.csv',
        'is_internal': False,
        'created_at': '2018-12-29T13:34:24.257835+08:00',
        'uploader': 6,
    }


@pytest.fixture
def match_response(dataset_response):
    """Return the expected response for a match resource"""
    return {
        'id': 'f195903b-6c7d-4290-8320-ce5ce5af3b5c',
        'source_bgy_col': None,
        'source_municity_col': None,
        'source_prov_col': 'Province',
        'created_at': '2018-12-29T13:34:24.257835+08:00',
        'dataset': dataset_response,
        'matched_dataset': {
            'id': 'f2286737-87ec-4a16-8434-23b2620a548f',
            'file': 'https://storage.googleapis.com/linksight/datasets/test_areas-linksight_d7UH5fY.csv',  # NOQA
            'name': 'test_areas-linksight.csv',
            'is_internal': False,
            'created_at': '2018-12-29T13:36:56.493743+08:00',
            'uploader': None,
        },
    }


@pytest.fixture
def mock_api(user_response, dataset_response, match_response):
    """Return a mocked external API"""
    # Manage endpoints
    user_endpt = urljoin(ENDPOINT, 'users', 'me')
    dataset_endpt = urljoin(ENDPOINT, 'datasets')
    match_endpt = urljoin(
        ENDPOINT, 'datasets', dataset_response['id'], 'match'
    )
    with responses.RequestsMock(assert_all_requests_are_fired=False) as rsps:
        rsps.add(responses.GET, url=user_endpt, json=user_response)
        rsps.add(responses.POST, url=dataset_endpt, json=dataset_response)
        rsps.add(responses.POST, url=match_endpt, json=match_response)
        yield rsps


@pytest.fixture
def mock_api_server_error(dataset_response):
    """Return a mocked external API with 500 response"""
    # Manage endpoints
    dataset_endpt = urljoin(ENDPOINT, 'datasets')
    match_endpt = urljoin(
        ENDPOINT, 'datasets', dataset_response['id'], 'match'
    )
    with responses.RequestsMock(assert_all_requests_are_fired=False) as rsps:
        rsps.add(responses.POST, url=dataset_endpt, json=dataset_response)
        rsps.add(
            responses.POST,
            url=match_endpt,
            status=500,
            json={'error': 'Server Error (500)'},
        )
        yield rsps
