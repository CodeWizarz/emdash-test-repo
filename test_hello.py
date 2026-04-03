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


def test_hello_return_format():
    """Test that hello() returns properly formatted message with comma and exclamation"""
    result = hello()
    assert ', ' in result, "Message should contain comma followed by space"
    assert result.endswith('!'), "Message should end with exclamation mark"


def test_hello_exact_format():
    """Test exact format including punctuation and capitalization"""
    result = hello()
    assert result == 'Hello, World!', "Message must match exact format"
    assert result[0].isupper(), "First letter should be capitalized"
    assert 'World' in result and result[result.index('World')].isupper(), "World should be capitalized"


def test_hello_consistency():
    """Test that hello() returns the same value on multiple calls"""
    result1 = hello()
    result2 = hello()
    result3 = hello()
    assert result1 == result2 == result3, "hello() should return consistent values"


def test_hello_no_side_effects():
    """Test that calling hello() multiple times has no side effects"""
    initial = hello()
    for _ in range(10):
        result = hello()
        assert result == initial, "hello() should have no side effects"


def test_hello_return_type_not_bytes():
    """Test that hello() doesn't return bytes"""
    result = hello()
    assert not isinstance(result, bytes), "Result should be str, not bytes"


def test_hello_return_is_unicode():
    """Test that hello() returns unicode string"""
    result = hello()
    assert isinstance(result, str), "Result should be unicode string (str in Python 3)"
    # Verify it can be encoded to UTF-8
    try:
        result.encode('utf-8')
    except UnicodeEncodeError:
        pytest.fail("Result should be valid UTF-8")
