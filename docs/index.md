# paspybin

[![CI](https://github.com/kiraware/paspybin/workflows/ci/badge.svg)](https://github.com/kiraware/paspybin/actions/workflows/ci.yml)
[![CodeQL](https://github.com/kiraware/paspybin/workflows/codeql/badge.svg)](https://github.com/kiraware/paspybin/actions/workflows/codeql.yml)
[![Docs](https://readthedocs.org/projects/paspybin/badge/?version=latest)](https://paspybin.readthedocs.io/en/latest/?badge=latest)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Ruff](https://camo.githubusercontent.com/7f995d42c2de5a9eb8ced2df552a0813050d324427a3facabfcfa5f88cb11c59/68747470733a2f2f696d672e736869656c64732e696f2f656e64706f696e743f75726c3d68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f636861726c6965726d617273682f727566662f6d61696e2f6173736574732f62616467652f76312e6a736f6e)](https://github.com/astral-sh/ruff)
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