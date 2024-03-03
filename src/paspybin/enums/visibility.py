"""
Module to store an int enum class representation visibility.
"""

from enum import IntEnum

__all__ = ["Visibility"]


class Visibility(IntEnum):
    """
    An int enum class that define valid visibility.

    Attributes:
        PUBLIC: `0`
        UNLISTED: `1`
        PRIVATE: `2`

    Examples:
        >>> Visibility(0)
        <Visibility.PUBLIC: 0>
        >>> Visibility["PUBLIC"]
        <Visibility.PUBLIC: 0>
        >>> Visibility.PUBLIC
        <Visibility.PUBLIC: 0>
        >>> Visibility.PUBLIC == 0
        True
        >>> print(Visibility.PUBLIC)
        0
    """

    PUBLIC: int = 0
    UNLISTED: int = 1
    PRIVATE: int = 2
