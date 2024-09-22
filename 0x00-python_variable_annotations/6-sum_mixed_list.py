#!/usr/bin/env python3
"""
sum of mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sum of all the numbers in the list as float"""
    return sum(mxd_lst)