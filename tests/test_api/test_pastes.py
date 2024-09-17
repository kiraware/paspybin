from http import HTTPStatus
from unittest.mock import patch

import pytest

from paspybin import Paspybin
from paspybin.api import Paste, Pastes
from paspybin.enums import Expire, Format, Visibility
from paspybin.exceptions import PaspybinBadAPIRequestError, PaspybinNotFoundError


async def test_pastes_get_all():
    with patch("paspybin.api.api.ClientSession.post") as mocked:
        async with Paspybin("dev_key") as paspybin:
            mocked.return_value.__aenter__.return_value.text.return_value = "user_key"
            await paspybin.login("username", "password")

            mocked.return_value.__aenter__.return_value.text.return_value = (
                "<paste>"
                "<paste_key>0b42rwhf</paste_key>"
                "<paste_date>1297953260</paste_date>"
                "<paste_title>javascript test</paste_title>"
                "<paste_size>15</paste_size>"
                "<paste_expire_date>1297956860</paste_expire_date>"
                "<paste_private>0</paste_private>"
                "<paste_format_long>JavaScript</paste_format_long>"
                "<paste_format_short>javascript</paste_format_short>"
                "<paste_url>https://pastebin.com/0b42rwhf</paste_url>"
                "<paste_hits>15</paste_hits>"
                "</paste>"
            )
            pastes = [paste async for paste in paspybin.pastes.get_all()]

            assert len(pastes) == 1
            assert isinstance(pastes[0], Paste)

        mocked.assert_called_with(
            "/api/api_post.php",
            data={
                "api_dev_key": "dev_key",
                "api_option": "list",
                "api_user_key": "user_key",
            },
        )


async def test_direct_pastes_get_all():
    with patch("paspybin.api.api.ClientSession.post") as mocked:
        async with Pastes("dev_key", "user_key") as pastes:
            mocked.return_value.__aenter__.return_value.text.return_value = (
                "<paste>"
                "<paste_key>0b42rwhf</paste_key>"
                "<paste_date>1297953260</paste_date>"
                "<paste_title>javascript test</paste_title>"
                "<paste_size>15</paste_size>"
                "<paste_expire_date>1297956860</paste_expire_date>"
                "<paste_private>0</paste_private>"
                "<paste_format_long>JavaScript</paste_format_long>"
                "<paste_format_short>javascript</paste_format_short>"
                "<paste_url>https://pastebin.com/0b42rwhf</paste_url>"
                "<paste_hits>15</paste_hits>"
                "</paste>"
            )
            pastes_data = [paste async for paste in pastes.get_all()]

            assert len(pastes_data) == 1
            assert isinstance(pastes_data[0], Paste)

        mocked.assert_called_with(
            "/api/api_post.php",
            data={
                "api_dev_key": "dev_key",
                "api_option": "list",
                "api_user_key": "user_key",
            },
        )


async def test_pastes_get_all_but_empty():
    with patch("paspybin.api.api.ClientSession.post") as mocked:
        async with Paspybin("dev_key") as paspybin:
            mocked.return_value.__aenter__.return_value.text.return_value = "user_key"
            await paspybin.login("username", "password")

            mocked.return_value.__aenter__.return_value.text.return_value = (
                "No pastes found."
            )
            pastes = [paste async for paste in paspybin.pastes.get_all()]

            assert len(pastes) == 0

        mocked.assert_called_with(
            "/api/api_post.php",
            data={
                "api_dev_key": "dev_key",
                "api_option": "list",
                "api_user_key": "user_key",
            },
        )


async def test_direct_pastes_get_all_but_empty():
    with patch("paspybin.api.api.ClientSession.post") as mocked:
        async with Pastes("dev_key", "user_key") as pastes:
            mocked.return_value.__aenter__.return_value.text.return_value = (
                "No pastes found."
            )
            pastes_data = [paste async for paste in pastes.get_all()]

            assert len(pastes_data) == 0

        mocked.assert_called_with(
            "/api/api_post.php",
            data={
                "api_dev_key": "dev_key",
                "api_option": "list",
                "api_user_key": "user_key",
            },
        )


async def test_pastes_get_all_without_dev_key():
    async with Paspybin() as paspybin:
        with pytest.raises(ValueError, match="dev_key is required to use this method"):
            async for _paste in paspybin.pastes.get_all():
                pass


async def test_direct_pastes_get_all_without_dev_key():
    async with Pastes() as pastes:
        with pytest.raises(ValueError, match="dev_key is required to use this method"):
            async for _paste in pastes.get_all():
                pass


async def test_pastes_get_all_with_guest():
    async with Paspybin("dev_key") as paspybin:
        with pytest.raises(
            ValueError, match="only logged in users can use this method"
        ):
            async for _paste in paspybin.pastes.get_all():
                pass


async def test_direct_pastes_get_all_with_guest():
    async with Pastes("dev_key") as pastes:
        with pytest.raises(
            ValueError, match="only logged in users can use this method"
        ):
            async for _paste in pastes.get_all():
                pass


async def test_pastes_get_all_of_logged_in_user_when_limit_is_valid():
    with patch("paspybin.api.api.ClientSession.post") as mocked:
        async with Paspybin("dev_key") as paspybin:
            mocked.return_value.__aenter__.return_value.text.return_value = "user_key"
            await paspybin.login("username", "password")

            mocked.return_value.__aenter__.return_value.text.return_value = (
                "<paste>"
                "<paste_key>0b42rwhf</paste_key>"
                "<paste_date>1297953260</paste_date>"
                "<paste_title>javascript test</paste_title>"
                "<paste_size>15</paste_size>"
                "<paste_expire_date>1297956860</paste_expire_date>"
                "<paste_private>0</paste_private>"
                "<paste_format_long>JavaScript</paste_format_long>"
                "<paste_format_short>javascript</paste_format_short>"
                "<paste_url>https://pastebin.com/0b42rwhf</paste_url>"
                "<paste_hits>15</paste_hits>"
                "</paste>"
            )

            async for _paste in paspybin.pastes.get_all(50):
                pass

        mocked.assert_called_with(
            "/api/api_post.php",
            data={
                "api_dev_key": "dev_key",
                "api_option": "list",
                "api_user_key": "user_key",
                "api_results_limit": 50,
            },
        )


async def test_direct_pastes_get_all_of_logged_in_user_when_limit_is_valid():
    with patch("paspybin.api.api.ClientSession.post") as mocked:
        async with Pastes("dev_key", "user_key") as pastes:
            mocked.return_value.__aenter__.return_value.text.return_value = (
                "<paste>"
                "<paste_key>0b42rwhf</paste_key>"
                "<paste_date>1297953260</paste_date>"
                "<paste_title>javascript test</paste_title>"
                "<paste_size>15</paste_size>"
                "<paste_expire_date>1297956860</paste_expire_date>"
                "<paste_private>0</paste_private>"
                "<paste_format_long>JavaScript</paste_format_long>"
                "<paste_format_short>javascript</paste_format_short>"
                "<paste_url>https://pastebin.com/0b42rwhf</paste_url>"
                "<paste_hits>15</paste_hits>"
                "</paste>"
            )

            async for _paste in pastes.get_all(50):
                pass

        mocked.assert_called_with(
            "/api/api_post.php",
            data={
                "api_dev_key": "dev_key",
                "api_option": "list",
                "api_user_key": "user_key",
                "api_results_limit": 50,
            },
        )


@pytest.mark.parametrize("limit", (0, 1001))
async def test_pastes_get_all_of_logged_in_user_but_limit_is_invalid(limit):
    with patch("paspybin.api.api.ClientSession.post") as mocked:
        async with Paspybin("dev_key") as paspybin:
            mocked.return_value.__aenter__.return_value.text.return_value = "user_key"
            await paspybin.login("username", "password")

            with pytest.raises(
                ValueError, match="limit value must be between 1 and 1000"
            ):
                async for _paste in paspybin.pastes.get_all(limit):
                    pass


@pytest.mark.parametrize("limit", (0, 1001))
async def test_direct_pastes_get_all_of_logged_in_user_but_limit_is_invalid(limit):
    async with Pastes("dev_key", "user_key") as pastes:
        with pytest.raises(ValueError, match="limit value must be between 1 and 1000"):
            async for _paste in pastes.get_all(limit):
                pass


async def test_pastes_get_all_fail():
    with patch("paspybin.api.api.ClientSession.post") as mocked:
        async with Paspybin("dev_key") as paspybin:
            mocked.return_value.__aenter__.return_value.text.return_value = "user_key"
            await paspybin.login("username", "password")

            mocked.return_value.__aenter__.return_value.text.return_value = "err_msg"
            mocked.return_value.__aenter__.return_value.ok = False

            with pytest.raises(PaspybinBadAPIRequestError, match="err_msg"):
                async for _paste in paspybin.pastes.get_all():
                    pass

        mocked.assert_called_with(
            "/api/api_post.php",
            data={
                "api_dev_key": "dev_key",
                "api_option": "list",
                "api_user_key": "user_key",
            },
        )


async def test_direct_pastes_get_all_fail():
    with patch("paspybin.api.api.ClientSession.post") as mocked:
        async with Pastes("dev_key", "user_key") as pastes:
            mocked.return_value.__aenter__.return_value.text.return_value = "err_msg"
            mocked.return_value.__aenter__.return_value.ok = False

            with pytest.raises(PaspybinBadAPIRequestError, match="err_msg"):
                async for _paste in pastes.get_all():
                    pass

        mocked.assert_called_with(
            "/api/api_post.php",
            data={
                "api_dev_key": "dev_key",
                "api_option": "list",
                "api_user_key": "user_key",
            },
        )


async def test_pastes_get_content():
    with patch("paspybin.api.api.ClientSession.get") as mocked:
        async with Pastes() as pastes:
            mocked.return_value.__aenter__.return_value.text.return_value = (
                "just some paste content"
            )
            paste_content = await pastes.get_content("paste_key")

            assert paste_content == "just some paste content"

        mocked.assert_called_once_with("/raw/paste_key")


async def test_pastes_get_content_but_not_found():
    with patch("paspybin.api.api.ClientSession.get") as mocked:
        async with Paspybin() as paspybin:
            mocked.return_value.__aenter__.return_value.status = HTTPStatus.NOT_FOUND

            with pytest.raises(PaspybinNotFoundError):
                await paspybin.pastes.get_content("paste_key")

        mocked.assert_called_once_with("/raw/paste_key")


async def test_direct_pastes_get_content_but_not_found():
    with patch("paspybin.api.api.ClientSession.get") as mocked:
        async with Pastes() as pastes:
            mocked.return_value.__aenter__.return_value.status = HTTPStatus.NOT_FOUND

            with pytest.raises(PaspybinNotFoundError):
                await pastes.get_content("paste_key")

        mocked.assert_called_once_with("/raw/paste_key")


@pytest.mark.parametrize("is_login", (True, False))
async def test_create_paste_with_logged_in_user(is_login):
    with patch("paspybin.api.api.ClientSession.post") as mocked:
        async with Paspybin("dev_key") as paspybin:
            if is_login:
                mocked.return_value.__aenter__.return_value.text.return_value = (
                    "user_key"
                )
                await paspybin.login("username", "password")

            mocked.return_value.__aenter__.return_value.text.return_value = (
                "https://pastebin.com/paste_key"
            )

            paste_key = await paspybin.pastes.create_paste(
                "test",
                "title",
                Format.ARM,
                Visibility.UNLISTED,
                Expire.ONE_MONTH,
                "folder_key",
            )

            assert paste_key == "paste_key"

        payload = {
            "api_dev_key": "dev_key",
            "api_option": "paste",
            "api_paste_code": "test",
            "api_paste_name": "title",
            "api_paste_format": Format.ARM,
            "api_paste_private": Visibility.UNLISTED,
            "api_paste_expire_date": Expire.ONE_MONTH,
            "api_folder_key": "folder_key",
        }

        if is_login:
            payload["api_user_key"] = "user_key"

        mocked.assert_called_with("/api/api_post.php", data=payload)


async def test_direct_create_paste_with_logged_in_user():
    with patch("paspybin.api.api.ClientSession.post") as mocked:
        async with Pastes("dev_key", "user_key") as pastes:
            mocked.return_value.__aenter__.return_value.text.return_value = (
                "https://pastebin.com/paste_key"
            )

            paste_key = await pastes.create_paste(
                "test",
                "title",
                Format.ARM,
                Visibility.UNLISTED,
                Expire.ONE_MONTH,
                "folder_key",
            )

            assert paste_key == "paste_key"

        payload = {
            "api_dev_key": "dev_key",
            "api_option": "paste",
            "api_paste_code": "test",
            "api_user_key": "user_key",
            "api_paste_name": "title",
            "api_paste_format": Format.ARM,
            "api_paste_private": Visibility.UNLISTED,
            "api_paste_expire_date": Expire.ONE_MONTH,
            "api_folder_key": "folder_key",
        }

        mocked.assert_called_with("/api/api_post.php", data=payload)


async def test_direct_create_paste_with_guest_user():
    with patch("paspybin.api.api.ClientSession.post") as mocked:
        async with Pastes("dev_key") as pastes:
            mocked.return_value.__aenter__.return_value.text.return_value = (
                "https://pastebin.com/paste_key"
            )

            paste_key = await pastes.create_paste(
                "test",
                "title",
                Format.ARM,
                Visibility.UNLISTED,
                Expire.ONE_MONTH,
                "folder_key",
            )

            assert paste_key == "paste_key"

        payload = {
            "api_dev_key": "dev_key",
            "api_option": "paste",
            "api_paste_code": "test",
            "api_paste_name": "title",
            "api_paste_format": Format.ARM,
            "api_paste_private": Visibility.UNLISTED,
            "api_paste_expire_date": Expire.ONE_MONTH,
            "api_folder_key": "folder_key",
        }

        mocked.assert_called_with("/api/api_post.php", data=payload)


async def test_create_paste_without_dev_key():
    async with Paspybin() as paspybin:
        with pytest.raises(ValueError, match="dev_key is required to use this method"):
            await paspybin.pastes.create_paste("test")


async def test_direct_create_paste_without_dev_key():
    async with Pastes() as pastes:
        with pytest.raises(ValueError, match="dev_key is required to use this method"):
            await pastes.create_paste("test")


async def test_create_paste_with_empty_content():
    async with Paspybin("dev_key") as paspybin:
        with pytest.raises(ValueError, match="paste content was empty"):
            await paspybin.pastes.create_paste("")


async def test_direct_create_paste_with_empty_content():
    async with Pastes("dev_key") as pastes:
        with pytest.raises(ValueError, match="paste content was empty"):
            await pastes.create_paste("")


async def test_create_paste_with_guest_using_private_visibility():
    async with Paspybin("dev_key") as paspybin:
        with pytest.raises(
            ValueError, match="guest paste visibility cannot be private"
        ):
            await paspybin.pastes.create_paste("test", visibility=Visibility.PRIVATE)


async def test_direct_create_paste_with_guest_using_private_visibility():
    async with Pastes("dev_key") as pastes:
        with pytest.raises(
            ValueError, match="guest paste visibility cannot be private"
        ):
            await pastes.create_paste("test", visibility=Visibility.PRIVATE)


async def test_create_paste_fail():
    with patch("paspybin.api.api.ClientSession.post") as mocked:
        async with Paspybin("dev_key") as paspybin:
            mocked.return_value.__aenter__.return_value.text.return_value = "err_msg"
            mocked.return_value.__aenter__.return_value.ok = False

            with pytest.raises(PaspybinBadAPIRequestError, match="err_msg"):
                await paspybin.pastes.create_paste("test")

        mocked.assert_called_once_with(
            "/api/api_post.php",
            data={
                "api_dev_key": "dev_key",
                "api_option": "paste",
                "api_paste_code": "test",
            },
        )


async def test_direct_create_paste_fail():
    with patch("paspybin.api.api.ClientSession.post") as mocked:
        async with Pastes("dev_key") as pastes:
            mocked.return_value.__aenter__.return_value.text.return_value = "err_msg"
            mocked.return_value.__aenter__.return_value.ok = False

            with pytest.raises(PaspybinBadAPIRequestError, match="err_msg"):
                await pastes.create_paste("test")

        mocked.assert_called_once_with(
            "/api/api_post.php",
            data={
                "api_dev_key": "dev_key",
                "api_option": "paste",
                "api_paste_code": "test",
            },
        )
