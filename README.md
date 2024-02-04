# OpenVoid Python Client

You can use the OpenVoid Python client to interact with the OpenVoid AI API.

## Installing

```bash
pip install openvoid
```

### From Source

This client uses `poetry` as a dependency and virtual environment manager.

You can install poetry with

```bash
pip install poetry
```

`poetry` will set up a virtual environment and install dependencies with the following command:

```bash
poetry install
```

## Run examples

You can run the examples in the `examples/` directory using `poetry run` or by entering the virtual environment using `poetry shell`.

### API Key Setup

Running the examples requires a OpenVoid AI API key.

1. Get your own OpenVoid API Key: <https://docs.openvoid.ai/#api-access>
2. Set your OpenVoid API Key as an environment variable. You only need to do this once.

```bash
# set OpenVoid API Key (using zsh for example)
$ echo 'export OPENVOID_API_KEY=[your_key_here]' >> ~/.zshenv

# reload the environment (or just quit and open a new terminal)
$ source ~/.zshenv
```

### Using poetry run

```bash
cd examples
poetry run python chat_no_streaming.py
```

### Using poetry shell

```bash
poetry shell
cd examples

>> python chat_no_streaming.py
```
