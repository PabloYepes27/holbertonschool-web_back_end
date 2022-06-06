#!/usr/bin/env python3
""" File that contains a sum_mixed_list function """

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        Function that return a string and a squared number

        Args:
            k (str): a random string
            v (Union[int, float]): number to be squared

        Returns:
            Tuple[str, float]: _description_
    """
    return (k, v**2)
