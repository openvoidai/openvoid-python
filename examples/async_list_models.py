#!/usr/bin/env python

import asyncio
import os

from openvoid.async_client import OpenVoidAsyncClient


async def main():
    api_key = os.environ["OPENVOID_API_KEY"]

    client = OpenVoidAsyncClient(api_key=api_key)

    list_models_response = await client.list_models()
    print(list_models_response)


if __name__ == "__main__":
    asyncio.run(main())
