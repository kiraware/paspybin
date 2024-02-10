from unittest.mock import MagicMock, patch

import pytest

from paspybin.exception import PaspybinParseError
from paspybin.parser import parse_pastes


def test_parse_pastes_with_invalid_fields_length():
    paste = MagicMock()
    paste.__len__.return_value = 9

    with patch("paspybin.parser.fromstring", return_value=[paste]):
        with pytest.raises(
            PaspybinParseError,
            match="one or more fields not found",
        ):
            for paste in parse_pastes("<paste></paste>"):
                pass


@pytest.mark.parametrize(
    "index, err_msg",
    (
        (0, "paste_key value not found"),
        (1, "paste_date value not found"),
        (2, "paste_title value not found"),
        (3, "paste_size value not found"),
        (4, "paste_expire_date value not found"),
        (5, "paste_private value not found"),
        # (6, ""),
        (7, "paste_format_short value not found"),
        (8, "paste_url value not found"),
        (9, "paste_hits value not found"),
    ),
)
def test_parse_pastes_with_invalid_field(index, err_msg):
    field = MagicMock()
    field.text = None

    paste = MagicMock()
    paste.__len__.return_value = 10
    paste.__getitem__.side_effect = lambda idx: field if idx == index else MagicMock()

    with patch("paspybin.parser.fromstring", return_value=[paste]):
        with pytest.raises(
            PaspybinParseError,
            match=err_msg,
        ):
            for paste in parse_pastes("<paste></paste>"):
                pass
