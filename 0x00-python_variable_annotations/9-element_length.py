#!/usr/bin/env python3
'''validates module.
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''evaluates the len of a list of sequences.
    '''
    return [(a, len(a)) for a in lst]
