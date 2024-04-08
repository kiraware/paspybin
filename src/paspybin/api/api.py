from traceback import TracebackException
from types import TracebackType
from typing import Self

from aiohttp import ClientSession

from ..types import DevKey, UserKey

__all__ = ["API"]


class API:
    """
    Base Pastebin API wrapper.

    This class has common attributes that all api must have.
    """

    base_url = "https://pastebin.com"

    api_url = "/api"
    raw_url = "/raw"

    api_post_url = api_url + "/api_post.php"
    api_login_url = api_url + "/api_login.php"
    api_raw_url = api_url + "/api_raw.php"

    def __init__(
        self,
        dev_key: DevKey | None = None,
        user_key: UserKey | None = None,
        session: ClientSession | None = None,
    ) -> None:
        self._dev_key = dev_key
        self._user_key = user_key
        self._session = session if session is not None else ClientSession(self.base_url)

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

    def is_authenticated(self) -> bool:
        return self._user_key is not None
