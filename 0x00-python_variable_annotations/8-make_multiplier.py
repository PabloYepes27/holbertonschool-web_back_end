#!/usr/bin/env python3
""" File that contains a make_multiplier function """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Function that returns a function that multiplies two floats

        Args:
            multiplier (float): a float number

        Return:
            Callable[[float], float]: function that multiplies a float by multiplier.
    """
    return lambda n: n * multiplier
