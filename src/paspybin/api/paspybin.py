from traceback import TracebackException
from types import TracebackType
from typing import Self

from ..exceptions import PaspybinBadAPIRequestError
from ..types import DevKey
from .api import API
from .pastes import Pastes
from .user import User

__all__ = [
    "Paspybin",
]


class Paspybin(API):
    """
    Main Pastebin API class.
    """

    def __init__(self, dev_key: DevKey | None = None):
        API.__init__(self, dev_key)

        self.user = User(self._dev_key, self._user_key, self._session)
        self.pastes = Pastes(self._dev_key, self._user_key, self._session)

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: Exception,
        exc_val: TracebackException,
        traceback: TracebackType,
    ) -> None:
        await self.close()

    async def close(self) -> None:
        if self._session is not None:
            await self._session.close()

    async def login(self, username: str, password: str) -> None:
        """
        Authenticating to Pastebin API based on credential auth given.

        Args:
            username: username of user.
            password: password of user.

        Raises:
            PaspybinBadAPIRequestError: if a bad request is sent to the API.

        Examples:
            >>> import asyncio
            >>> import os
            >>> PASTEBIN_API_DEV_KEY = os.environ["PASTEBIN_API_DEV_KEY"]
            >>> PASTEBIN_USERNAME = os.environ["PASTEBIN_USERNAME"]
            >>> PASTEBIN_PASSWORD = os.environ["PASTEBIN_PASSWORD"]
            >>> async def main():
            ...     async with Paspybin(PASTEBIN_API_DEV_KEY) as paspybin:
            ...         await paspybin.login(PASTEBIN_USERNAME, PASTEBIN_PASSWORD)
            >>> asyncio.run(main())
        """
        payload = {
            "api_dev_key": self._dev_key,
            "api_user_name": username,
            "api_user_password": password,
        }

        async with self._session.post(self.api_login_url, data=payload) as response:
            data = await response.text()

            if not response.ok:
                raise PaspybinBadAPIRequestError(data)

            user_key = data

            API.__init__(self, self._dev_key, user_key, self._session)

            self.user = User(self._dev_key, self._user_key, self._session)
            self.pastes = Pastes(self._dev_key, self._user_key, self._session)

    def logout(self) -> None:
        user_key = None

        API.__init__(self, self._dev_key, user_key, self._session)

        self.user = User(self._dev_key, self._user_key, self._session)
        self.pastes = Pastes(self._dev_key, self._user_key, self._session)
