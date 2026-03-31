"""Tests for hello endpoint."""
import pytest
from hello import hello


def test_hello_returns_dict():
    """Test that hello returns a dictionary."""
    result = hello()
    assert isinstance(result, dict)


def test_hello_has_message():
    """Test that hello returns a message field."""
    result = hello()
    assert 'message' in result
    assert result['message'] == 'Hello, World!'


def test_hello_has_description():
    """Test that hello returns a description field."""
    result = hello()
    assert 'description' in result
    assert isinstance(result['description'], str)
    assert len(result['description']) > 0


def test_hello_description_content():
    """Test that description contains meaningful content."""
    result = hello()
    description = result['description'].lower()
    # Verify description is informative
    assert len(description) > 10, "Description should be more than trivial"
