#!/usr/bin/env python3
""" File that contains a sum_mixed_list function """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Function which takes a list of floats and integers
        and returns their sum as a float.

        Args:
            mxd_lst -> List[Union[int, float]]

        Return: sum of list the numbers
    """
    return sum(mxd_lst)
