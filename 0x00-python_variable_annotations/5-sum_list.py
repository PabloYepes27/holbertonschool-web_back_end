#!/usr/bin/env python3
""" File that contains a sum_list function """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
        Function that returns the sum of the list elements

        Args:
            input_list (List[float]): list of float numbers

        Returns:
            float: sum of the list elements 
    """
    return sum(input_list)
