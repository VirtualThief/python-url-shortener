from unittest.mock import Mock, ANY
import pytest

from app.controllers.shortener_controller import ShortenerController


def test_post_url_should_save_url_with_random_id():
    """Test that URL is saved to DB with random ID"""

    url = 'https://google.com/'
    redisMock = Mock()
    
    controller = ShortenerController(redisMock)
    controller.post_url(url)

    redisMock.set.assert_called_once_with(ANY, url)


def test_redirect_reads_url_from_database():
    """Test that redirect reads URL from database"""
    
    short_url = 'abcdef'
    url = 'https://google.com/'
    redisMock = Mock()
    redisMock.get.return_value = url

    controller = ShortenerController(redisMock)
    controller.redirect(short_url)

    redisMock.get.assert_called_once_with(short_url)


def test_redirect_searches_for_stripped_value():
    """Test that short id is stripped before searching in database"""
    raise NotImplementedError


def test_redirect_redirects_to_url_if_short_link_exists():
    """Test that redirects to URL if it exists in database"""
    raise NotImplementedError


def test_redirect_returns_404_if_link_not_exists():
    """Test that 404 is returned if link doesn't exist in database"""
    raise NotImplementedError
