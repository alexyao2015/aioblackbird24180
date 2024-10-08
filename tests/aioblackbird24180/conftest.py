"""Test helpers."""

import pytest

from tests.common import load_fixture


@pytest.fixture(scope="class")
def http_request():
    """Load status response."""
    return load_fixture("http_request.txt")


@pytest.fixture(scope="class")
def http_response_body():
    """Load status response."""
    return load_fixture("http_response_body.txt")


@pytest.fixture(scope="class")
def http_response():
    """Load status response."""
    return load_fixture("http_response.txt")


@pytest.fixture(scope="class")
def parsed_response():
    """Load parsed response."""
    return load_fixture("parsed_response.json")
