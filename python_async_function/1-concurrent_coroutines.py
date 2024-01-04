#!/usr/bin/env python3
"""function that calls wait_random n times"""
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """function that calls wait_random n times"""
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
