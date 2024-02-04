#!/usr/bin/env python

import os

from openvoid.client import OpenVoidClient
from openvoid.models.chat_completion import ChatMessage


def main():
    api_key = os.environ["OPENVOID_API_KEY"]
    model = "prox"

    client = OpenVoidClient(api_key=api_key)

    for chunk in client.chat_stream(
        model=model,
        messages=[ChatMessage(role="user", content="What is SQL Injection?")],
    ):
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")


if __name__ == "__main__":
    main()
