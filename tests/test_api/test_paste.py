from datetime import datetime
from unittest.mock import patch

import pytest

from paspybin import Paspybin
from paspybin.api import Paste
from paspybin.enums import Format, Visibility
from paspybin.exceptions import PaspybinBadAPIRequestError


async def test_paste_validity_from_pastes_get_all():
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
                "<paste>"
                "<paste_key>paste_key</paste_key>"
                "<paste_date>1397883260</paste_date>"
                "<paste_title></paste_title>"
                "<paste_size>9</paste_size>"
                "<paste_expire_date>0</paste_expire_date>"
                "<paste_private>0</paste_private>"
                "<paste_format_long>None</paste_format_long>"
                "<paste_format_short>text</paste_format_short>"
                "<paste_url>https://pastebin.com/paste_key</paste_url>"
                "<paste_hits>15</paste_hits>"
                "</paste>"
            )
            pastes = [paste async for paste in paspybin.pastes.get_all()]

            assert len(pastes) == 2

            assert isinstance(pastes[0], Paste)
            assert pastes[0].key == "0b42rwhf"
            assert pastes[0].date == datetime.fromtimestamp(1297953260)
            assert pastes[0].title == "javascript test"
            assert pastes[0].size == 15
            assert pastes[0].expire_date == datetime.fromtimestamp(1297956860)
            assert pastes[0].private == Visibility.PUBLIC
            assert pastes[0].format == Format.JAVASCRIPT
            assert pastes[0].url == "https://pastebin.com/0b42rwhf"
            assert pastes[0].hits == 15

            assert isinstance(pastes[1], Paste)
            assert pastes[1].key == "paste_key"
            assert pastes[1].date == datetime.fromtimestamp(1397883260)
            assert pastes[1].title is None
            assert pastes[1].size == 9
            assert pastes[1].expire_date == datetime.fromtimestamp(0)
            assert pastes[1].private == Visibility.PUBLIC
            assert pastes[1].format == Format.NONE
            assert pastes[1].url == "https://pastebin.com/paste_key"
            assert pastes[1].hits == 15

        mocked.assert_called_with(
            "/api/api_post.php",
            data={
                "api_dev_key": "dev_key",
                "api_option": "list",
                "api_user_key": "user_key",
            },
        )


async def test_paste_delete():
    with patch("paspybin.api.api.ClientSession.post") as mocked:
        async with Paspybin("dev_key") as paspybin:
            mocked.return_value.__aenter__.return_value.text.return_value = "user_key"
            await paspybin.login("username", "password")

            mocked.return_value.__aenter__.return_value.text.return_value = (
                "<paste>"
                "<paste_key>paste_key</paste_key>"
                "<paste_date>1397883260</paste_date>"
                "<paste_title></paste_title>"
                "<paste_size>9</paste_size>"
                "<paste_expire_date>0</paste_expire_date>"
                "<paste_private>0</paste_private>"
                "<paste_format_long>None</paste_format_long>"
                "<paste_format_short>text</paste_format_short>"
                "<paste_url>https://pastebin.com/paste_key</paste_url>"
                "<paste_hits>15</paste_hits>"
                "</paste>"
            )
            pastes = [paste async for paste in paspybin.pastes.get_all()]

            await pastes[0].delete()

        mocked.assert_called_with(
            "/api/api_post.php",
            data={
                "api_dev_key": "dev_key",
                "api_option": "delete",
                "api_paste_key": "paste_key",
                "api_user_key": "user_key",
            },
        )


async def test_paste_delete_fail():
    with patch("paspybin.api.api.ClientSession.post") as mocked:
        async with Paspybin("dev_key") as paspybin:
            mocked.return_value.__aenter__.return_value.text.return_value = "user_key"
            await paspybin.login("username", "password")

            mocked.return_value.__aenter__.return_value.text.return_value = (
                "<paste>"
                "<paste_key>paste_key</paste_key>"
                "<paste_date>1397883260</paste_date>"
                "<paste_title></paste_title>"
                "<paste_size>9</paste_size>"
                "<paste_expire_date>0</paste_expire_date>"
                "<paste_private>0</paste_private>"
                "<paste_format_long>None</paste_format_long>"
                "<paste_format_short>text</paste_format_short>"
                "<paste_url>https://pastebin.com/paste_key</paste_url>"
                "<paste_hits>15</paste_hits>"
                "</paste>"
            )
            pastes = [paste async for paste in paspybin.pastes.get_all()]

            mocked.return_value.__aenter__.return_value.text.return_value = "err_msg"
            mocked.return_value.__aenter__.return_value.ok = False

            with pytest.raises(PaspybinBadAPIRequestError, match="err_msg"):
                await pastes[0].delete()

        mocked.assert_called_with(
            "/api/api_post.php",
            data={
                "api_dev_key": "dev_key",
                "api_option": "delete",
                "api_paste_key": "paste_key",
                "api_user_key": "user_key",
            },
        )


async def test_paste_get_content():
    with patch("paspybin.api.api.ClientSession.post") as mocked:
        async with Paspybin("dev_key") as paspybin:
            mocked.return_value.__aenter__.return_value.text.return_value = "user_key"
            await paspybin.login("username", "password")

            mocked.return_value.__aenter__.return_value.text.return_value = (
                "<paste>"
                "<paste_key>paste_key</paste_key>"
                "<paste_date>1397883260</paste_date>"
                "<paste_title></paste_title>"
                "<paste_size>9</paste_size>"
                "<paste_expire_date>0</paste_expire_date>"
                "<paste_private>0</paste_private>"
                "<paste_format_long>None</paste_format_long>"
                "<paste_format_short>text</paste_format_short>"
                "<paste_url>https://pastebin.com/paste_key</paste_url>"
                "<paste_hits>15</paste_hits>"
                "</paste>"
            )
            pastes = [paste async for paste in paspybin.pastes.get_all()]

            mocked.return_value.__aenter__.return_value.text.return_value = "test"
            paste_content = await pastes[0].get_content()

            assert paste_content == "test"

        mocked.assert_called_with(
            "/api/api_raw.php",
            data={
                "api_dev_key": "dev_key",
                "api_option": "show_paste",
                "api_paste_key": "paste_key",
                "api_user_key": "user_key",
            },
        )


async def test_paste_get_content_fail():
    with patch("paspybin.api.api.ClientSession.post") as mocked:
        async with Paspybin("dev_key") as paspybin:
            mocked.return_value.__aenter__.return_value.text.return_value = "user_key"
            await paspybin.login("username", "password")

            mocked.return_value.__aenter__.return_value.text.return_value = (
                "<paste>"
                "<paste_key>paste_key</paste_key>"
                "<paste_date>1397883260</paste_date>"
                "<paste_title></paste_title>"
                "<paste_size>9</paste_size>"
                "<paste_expire_date>0</paste_expire_date>"
                "<paste_private>0</paste_private>"
                "<paste_format_long>None</paste_format_long>"
                "<paste_format_short>text</paste_format_short>"
                "<paste_url>https://pastebin.com/paste_key</paste_url>"
                "<paste_hits>15</paste_hits>"
                "</paste>"
            )
            pastes = [paste async for paste in paspybin.pastes.get_all()]

            mocked.return_value.__aenter__.return_value.text.return_value = "err_msg"
            mocked.return_value.__aenter__.return_value.ok = False

            with pytest.raises(PaspybinBadAPIRequestError, match="err_msg"):
                await pastes[0].get_content()

        mocked.assert_called_with(
            "/api/api_raw.php",
            data={
                "api_dev_key": "dev_key",
                "api_option": "show_paste",
                "api_paste_key": "paste_key",
                "api_user_key": "user_key",
            },
        )
