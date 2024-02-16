from dataclasses import dataclass

from ..enums import Expire, Format, Type, Visibility

__all__ = ["User"]


@dataclass(slots=True)
class User:
    """
    A schema used to store info about user.

    Attributes:
        name: name of user
        format: syntax highlighting format of user
        expiration: expire enum of user
        avatar_url: avatar url of user
        private: visibility of user
        website: website of user
        email: email of user
        location: location of user
        account_type: account type of user
    """

    name: str
    format: Format
    expiration: Expire
    avatar_url: str
    private: Visibility
    website: str | None
    email: str
    location: str | None
    account_type: Type
