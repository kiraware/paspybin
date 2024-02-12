# Tutorial

## Getting Started

Let's install paspybin first if it is not already installed
using the following command. Make sure Python is installed
on your computer.

```properties
pip install paspybin
```

All done!

## Pastes API

There are three APIs available for pastes
namely get_all, get_content, and create_paste.

### get_all

get_all is used to get all pastes. Read get_all
[reference](reference/api.md/#paspybin.api.Pastes.get_all)
for more details.

Code example:

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

Example output:

```console
Paste(key='gS5N2xdg', date=datetime.datetime(2024, 1, 26, 16, 32, 22), title='NONE', size=4, expire_date=datetime.datetime(1970, 1, 1, 8, 0), private=<Visibility.PUBLIC: 0>, format=<Format.NONE: 'text'>, url='https://pastebin.com/gS5N2xdg', hits=3)
...
```

### get_content

get_content is used to get the paste content based on
the given paste_key. This method should be used when
you want to get pasted content belonging to other people
that is public or unlisted or get pasted content without
logging in, aka guest mode. Read get_content
[reference](reference/api.md/#paspybin.api.Pastes.get_content)
for more details.

Code example:

```python
import asyncio

from paspybin import Paspybin


async def main():
    async with Paspybin() as paspybin:
        paste_key = "0C343n0d"
        paste_content = await paspybin.pastes.get_content(paste_key)
        print(paste_content)


asyncio.run(main())
```

Example output:

```console
Hi, and welcome to Pastebin.
...
```

### create_paste

create_paste is used to create pastes for both guests and
logged in users. Read create_paste
[reference](reference/api.md/#paspybin.api.Pastes.create_paste)
for more details.

Code example:

```python
import asyncio
import os

from paspybin import Paspybin

PASTEBIN_API_DEV_KEY = os.environ["PASTEBIN_API_DEV_KEY"]


async def main():
    async with Paspybin(PASTEBIN_API_DEV_KEY) as paspybin:
        # await paspybin.login(PASTEBIN_USERNAME, PASTEBIN_PASSWORD)
        paste_content = "some paste content"
        await paspybin.pastes.create_paste(paste_content)


asyncio.run(main())
```

## Paste API

Paste API is part of the Pastes API. There are two
methods available, namely get_content and delete.

### get_content

get_content is used to get the content of paste.
Read get_content
[reference](reference/api.md/#paspybin.api.Paste.get_content)
for more details.

Code example:

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
            paste_content = await paste.get_content()
            print(paste_content)


asyncio.run(main())
```

Example output:

```console
Just some paste content here
```

### delete

delete is used to delete paste. Read delete
[reference](reference/api.md/#paspybin.api.Paste.delete)
for more details.

Code example:

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
            paste.delete()


asyncio.run(main())
```

## User API

There is only one API available for user namely get_detail.

### get_detail

get_detail is used to get user details from the account
that is currently logged in. Read get_detail
[reference](reference/api.md/#paspybin.api.User.get_detail)
for more details.

Code example:

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
        user_detail = await paspybin.user.get_detail()
        print(user_detail)


asyncio.run(main())
```

Example output:

```console
User(name='paspybin', format=<Format.NONE: 'text'>, expiration=<Expire.NEVER: 'N'>, avatar_url='@themes/img/guest.png', private=<Visibility.PUBLIC: 0>, website=None, email='paspybin@email.com', location=None, account_type=<Type.NORMAL: 0>)
```
