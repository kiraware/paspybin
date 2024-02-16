# paspybin

[![CI](https://github.com/kiraware/paspybin/workflows/ci/badge.svg)](https://github.com/kiraware/paspybin/actions/workflows/ci.yml)
[![CodeQL](https://github.com/kiraware/paspybin/workflows/codeql/badge.svg)](https://github.com/kiraware/paspybin/actions/workflows/codeql.yml)
[![Docs](https://readthedocs.org/projects/paspybin/badge/?version=latest)](https://paspybin.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/kiraware/paspybin/graph/badge.svg?token=PH6EUFT4V0)](https://codecov.io/gh/kiraware/paspybin)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![pypi](https://img.shields.io/pypi/v/paspybin.svg)](https://pypi.org/project/paspybin/)
[![python](https://img.shields.io/pypi/pyversions/paspybin.svg)](https://pypi.org/project/paspybin/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/license/mit/)

The `paspybin` project is an asynchronous api wrapper
written in Python for [Pastebin API](https://pastebin.com/doc_api).
paspybin was created to make it easier for users to use the API
provided by Pastebin asynchronously.

We use the third party library [aiohttp](https://docs.aiohttp.org/en/stable/)
for asynchronous client requests and it has been tested
to work well using the [asyncio](https://docs.python.org/3/library/asyncio.html)
library. Also it use [dataclass](https://docs.python.org/3/library/dataclasses.html)
as the schema.

## Table Of Contents

You can start reading the documentation with the
following links:

1. [Tutorials](tutorials.md)
2. [How-To Guides](how-to-guides.md)
3. [Reference](reference/api.md)

## Acknowledgements

We would like to thank [Pastebin](https://pastebin.com/)
for providing API services and also good documentation for
using the API.
