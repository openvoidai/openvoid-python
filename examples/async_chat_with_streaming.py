#!/usr/bin/env python

import asyncio
import os

from openvoid.async_client import OpenVoidAsyncClient
from openvoid.models.chat_completion import ChatMessage


async def main():
    api_key = os.environ["OPENVOID_API_KEY"]
    model = "prox"

    client = OpenVoidAsyncClient(api_key=api_key)

    print("Chat response:")
    response = client.chat_stream(
        model=model,
        messages=[ChatMessage(role="user", content="What is SQL Injection?")],
    )

    async for chunk in response:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")

    print("\n")

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
