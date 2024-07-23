from datetime import datetime

from aiohttp import ClientSession

from .. import schemas
from ..enums import Format, Visibility
from ..exceptions import PaspybinBadAPIRequestError
from ..types import DevKey, PastebinUrl, PasteKey, UserKey
from .api import API

__all__ = ["Paste"]


class Paste(API, schemas.Paste):
    """
    Paste API wrapper.
    """

    def __init__(
        self,
        key: PasteKey,
        date: datetime | None = None,
        title: str | None = None,
        size: int | None = None,
        expire_date: datetime | None = None,
        private: Visibility | None = None,
        format: Format | None = None,
        url: PastebinUrl | None = None,
        hits: int | None = None,
        dev_key: DevKey | None = None,
        user_key: UserKey | None = None,
        session: ClientSession | None = None,
    ) -> None:
        API.__init__(self, dev_key, user_key, session)
        schemas.Paste.__init__(
            self, key, date, title, size, expire_date, private, format, url, hits
        )

    async def delete(self) -> None:
        """
        Delete a paste owned by user.

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
            ...         async for paste in paspybin.pastes.get_all():
            ...             # paste.delete()
            ...             pass
            >>> asyncio.run(main())
        """
        if self._dev_key is None:
            raise ValueError("dev_key is required to use this method")

        if not self.is_authenticated():
            raise ValueError("only logged in users can use this method")

        payload = {
            "api_dev_key": self._dev_key,
            "api_option": "delete",
            "api_paste_key": self.key,
            "api_user_key": self._user_key,
        }

        async with self._session.post(self.api_post_url, data=payload) as response:
            data = await response.text()

            if not response.ok:
                raise PaspybinBadAPIRequestError(data)

    async def get_content(self) -> str:
        """
        Get the pasted content.

        Returns:
            A string of paste content.

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
            ...         async for paste in paspybin.pastes.get_all():
            ...             paste_content = await paste.get_content()
            ...             # do what you want to do with paste content here
            >>> asyncio.run(main())
        """
        if self._dev_key is None:
            raise ValueError("dev_key is required to use this method")

        if not self.is_authenticated():
            raise ValueError("only logged in users can use this method")

        payload = {
            "api_dev_key": self._dev_key,
            "api_option": "show_paste",
            "api_paste_key": self.key,
            "api_user_key": self._user_key,
        }

        async with self._session.post(self.api_raw_url, data=payload) as response:
            data = await response.text()

            if not response.ok:
                raise PaspybinBadAPIRequestError(data)

        return data
