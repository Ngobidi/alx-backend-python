#!/usr/bin/env python3
'''validates module.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''compute the sums of a list of int and floating point num.
    '''
    return float(sum(mxd_lst))
