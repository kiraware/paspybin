from dataclasses import dataclass
from datetime import datetime

from ..enums import Format, Visibility
from ..types import PastebinUrl, PasteKey

__all__ = ["Paste"]


@dataclass(slots=True)
class Paste:
    """
    A schema used to store info about paste.

    Attributes:
        key: key of paste
        date: created date of paste
        title: title of paste
        size: size of paste
        expire_date: expire date of paste
        private: visibility of paste
        format: syntax highlighting format of paste
        url: url location of paste
        hits: views count of paste

    Note:
        It is actually impossible for the fields `date`, `size`, `expire_date`,
        `private`,`format`, `url`, and `hits` to have the value `None` based on the API
        documentation, however, to make it easier to use the API wrapper so that it is
        more flexible, these fields are made so that they can contain the value `None`.
    """

    key: PasteKey
    date: datetime | None
    title: str | None
    size: int | None
    expire_date: datetime | None
    private: Visibility | None
    format: Format | None
    url: PastebinUrl | None
    hits: int | None
