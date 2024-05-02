#!/usr/bin/env python3
'''validates module.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''develop a multiplier functions.
    '''
    return lambda x: x * multiplier
