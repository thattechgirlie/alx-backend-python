#!/usr/bin/env python3
"""Contains a function with annotated parameters"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    """Returns list of tuples with each elements length"""
    return [(i, len(i)) for i in lst]