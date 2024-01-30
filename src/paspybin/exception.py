__all__ = [
    "PaspybinError",
    "PaspybinBadAPIRequestError",
    "PaspybinNotFoundError",
    "PaspybinParseError",
]


class PaspybinError(Exception):
    """
    Paspybin general exception.
    """

    pass


class PaspybinBadAPIRequestError(PaspybinError):
    """
    Paspybin exception raised when a bad request occurs.
    """

    pass


class PaspybinNotFoundError(PaspybinError):
    """
    Paspybin exception raised when paste content is not found.
    """

    pass


class PaspybinParseError(PaspybinError):
    """
    Paspybin exception raised when the parser fails to parse.
    """

    pass
