#!/usr/bin/env python3
"""sums_list task"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """return sum of floats in a given list
    """
    if input_list is None:
        return 0
    else:
        return sum(input_list)