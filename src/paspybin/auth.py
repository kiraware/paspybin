from dataclasses import dataclass

__all__ = ["Login"]


@dataclass(slots=True)
class Login:
    """
    Class to store credentials for login.

    Attributes:
        username: username of user.
        password: password of user.
    """

    username: str
    password: str
