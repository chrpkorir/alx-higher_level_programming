#!/usr/bin/python3
"""Module 100-my_int.
Creates a class that inhrits from int.
"""


class MyInt(int):
    """Class inheriting from int,
    But reverses behaviour of == and !=
    """

    def __eq__(self, other):
        """Equal becomes inequal."""

        return super().__ne__(other)

    def __ne__(self, other):
        """Inequal becomes equal."""

        return super().__eq__(other)
