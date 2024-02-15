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
        date: datetime,
        title: str,
        size: int,
        expire_date: datetime,
        private: Visibility,
        format: Format,
        url: PastebinUrl,
        hits: int,
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

        Examples:
            >>> import asyncio
            >>> import os
            >>> from paspybin import Paspybin
            >>> PASTEBIN_API_DEV_KEY = os.environ["PASTEBIN_API_DEV_KEY"]
            >>> PASTEBIN_USERNAME = os.environ["PASTEBIN_USERNAME"]
            >>> PASTEBIN_PASSWORD = os.environ["PASTEBIN_PASSWORD"]
            >>> async def main():
            ...     async with Paspybin(PASTEBIN_API_DEV_KEY) as paspybin:
            ...         await paspybin.login(PASTEBIN_USERNAME, PASTEBIN_PASSWORD)
            ...         async for paste in paspybin.pastes.get_all():
            ...             # paste.delete()
            ...             pass
            >>> asyncio.run(main())
        """
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

        Examples:
            >>> import asyncio
            >>> import os
            >>> from paspybin import Paspybin
            >>> PASTEBIN_API_DEV_KEY = os.environ["PASTEBIN_API_DEV_KEY"]
            >>> PASTEBIN_USERNAME = os.environ["PASTEBIN_USERNAME"]
            >>> PASTEBIN_PASSWORD = os.environ["PASTEBIN_PASSWORD"]
            >>> async def main():
            ...     async with Paspybin(PASTEBIN_API_DEV_KEY) as paspybin:
            ...         await paspybin.login(PASTEBIN_USERNAME, PASTEBIN_PASSWORD)
            ...         async for paste in paspybin.pastes.get_all():
            ...             paste_content = await paste.get_content()
            ...             # do what you want to do with paste content here
            >>> asyncio.run(main())
        """
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
