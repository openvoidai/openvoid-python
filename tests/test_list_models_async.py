import unittest.mock as mock

import pytest
from openvoid.async_client import OpenVoidAsyncClient
from openvoid.models.models import ModelList

from .utils import mock_list_models_response_payload, mock_response


@pytest.fixture()
def client():
    client = OpenVoidAsyncClient()
    client._client = mock.AsyncMock()
    return client


class TestAsyncListModels:
    @pytest.mark.asyncio
    async def test_list_models(self, client):
        client._client.request.return_value = mock_response(
            200,
            mock_list_models_response_payload(),
        )

        result = await client.list_models()

        client._client.request.assert_awaited_once_with(
            "get",
            "https://api.openvoid.ai/v1/models",
            headers={
                "User-Agent": f"openvoid-client-python/{client._version}",
                "Accept": "application/json",
                "Authorization": "Bearer None",
                "Content-Type": "application/json",
            },
            json={},
        )

        assert isinstance(result, ModelList), "Should return an ModelList"
        assert len(result.data) == 2
        assert result.object == "list"
