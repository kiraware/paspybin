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
    """

    key: PasteKey
    date: datetime
    title: str | None
    size: int
    expire_date: datetime
    private: Visibility
    format: Format
    url: PastebinUrl
    hits: int
