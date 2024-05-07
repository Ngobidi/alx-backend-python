#!/usr/bin/env python3
'''validates sequence module.
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''reproduce a sequence of 10 nums.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
