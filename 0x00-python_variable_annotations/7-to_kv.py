#!/usr/bin/env python3
'''validates module.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Conversion of a keys' values to a tuple of the key and
    the square of its values.
    '''
    return (k, float(v**2))
