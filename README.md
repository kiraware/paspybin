# paspybin

[![Test](https://github.com/kiraware/paspybin/workflows/Test/badge.svg)](https://github.com/kiraware/paspybin/actions/workflows/test.yml)
[![CodeQL](https://github.com/kiraware/paspybin/workflows/CodeQL/badge.svg)](https://github.com/kiraware/paspybin/actions/workflows/codeql.yml)
[![Docs](https://readthedocs.org/projects/paspybin/badge/?version=latest)](https://paspybin.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/kiraware/paspybin/graph/badge.svg?token=PH6EUFT4V0)](https://codecov.io/gh/kiraware/paspybin)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![pypi](https://img.shields.io/pypi/v/paspybin.svg)](https://pypi.org/project/paspybin/)
[![python](https://img.shields.io/pypi/pyversions/paspybin.svg)](https://pypi.org/project/paspybin/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/license/MIT/)

`paspybin` is an asynchronous API wrapper for the
[Pastebin API](https://pastebin.com/doc_api), designed to streamline
interaction with Pastebin's services in Python. It enables users to
leverage Pastebin's functionality asynchronously, enhancing performance
and usability.

## Key Features

- **Asynchronous Operations:** Utilizes `asyncio` and `aiohttp` for efficient API requests.
- **Data Schema:** Built with Python's `dataclass` for clear and structured data representation.
- **Comprehensive Documentation:** Explore detailed [documentation](https://paspybin.readthedocs.io/en/latest/) for seamless integration and usage.

## Installation

```bash
pip install paspybin
```

## Usage

```python
import asyncio
import os

from paspybin import Paspybin

PASTEBIN_API_DEV_KEY = os.environ["PASTEBIN_API_DEV_KEY"]
PASTEBIN_USERNAME = os.environ["PASTEBIN_USERNAME"]
PASTEBIN_PASSWORD = os.environ["PASTEBIN_PASSWORD"]

async def main():
    async with Paspybin(PASTEBIN_API_DEV_KEY) as paspybin:
        await paspybin.login(PASTEBIN_USERNAME, PASTEBIN_PASSWORD)
        async for paste in paspybin.pastes.get_all():
            print(paste)

asyncio.run(main())
```

## Docs

You can start reading the documentation [here](https://paspybin.readthedocs.io/en/latest/).

## Contributing

We welcome contributions to enhance paspybin! Please review our
[contributing guidelines](https://paspybin.readthedocs.io/en/latest/how-to-guides/#contributing).
before getting started.

## Acknowledgements

We would like to thank [Pastebin](https://pastebin.com/)
for providing API services and also good documentation for
using the API.
