#!/usr/bin/env python

import asyncio
import os

from openvoid.async_client import OpenVoidAsyncClient
from openvoid.models.chat_completion import ChatMessage


async def main():
    api_key = os.environ["OPENVOID_API_KEY"]
    model = "prox"

    client = OpenVoidAsyncClient(api_key=api_key)

    chat_response = await client.chat(
        model=model,
        messages=[ChatMessage(role="user", content="What is SQL Injection?")],
    )

    print(chat_response.choices[0].message.content)

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
