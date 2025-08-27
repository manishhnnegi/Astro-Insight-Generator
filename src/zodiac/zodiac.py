"""
zodiac.py

Module to determine a person's zodiac sign based on birth date.

Classes
-------
Zodiac
    Provides a method to infer the zodiac sign from a given date string.
"""

from datetime import datetime


class Zodiac:
    """
    Class to determine the zodiac sign from a birth date.

    Attributes
    ----------
    ZODIAC_DATES : list[tuple[str, tuple[int, int], tuple[int, int]]]
        List of zodiac signs with their start and end dates.
        Each entry is a tuple of:
        - Zodiac name (str)
        - Start date (month, day)
        - End date (month, day)
    """

    ZODIAC_DATES = [
        ("Capricorn", (1, 1), (1, 19)),
        ("Aquarius", (1, 20), (2, 18)),
        ("Pisces", (2, 19), (3, 20)),
        ("Aries", (3, 21), (4, 19)),
        ("Taurus", (4, 20), (5, 20)),
        ("Gemini", (5, 21), (6, 20)),
        ("Cancer", (6, 21), (7, 22)),
        ("Leo", (7, 23), (8, 22)),
        ("Virgo", (8, 23), (9, 22)),
        ("Libra", (9, 23), (10, 22)),
        ("Scorpio", (10, 23), (11, 21)),
        ("Sagittarius", (11, 22), (12, 21)),
        ("Capricorn", (12, 22), (12, 31)),
    ]

    @classmethod
    def get_zodiac(cls, date_str: str) -> str:
        """
        Determine the zodiac sign for a given birth date.

        Parameters
        ----------
        date_str : str
            Birth date in the format 'YYYY-MM-DD'.

        Returns
        -------
        str
            The zodiac sign corresponding to the given date.
            Returns "Unknown" if the date does not match any zodiac range.

        Example
        -------
        >>> Zodiac.get_zodiac("1995-08-20")
        'Leo'
        """

        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        month, day = date_obj.month, date_obj.day
        for sign, (sm, sd), (em, ed) in cls.ZODIAC_DATES:
            if (month == sm and day >= sd) or (month == em and day <= ed):
                return sign
        return "Unknown"
