# Tutorial

## Getting Started

Let's install paspybin first if it is not already installed
using the following command. Make sure Python is installed
on your computer.

```properties
pip install paspybin
```

All done!

## Paspybin API

There are two APIs available for paspybin
namely login and logout.

### login

login is used to get user_key from Pastebin API and
authenticate all the paspybin interface. Use this method
to authenticate paspybin interface. Read login
[reference](reference/api.md/#paspybin.api.Paspybin.login)
for more details.

!!! tip
    Because Pastebin API has API rate limiting, and Pastebin stated
    !!! quote
        Only one key can be active at the same time for the same user.
        This key does not expire, unless a new one is generated.
    Hence it's better to store the user_key somewhere so that you
    can use it multiple times to avoid API rate limiting caused by
    login called multiple times.

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
        # Save the Pastebin user_key somewhere else
        print(paspybin._user_key)


asyncio.run(main())
```

Example output:

```console
r4nd0m5tr1n9u53rk3y
```

### logout

logout is used to deauthenticate all the paspybin interface.
This method usefull if you already authenticate paspybin with
provided user_key or by calling login method to become guest
user. This method is not calling Pastebin API. Read logout
[reference](reference/api.md/#paspybin.api.Paspybin.login)
for more details.

Code example:

```python
...
paspybin.logout()
```

## Pastes API

There are three APIs available for pastes
namely get_all, get_content, and create_paste.

### get_all

get_all is used to get all pastes. Use this method
to get a list of pastes owned by a user. Therefore,
to use this method you are required to log in or
just used the user_key you already has. Read get_all
[reference](reference/api.md/#paspybin.api.Pastes.get_all)
for more details.

Code example:

```python
import asyncio
import os

from paspybin import Paspybin

PASTEBIN_API_DEV_KEY = os.environ["PASTEBIN_API_DEV_KEY"]
PASTEBIN_API_USER_KEY = os.environ["PASTEBIN_API_USER_KEY"]


async def main():
    async with Paspybin(PASTEBIN_API_DEV_KEY, PASTEBIN_API_USER_KEY) as paspybin:
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
logging in, aka guest mode. To use this method, you
don't need a dev_key. Read get_content
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
# PASTEBIN_API_USER_KEY = os.environ["PASTEBIN_API_USER_KEY"]


async def main():
    # async with Paspybin(PASTEBIN_API_DEV_KEY, PASTEBIN_API_USER_KEY) as paspybin:
    async with Paspybin(PASTEBIN_API_DEV_KEY) as paspybin:
        paste_content = "some paste content"
        await paspybin.pastes.create_paste(paste_content)


asyncio.run(main())
```

When making a paste, you can determine many things related
to the paste. Such as paste title, paste format or syntax
highlighting, paste exposure or visibility, when the paste
expires, and where to save the paste to which folder with
folder_key.

paste title is just a string in general, you can give the
paste title with the `title` parameter.

```python
await paspybin.pastes.create_paste("hello content", "Nice Title")
```

Then to determine format or syntax highlighting, paste
exposure or visibility, and when a paste expires, we provide
an enum class that can be easily used. All three have
parameters `format`, `visibility`, and `expire`.

```python
from paspybin.enums import Expire, Format, Visibility
...
await paspybin.pastes.create_paste(
    "hello content",
    format=Format.NONE,
    visibility=Visibility.PUBLIC,
    expire=Expire.NEVER,
)
```

The code example above also shows the default values ​for
the three parameters provided by the Pastebin API if
these parameters are not provided.

And the last one is the `folder_key` parameter. We don't
know the correct way to get the folder key because there
is no documentation on how to get it. However, if you want
to paste it and put it in a folder owned by the user, you
can provide the folder key to the `folder_key` parameter
and of course you have to log in first.

```python
await paspybin.pastes.create_paste("hello content", folder_key="folder key here")
```

## Paste API

Paste API is part of the [Pastes API](reference/api.md/#paspybin.api.Pastes).
There are two methods available, namely get_content
and delete. All methods in the Paste API require you
to log in and of course to get the Paste API via the
Pastes API in the [get_all](reference/api.md/#paspybin.api.Pastes.get_all)
method which has been checked first to see if the user
has logged in so you can be sure that the user using
the Paste API is logged in.

### get_content

get_content is used to get the content of
paste owned by a user. Read get_content
[reference](reference/api.md/#paspybin.api.Paste.get_content)
for more details.

Code example:

```python
import asyncio
import os

from paspybin import Paspybin

PASTEBIN_API_DEV_KEY = os.environ["PASTEBIN_API_DEV_KEY"]
PASTEBIN_API_USER_KEY = os.environ["PASTEBIN_API_USER_KEY"]


async def main():
    async with Paspybin(PASTEBIN_API_DEV_KEY, PASTEBIN_API_USER_KEY) as paspybin:
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

delete is used to delete paste owned by a user.
Read delete
[reference](reference/api.md/#paspybin.api.Paste.delete)
for more details.

Code example:

!!! warning
    This code will delete all your pastes!

```python
import asyncio
import os

from paspybin import Paspybin

PASTEBIN_API_DEV_KEY = os.environ["PASTEBIN_API_DEV_KEY"]
PASTEBIN_API_USER_KEY = os.environ["PASTEBIN_API_USER_KEY"]


async def main():
    async with Paspybin(PASTEBIN_API_DEV_KEY, PASTEBIN_API_USER_KEY) as paspybin:
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
PASTEBIN_API_USER_KEY = os.environ["PASTEBIN_API_USER_KEY"]


async def main():
    async with Paspybin(PASTEBIN_API_DEV_KEY, PASTEBIN_API_USER_KEY) as paspybin:
        user_detail = await paspybin.user.get_detail()
        print(user_detail)


asyncio.run(main())
```

Example output:

```console
User(name='paspybin', format=<Format.NONE: 'text'>, expiration=<Expire.NEVER: 'N'>, avatar_url='@themes/img/guest.png', private=<Visibility.PUBLIC: 0>, website=None, email='paspybin@email.com', location=None, account_type=<Type.NORMAL: 0>)
```
