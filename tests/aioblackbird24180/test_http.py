"""Test aioblackbird24180.http."""

import pytest

from aioblackbird24180.http import __generate_request, __process_response


@pytest.mark.parametrize(
    ("request_params", "expected_request"),
    [
        (
            ("POST", "/cgi-bin/MUH44TP_getsetparams.cgi", "192.168.1.1", "lcc"),
            b"""POST /cgi-bin/MUH44TP_getsetparams.cgi HTTP/1.1
Host: 192.168.1.1
Accept: */*
Content-Length: 3

lcc""",
        ),
        (
            ("POST", "/cgi-bin/MMX32_Keyvalue.cgi", "localhost", "{CMD=OUT02:01."),
            b"""POST /cgi-bin/MMX32_Keyvalue.cgi HTTP/1.1
Host: localhost
Accept: */*
Content-Length: 14

{CMD=OUT02:01.""",
        ),
    ],
)
def test_generate_request(request_params, expected_request):
    """Test MatrixState."""
    assert __generate_request(*request_params) == expected_request


def test_process_response(http_response, http_response_body):
    """Test __process_response."""
    assert __process_response(http_response.encode()) == (200, http_response_body)
