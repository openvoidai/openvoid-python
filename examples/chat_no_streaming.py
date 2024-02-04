#!/usr/bin/env python

import os

from openvoid.client import OpenVoidClient
from openvoid.models.chat_completion import ChatMessage


def main():
    api_key = os.environ["OPENVOID_API_KEY"]
    model = "prox"

    client = OpenVoidClient(api_key=api_key)

    chat_response = client.chat(
        model=model,
        messages=[ChatMessage(role="user", content="What is SQL Injection?")],
    )
    print(chat_response.choices[0].message.content)


if __name__ == "__main__":
    main()
