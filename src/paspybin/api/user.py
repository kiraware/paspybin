from .. import schemas
from ..exceptions import PaspybinBadAPIRequestError
from ..parsers import parse_user
from .api import API

__all__ = ["User"]


class User(API):
    async def get_detail(self) -> schemas.User:
        """
        Get a user detail.

        Returns:
            A `User` schema.

        Raises:
            PaspybinBadAPIRequestError: if a bad request is sent to the API.
            ValueError: if dev_key not supplied.
            ValueError: if guest use this method.

        Examples:
            >>> import asyncio
            >>> import os
            >>> from paspybin import Paspybin
            >>> PASTEBIN_API_DEV_KEY = os.environ["PASTEBIN_API_DEV_KEY"]
            >>> PASTEBIN_API_USER_KEY = os.environ["PASTEBIN_API_USER_KEY"]
            >>> async def main():
            ...     async with Paspybin(
            ...         PASTEBIN_API_DEV_KEY, PASTEBIN_API_USER_KEY
            ...     ) as paspybin:
            ...         print(await paspybin.user.get_detail())
            >>> asyncio.run(main())
            User(...)
        """
        if self._dev_key is None:
            raise ValueError("dev_key is required to use this method")

        if not self.is_authenticated():
            raise ValueError("only logged in users can use this method")

        payload = {
            "api_dev_key": self._dev_key,
            "api_option": "userdetails",
            "api_user_key": self._user_key,
        }

        async with self._session.post(self.api_post_url, data=payload) as response:
            data = await response.text()

            if not response.ok:
                raise PaspybinBadAPIRequestError(data)
            else:
                return parse_user(data)
