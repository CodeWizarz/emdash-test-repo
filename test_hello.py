import pytest
from hello import hello


def test_hello_returns_string():
    """Test that hello() returns a string"""
    result = hello()
    assert isinstance(result, str)


def test_hello_returns_correct_message():
    """Test that hello() returns the correct greeting"""
    result = hello()
    assert result == 'Hello, World!'


def test_hello_not_empty():
    """Test that hello() doesn't return an empty string"""
    result = hello()
    assert len(result) > 0


def test_hello_contains_hello():
    """Test that the message contains 'Hello'"""
    result = hello()
    assert 'Hello' in result


def test_hello_contains_world():
    """Test that the message contains 'World'"""
    result = hello()
    assert 'World' in result


def test_hello_no_parameters():
    """Test that hello() can be called without parameters"""
    try:
        hello()
    except TypeError:
        pytest.fail("hello() should not require parameters")
