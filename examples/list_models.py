#!/usr/bin/env python

import os

from openvoid.client import OpenVoidClient


def main():
    api_key = os.environ["OPENVOID_API_KEY"]

    client = OpenVoidClient(api_key=api_key)

    list_models_response = client.list_models()
    print(list_models_response)


if __name__ == "__main__":
    main()
