#!/usr/bin/env python3
"""gets value from dictionary."""
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """returns value safely gotten from dict
    """
    if key in dct:
        return dct[key]
    else:
        return default