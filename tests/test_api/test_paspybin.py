from unittest.mock import patch

import pytest

from paspybin import Paspybin
from paspybin.exceptions import PaspybinBadAPIRequestError


async def test_paspybin_login():
    with patch("paspybin.api.api.ClientSession.post") as mocked:
        async with Paspybin("dev_key") as paspybin:
            mocked.return_value.__aenter__.return_value.text.return_value = "user_key"

            await paspybin.login("username", "password")

            mocked.assert_called_once_with(
                "/api/api_login.php",
                data={
                    "api_dev_key": "dev_key",
                    "api_user_name": "username",
                    "api_user_password": "password",
                },
            )

            assert paspybin._user_key == "user_key"
            assert paspybin.user._user_key == "user_key"
            assert paspybin.pastes._user_key == "user_key"


async def test_paspybin_login_without_dev_key():
    async with Paspybin() as paspybin:
        with pytest.raises(ValueError, match="dev_key is required to use this method"):
            await paspybin.login("username", "password")


async def test_paspybin_login_fail():
    with patch("paspybin.api.api.ClientSession.post") as mocked:
        async with Paspybin("dev_key") as paspybin:
            mocked.return_value.__aenter__.return_value.text.return_value = "err_msg"
            mocked.return_value.__aenter__.return_value.ok = False

            with pytest.raises(PaspybinBadAPIRequestError, match="err_msg"):
                await paspybin.login("username", "password")

            mocked.assert_called_once_with(
                "/api/api_login.php",
                data={
                    "api_dev_key": "dev_key",
                    "api_user_name": "username",
                    "api_user_password": "password",
                },
            )


async def test_paspybin_logout():
    with patch("paspybin.api.api.ClientSession.post") as mocked:
        async with Paspybin("dev_key") as paspybin:
            mocked.return_value.__aenter__.return_value.text.return_value = "user_key"

            await paspybin.login("username", "password")

            assert paspybin._user_key == "user_key"
            assert paspybin.user._user_key == "user_key"
            assert paspybin.pastes._user_key == "user_key"

            paspybin.logout()

            assert paspybin._user_key is None
            assert paspybin.user._user_key is None
            assert paspybin.pastes._user_key is None
