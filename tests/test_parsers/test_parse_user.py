from unittest.mock import MagicMock, patch

import pytest

from paspybin.exceptions import PaspybinParseError
from paspybin.parsers import parse_user


def test_parse_pastes_with_invalid_fields_length():
    user = MagicMock()
    user.__len__.return_value = 8

    with patch("paspybin.parsers.fromstring", return_value=user):
        with pytest.raises(
            PaspybinParseError,
            match="one or more fields not found",
        ):
            parse_user("<user></user>")


@pytest.mark.parametrize(
    "index, err_msg",
    (
        (0, "user_name value not found"),
        (1, "user_format_short value not found"),
        (2, "user_expiration value not found"),
        (3, "user_avatar_url value not found"),
        (4, "user_private value not found"),
        (6, "user_email value not found"),
        (8, "user_account_type value not found"),
    ),
)
def test_parse_user_with_invalid_field(index, err_msg):
    field = MagicMock()
    field.text = None

    user = MagicMock()
    user.__len__.return_value = 9
    user.__getitem__.side_effect = lambda idx: field if idx == index else MagicMock()

    with patch("paspybin.parsers.fromstring", return_value=user):
        with pytest.raises(
            PaspybinParseError,
            match=err_msg,
        ):
            parse_user("<user></user>")
