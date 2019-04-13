import pytest

from app.utilities.base64_converter import convert_base62, convert_from_base62


def test_converts_some_numbers_correctly():
    """Test that some numbers are converted correctly"""
    
    res = convert_base62(0)
    assert res == '0'

    res = convert_base62(20)
    assert res == 'k'

    res = convert_base62(50)
    assert res == 'O'

    res = convert_base62(100)
    assert res == 'C1'

    res = convert_base62(150)
    assert res == 'q2'

    res = convert_base62(4000)
    assert res == 'w21'

    res = convert_base62(1000000)
    assert res == '29c4'


def test_convert_from_base62_string():
    """Test that some base62 strings are converted to integers correctly"""

    res = convert_from_base62('0')
    assert res == 0

    res = convert_from_base62('k')
    assert res == 20

    res = convert_from_base62('O')
    assert res == 50

    res = convert_from_base62('C1')
    assert res == 100

    res = convert_from_base62('q2')
    assert res == 150

    res = convert_from_base62('w21')
    assert res == 4000

    res = convert_from_base62('29c4')
    assert res == 1000000
