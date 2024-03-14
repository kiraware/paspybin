from collections.abc import Iterator
from datetime import datetime

# FIXME
# Element is used only for typing not parsing
from xml.etree.ElementTree import Element  # nosec B405

from defusedxml.ElementTree import fromstring

from .enums import Expire, Format, Type, Visibility
from .exceptions import PaspybinParseError
from .schemas import Paste, User

__all__ = [
    "parse_pastes",
    "parse_user",
]


def parse_pastes(data: str) -> Iterator[Paste]:
    """
    Parse pastes xml string.

    Args:
        data: str of pastes xml

    Yields:
        Some `Paste` schema.

    Raises:
        PaspybinParseError: if one or more required fields are not found.

    Examples:
    >>> data = (
    ...     "<paste>"
    ...     "<paste_key>0b42rwhf</paste_key>"
    ...     "<paste_date>1297953260</paste_date>"
    ...     "<paste_title>javascript test</paste_title>"
    ...     "<paste_size>15</paste_size>"
    ...     "<paste_expire_date>1297956860</paste_expire_date>"
    ...     "<paste_private>0</paste_private>"
    ...     "<paste_format_long>JavaScript</paste_format_long>"
    ...     "<paste_format_short>javascript</paste_format_short>"
    ...     "<paste_url>https://pastebin.com/0b42rwhf</paste_url>"
    ...     "<paste_hits>15</paste_hits>"
    ...     "</paste>"
    ... )
    >>> pastes = parse_pastes(data)
    >>> pastes
    <generator object parse_pastes at ...>
    """
    if data == "No pastes found.":
        return

    pastes: Element = fromstring(f"<pastes>{data}</pastes>")

    for paste in pastes:
        if len(paste) < 10:
            raise PaspybinParseError("one or more fields not found")

        paste_key = paste[0].text
        paste_date = paste[1].text
        paste_title = paste[2].text
        paste_size = paste[3].text
        paste_expire_date = paste[4].text
        paste_private = paste[5].text
        # paste_format_long = paste[6].text
        paste_format_short = paste[7].text
        paste_url = paste[8].text
        paste_hits = paste[9].text

        if paste_key is None:
            raise PaspybinParseError("paste_key value not found")
        elif paste_date is None:
            raise PaspybinParseError("paste_date value not found")
        elif paste_size is None:
            raise PaspybinParseError("paste_size value not found")
        elif paste_expire_date is None:
            raise PaspybinParseError("paste_expire_date value not found")
        elif paste_private is None:
            raise PaspybinParseError("paste_private value not found")
        elif paste_format_short is None:
            raise PaspybinParseError("paste_format_short value not found")
        elif paste_url is None:
            raise PaspybinParseError("paste_url value not found")
        elif paste_hits is None:
            raise PaspybinParseError("paste_hits value not found")

        yield Paste(
            paste_key,
            datetime.fromtimestamp(int(paste_date)),
            paste_title,
            int(paste_size),
            datetime.fromtimestamp(int(paste_expire_date)),
            Visibility(int(paste_private)),
            Format(paste_format_short),
            paste_url,
            int(paste_hits),
        )


def parse_user(data: str) -> User:
    """
    Parse user xml string.

    Args:
        data: str of user xml

    Returns:
        A `User` schema.

    Raises:
        PaspybinParseError: if one or more required fields are not found.

    Examples:
    >>> data = (
    ...     "<user>"
    ...     "<user_name>wiz_kitty</user_name>"
    ...     "<user_format_short>text</user_format_short>"
    ...     "<user_expiration>N</user_expiration>"
    ...     "<user_avatar_url>https://pastebin.com/cache/a/1.jpg</user_avatar_url>"
    ...     "<user_private>1</user_private>"
    ...     "<user_website>https://myawesomesite.com</user_website>"
    ...     "<user_email>oh@dear.com</user_email>"
    ...     "<user_location>New York</user_location>"
    ...     "<user_account_type>1</user_account_type>"
    ...     "</user>"
    ... )
    >>> user = parse_user(data)
    >>> user
    User(...)

    Note:
        `user_website` and `user_location` is optional.
    """
    user: Element = fromstring(data)

    if len(user) < 9:
        raise PaspybinParseError("one or more fields not found")

    user_name = user[0].text
    user_format_short = user[1].text
    user_expiration = user[2].text
    user_avatar_url = user[3].text
    user_private = user[4].text
    user_website = user[5].text
    user_email = user[6].text
    user_location = user[7].text
    user_account_type = user[8].text

    if user_name is None:
        raise PaspybinParseError("user_name value not found")
    elif user_format_short is None:
        raise PaspybinParseError("user_format_short value not found")
    elif user_expiration is None:
        raise PaspybinParseError("user_expiration value not found")
    elif user_avatar_url is None:
        raise PaspybinParseError("user_avatar_url value not found")
    elif user_private is None:
        raise PaspybinParseError("user_private value not found")
    elif user_email is None:
        raise PaspybinParseError("user_email value not found")
    elif user_account_type is None:
        raise PaspybinParseError("user_account_type value not found")

    return User(
        user_name,
        Format(user_format_short),
        Expire(user_expiration),
        user_avatar_url,
        Visibility(int(user_private)),
        user_website,
        user_email,
        user_location,
        Type(int(user_account_type)),
    )
