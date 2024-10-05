"""Test aioblackbird24180.util."""

from aioblackbird24180.util import parse_response


def test_parse_response(status_response, parsed_response):
    """Test parse response."""
    test_parsed_response = parse_response(status_response)
    assert isinstance(parsed_response, dict)
    # compare dict
    assert test_parsed_response == parsed_response
