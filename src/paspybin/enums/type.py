"""
Module to store an int enum class representation account type.
"""

from enum import IntEnum

__all__ = ["Type"]


class Type(IntEnum):
    """
    An int enum class that define valid account type.

    Attributes:
        NORMAL: `0`
        PRO: `1`

    Examples:
        >>> Type(0)
        <Type.NORMAL: 0>
        >>> Type["NORMAL"]
        <Type.NORMAL: 0>
        >>> Type.NORMAL
        <Type.NORMAL: 0>
        >>> Type.NORMAL == 0
        True
        >>> print(Type.NORMAL)
        0
    """

    NORMAL: int = 0
    PRO: int = 1
