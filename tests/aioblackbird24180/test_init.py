"""Test aioblackbird24180.init."""

from unittest.mock import patch

from aiohttp.http_exceptions import BadHttpMessage
import pytest

from aioblackbird24180 import Blackbird24180, MatrixState


def test_matrix_state():
    """Test MatrixState."""
    state = MatrixState()
    state.set_output_input(1, 1)
    state.set_output_input(2, 1)
    state.set_output_input(3, 2)
    assert state.get_input(1) == [1, 2]
    assert state.get_input(2) == [3]
    assert state.get_output(1) == 1
    assert state.get_output(2) == 1
    assert state.get_output(3) == 2


async def test_blackbird24180_status(status_response):
    """Test Blackbird24180 status."""
    blackbird = Blackbird24180("http://localhost")

    with patch.object(blackbird, "_Blackbird24180__post", return_value=status_response):
        state = await blackbird.get_matrix()
    assert state.get_input(1) == [1, 3, 4, 5, 6, 7, 8]
    assert state.get_output(1) == 1
    assert state.get_output(2) == 2


@pytest.mark.parametrize(
    ("output_input", "expected_post"),
    [
        ((2, 1), "{CMD=OUT02:01."),
        ((3, 2), "{CMD=OUT03:02."),
    ],
)
async def test_blackbird24180_set_output(
    output_input: tuple[int, int], expected_post: str
):
    """Test Blackbird24180 changing input."""
    blackbird = Blackbird24180("http://localhost")

    # The response from this post request will raise a BadHttpMessage exception.
    # We need to make sure that this exception is always caught and does not error.
    with patch.object(
        blackbird, "_Blackbird24180__post", side_effect=BadHttpMessage("test")
    ) as mocked_post:
        await blackbird.set_output(output_input[0], output_input[1])
        mocked_post.assert_called_with("cgi-bin/MMX32_Keyvalue.cgi", expected_post)
