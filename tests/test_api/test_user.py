from unittest.mock import patch

import pytest

from paspybin import Paspybin, schemas
from paspybin.api import User
from paspybin.enums import Expire, Format, Type, Visibility
from paspybin.exceptions import PaspybinBadAPIRequestError


async def test_user_get_detail():
    with patch("paspybin.api.api.ClientSession.post") as mocked:
        async with Paspybin("dev_key") as paspybin:
            mocked.return_value.__aenter__.return_value.text.return_value = "user_key"
            await paspybin.login("username", "password")

            mocked.return_value.__aenter__.return_value.text.return_value = (
                "<user>"
                "<user_name>wiz_kitty</user_name>"
                "<user_format_short>text</user_format_short>"
                "<user_expiration>N</user_expiration>"
                "<user_avatar_url>https://pastebin.com/cache/a/1.jpg</user_avatar_url>"
                "<user_private>1</user_private>"
                "<user_website>https://myawesomesite.com</user_website>"
                "<user_email>oh@dear.com</user_email>"
                "<user_location>New York</user_location>"
                "<user_account_type>1</user_account_type>"
                "</user>"
            )
            user_detail = await paspybin.user.get_detail()

            assert isinstance(user_detail, schemas.User)

            assert user_detail.name == "wiz_kitty"
            assert user_detail.format == "text"
            assert isinstance(user_detail.format, Format)
            assert user_detail.expiration == "N"
            assert isinstance(user_detail.expiration, Expire)
            assert user_detail.avatar_url == "https://pastebin.com/cache/a/1.jpg"
            assert user_detail.private == 1
            assert isinstance(user_detail.private, Visibility)
            assert user_detail.website == "https://myawesomesite.com"
            assert user_detail.email == "oh@dear.com"
            assert user_detail.location == "New York"
            assert user_detail.account_type == 1
            assert isinstance(user_detail.account_type, Type)

        mocked.assert_called_with(
            "/api/api_post.php",
            data={
                "api_dev_key": "dev_key",
                "api_option": "userdetails",
                "api_user_key": "user_key",
            },
        )


async def test_direct_user_get_detail():
    with patch("paspybin.api.api.ClientSession.post") as mocked:
        async with User("dev_key", "user_key") as user:
            mocked.return_value.__aenter__.return_value.text.return_value = (
                "<user>"
                "<user_name>wiz_kitty</user_name>"
                "<user_format_short>text</user_format_short>"
                "<user_expiration>N</user_expiration>"
                "<user_avatar_url>https://pastebin.com/cache/a/1.jpg</user_avatar_url>"
                "<user_private>1</user_private>"
                "<user_website>https://myawesomesite.com</user_website>"
                "<user_email>oh@dear.com</user_email>"
                "<user_location>New York</user_location>"
                "<user_account_type>1</user_account_type>"
                "</user>"
            )
            user_detail = await user.get_detail()

            assert isinstance(user_detail, schemas.User)

            assert user_detail.name == "wiz_kitty"
            assert user_detail.format == "text"
            assert isinstance(user_detail.format, Format)
            assert user_detail.expiration == "N"
            assert isinstance(user_detail.expiration, Expire)
            assert user_detail.avatar_url == "https://pastebin.com/cache/a/1.jpg"
            assert user_detail.private == 1
            assert isinstance(user_detail.private, Visibility)
            assert user_detail.website == "https://myawesomesite.com"
            assert user_detail.email == "oh@dear.com"
            assert user_detail.location == "New York"
            assert user_detail.account_type == 1
            assert isinstance(user_detail.account_type, Type)

        mocked.assert_called_with(
            "/api/api_post.php",
            data={
                "api_dev_key": "dev_key",
                "api_option": "userdetails",
                "api_user_key": "user_key",
            },
        )


async def test_user_get_detail_without_dev_key():
    async with Paspybin() as paspybin:
        with pytest.raises(ValueError, match="dev_key is required to use this method"):
            await paspybin.user.get_detail()


async def test_direct_user_get_detail_without_dev_key():
    async with User() as user:
        with pytest.raises(ValueError, match="dev_key is required to use this method"):
            await user.get_detail()


async def test_user_get_detail_with_guest():
    async with Paspybin("dev_key") as paspybin:
        with pytest.raises(
            ValueError, match="only logged in users can use this method"
        ):
            await paspybin.user.get_detail()


async def test_direct_user_get_detail_with_guest():
    async with User("dev_key") as user:
        with pytest.raises(
            ValueError, match="only logged in users can use this method"
        ):
            await user.get_detail()


async def test_user_get_detail_fail():
    with patch("paspybin.api.api.ClientSession.post") as mocked:
        async with Paspybin("dev_key") as paspybin:
            mocked.return_value.__aenter__.return_value.text.return_value = "user_key"
            await paspybin.login("username", "password")

            mocked.return_value.__aenter__.return_value.text.return_value = "err_msg"
            mocked.return_value.__aenter__.return_value.ok = False

            with pytest.raises(PaspybinBadAPIRequestError, match="err_msg"):
                await paspybin.user.get_detail()

        mocked.assert_called_with(
            "/api/api_post.php",
            data={
                "api_dev_key": "dev_key",
                "api_option": "userdetails",
                "api_user_key": "user_key",
            },
        )


async def test_direct_user_get_detail_fail():
    with patch("paspybin.api.api.ClientSession.post") as mocked:
        async with User("dev_key", "user_key") as user:
            mocked.return_value.__aenter__.return_value.text.return_value = "err_msg"
            mocked.return_value.__aenter__.return_value.ok = False

            with pytest.raises(PaspybinBadAPIRequestError, match="err_msg"):
                await user.get_detail()

        mocked.assert_called_with(
            "/api/api_post.php",
            data={
                "api_dev_key": "dev_key",
                "api_option": "userdetails",
                "api_user_key": "user_key",
            },
        )
