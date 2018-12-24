# -*- coding: utf-8 -*-

# Import standard library
import os

# Import modules
import pytest

# Import from package
import linksight

API_TOKEN = os.getenv('API_TOKEN')


@pytest.fixture
def client():
    """Return a client"""
    return linksight.Client(API_TOKEN)
