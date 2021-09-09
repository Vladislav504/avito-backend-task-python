import pytest

from avito_task.exceptions import ServerError
from avito_task.server import handle_response


class MockResponse:
    status = None
    reason = None

    async def text(self):
        return "Test"


@pytest.mark.asyncio
async def test_server_error_handle():
    mock_response = MockResponse()
    mock_response.status = 500
    mock_response.reason = "Test"
    with pytest.raises(ServerError, match="Test"):
        await handle_response(mock_response)


@pytest.mark.asyncio
async def test_server_correct_response():
    mock_response = MockResponse()
    mock_response.status = 200
    text = await handle_response(mock_response)
    assert text == await mock_response.text()
