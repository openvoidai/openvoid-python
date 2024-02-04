import contextlib
import unittest.mock as mock

from typing import List

import orjson
from httpx import Response


@contextlib.contextmanager
def mock_stream_response(status_code: int, content: List[str]):
    response = mock.Mock(Response)
    response.status_code = status_code
    response.iter_lines.return_value = iter(content)
    yield response


@contextlib.asynccontextmanager
async def mock_async_stream_response(status_code: int, content: List[str]):
    response = mock.Mock(Response)
    response.status_code = status_code

    async def async_iter(content: List[str]):
        for line in content:
            yield line

    response.aiter_lines.return_value = async_iter(content)
    yield response

def mock_response(
    status_code: int, content: str, is_json: bool = True
) -> mock.MagicMock:
    response = mock.Mock(Response)
    response.status_code = status_code
    if is_json:
        response.json = mock.MagicMock()
        response.json.return_value = orjson.loads(content)
    response.text = content
    return response


def mock_list_models_response_payload() -> str:
    return orjson.dumps(
        {
            "object": "list",
            "data": [
                {
                    "id": "prox",
                    "object": "model",
                    "created": 1703186988,
                    "owned_by": "openvoid",
                    "root": None,
                    "parent": None,
                },
                {
                    "id": "lex",
                    "object": "model",
                    "created": 1703186988,
                    "owned_by": "openvoid",
                    "root": None,
                    "parent": None,
                }
            ],
        }
    )


def mock_chat_response_payload():
    return orjson.dumps(
        {
            "id": "cmpl-7920a9c17077436bb12a225d8ee24aa9",
            "object": "chat.completion",
            "created": 1703165682,
            "choices": [
                {
                    "finish_reason": "stop",
                    "message": {
                        "role": "assistant",
                        "content": "What is SQL Injection?",
                    },
                    "index": 0,
                }
            ],
            "model": "lex",
            "usage": {"prompt_tokens": 90, "total_tokens": 90, "completion_tokens": 0},
        }
    ).decode()


def mock_chat_response_streaming_payload():
    return [
        "data: "
        + orjson.dumps(
            {
                "id": "cmpl-8cd9019d21ba490aa6b9740f5d0a883e",
                "model": "lex",
                "choices": [
                    {
                        "index": 0,
                        "delta": {"role": "assistant"},
                        "finish_reason": None,
                    }
                ],
            }
        ).decode()
        + "\n\n",
        *[
            "data: "
            + orjson.dumps(
                {
                    "id": "cmpl-8cd9019d21ba490aa6b9740f5d0a883e",
                    "object": "chat.completion.chunk",
                    "created": 1703168544,
                    "model": "lex",
                    "choices": [
                        {
                            "index": i,
                            "delta": {"content": f"stream response {i}"},
                            "finish_reason": None,
                        }
                    ],
                }
            ).decode()
            + "\n\n"
            for i in range(10)
        ],
        "data: [DONE]\n\n",
    ]
