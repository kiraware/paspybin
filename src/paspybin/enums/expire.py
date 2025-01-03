"""
Module to store a str enum class representation of expire date.
"""

from enum import StrEnum

__all__ = ["Expire"]


class Expire(StrEnum):
    """
    A str enum class that define valid expiration date.

    Attributes:
        NEVER (str): `"N"`, never expire
        TEN_MINUTES (str): `"10M"`, expire after ten minutes
        ONE_HOUR (str): `"1H"`, expire after one hour
        ONE_DAY (str): `"1D"`, expire after one day
        ONE_WEEK (str): `"1W"`, expire after one week
        TWO_WEEKS (str): `"2W"`, expire after two weeks
        ONE_MONTH (str): `"1M"`, expire after one month
        SIX_MONTHS (str): `"6M"`, expire after six month
        ONE_YEAR (str): `"1Y"`, expire after one year

    Examples:
        >>> Expire("N")
        <Expire.NEVER: 'N'>
        >>> Expire["NEVER"]
        <Expire.NEVER: 'N'>
        >>> Expire.NEVER
        <Expire.NEVER: 'N'>
        >>> Expire.NEVER == "N"
        True
        >>> print(Expire.NEVER)
        N
    """

    NEVER = "N"
    TEN_MINUTES = "10M"
    ONE_HOUR = "1H"
    ONE_DAY = "1D"
    ONE_WEEK = "1W"
    TWO_WEEKS = "2W"
    ONE_MONTH = "1M"
    SIX_MONTHS = "6M"
    ONE_YEAR = "1Y"
