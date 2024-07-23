from http import HTTPStatus
from typing import Any, AsyncIterator

from ..enums import Expire, Format, Visibility
from ..exceptions import PaspybinBadAPIRequestError, PaspybinNotFoundError
from ..parsers import parse_pastes
from ..types import FolderKey, PasteKey
from .api import API
from .paste import Paste

__all__ = ["Pastes"]


class Pastes(API):
    async def get_all(self, limit: int | None = None) -> AsyncIterator[Paste]:
        """
        Get list of pastes owned by user.

        Args:
            limit: Length limit of the paste list. By default the limit is 50, the
                minimum limit is 1 and the maximum limit is 1000.

        Yields:
            Some pastes.

        Raises:
            PaspybinBadAPIRequestError: if a bad request is sent to the API.
            ValueError: if dev_key not supplied.
            ValueError: if guest use this method.
            ValueError: if the limit value is less than 1 or more than 1000.

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
            ...             # do what you want to do with paste here
            ...             pass
            >>> asyncio.run(main())
        """
        if self._dev_key is None:
            raise ValueError("dev_key is required to use this method")

        if not self.is_authenticated():
            raise ValueError("only logged in users can use this method")

        payload: dict[str, Any] = {
            "api_dev_key": self._dev_key,
            "api_option": "list",
            "api_user_key": self._user_key,
        }

        if limit is not None:
            if limit < 1 or limit > 1000:
                raise ValueError("limit value must be between 1 and 1000")

            payload["api_results_limit"] = limit

        async with self._session.post(self.api_post_url, data=payload) as response:
            data = await response.text()

            if not response.ok:
                raise PaspybinBadAPIRequestError(data)
            else:
                for paste in parse_pastes(data):
                    yield Paste(
                        paste.key,
                        paste.date,
                        paste.title,
                        paste.size,
                        paste.expire_date,
                        paste.private,
                        paste.format,
                        paste.url,
                        paste.hits,
                        self._dev_key,
                        self._user_key,
                        self._session,
                    )

    async def get_content(self, paste_key: PasteKey) -> str:
        """
        Get the public or unlisted pasted content.

        Args:
            paste_key: A paste key of the paste content that you want to get.

        Returns:
            A string of paste content.

        Raises:
            PaspybinNotFoundError: if paste content not found.

        Examples:
            >>> import asyncio
            >>> from paspybin import Paspybin
            >>> async def main():
            ...     async with Paspybin() as paspybin:
            ...         paste_key = "0C343n0d"
            ...         paste_content = await paspybin.pastes.get_content(paste_key)
            ...         # do what you want to do with paste content here
            >>> asyncio.run(main())
        """
        async with self._session.get(f"{self.raw_url}/{paste_key}") as response:
            if response.status == HTTPStatus.NOT_FOUND:
                raise PaspybinNotFoundError("paste not found")
            data = await response.text()

        return data

    async def create_paste(
        self,
        content: str,
        title: str | None = None,
        format: Format | None = None,
        visibility: Visibility | None = None,
        expire: Expire | None = None,
        folder_key: FolderKey | None = None,
    ) -> PasteKey:
        """
        Create a new paste.

        Args:
            content: The paste content that you want to create.
            title: title of the paste.
            format: syntax highlighting format of the paste.
            visibility: visibility of the paste.
            expire: expire of the paste.
            folder_key: a folder that you want to store the paste.

        Returns:
            A paste key.

        Raises:
            PaspybinBadAPIRequestError: if a bad request is sent to the API.
            ValueError: if dev_key not supplied.
            ValueError: if the paste content is empty.
            ValueError: if the paste visibility is private for guest.

        Examples:
            >>> import asyncio
            >>> import os
            >>> from paspybin import Paspybin
            >>> PASTEBIN_API_DEV_KEY = os.environ["PASTEBIN_API_DEV_KEY"]
            >>> async def main():
            ...     async with Paspybin(PASTEBIN_API_DEV_KEY) as paspybin:
            ...         paste_content = "some paste content"
            ...         paste_key = await paspybin.pastes.create_paste(paste_content)
            ...         # do what you want to do with paste key here
            >>> asyncio.run(main())
        """
        if self._dev_key is None:
            raise ValueError("dev_key is required to use this method")

        if content == "":
            raise ValueError("paste content was empty")

        if visibility == Visibility.PRIVATE and not self.is_authenticated():
            raise ValueError("guest paste visibility cannot be private")

        payload = {
            "api_dev_key": self._dev_key,
            "api_option": "paste",
            "api_paste_code": content,
        }

        optional_payload: dict[str, Any] = {
            "api_user_key": self._user_key,
            "api_paste_name": title,
            "api_paste_format": format,
            "api_paste_private": visibility,
            "api_paste_expire_date": expire,
            "api_folder_key": folder_key,
        }

        payload.update({k: v for k, v in optional_payload.items() if v is not None})

        async with self._session.post(self.api_post_url, data=payload) as response:
            data = await response.text()

            if not response.ok:
                raise PaspybinBadAPIRequestError(data)

            return data[21:]
