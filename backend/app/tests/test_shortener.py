import os
import tempfile

import pytest

from app import start


@pytest.fixture
def client():
    """Configure testing client"""
    start.app.config['TESTING'] = True
    client = start.app.test_client()

    yield client

def test_index_page_rendered(client):
    """Test that index page is rendered correctly"""
    rv = client.get('/')

    assert b'<input type="text" class="form-control" id="url" name="url" placeholder="https://somesite.com/"/>' in rv.data