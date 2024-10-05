"""Test helpers."""

import pytest

from tests.common import load_fixture


@pytest.fixture(scope="class")
def status_response():
    """Load status response."""
    return load_fixture("status_response.txt")


@pytest.fixture(scope="class")
def parsed_response():
    """Load parsed response."""
    return load_fixture("parsed_response.json")
