#!/usr/bin/env python3
"""measure the runtime"""
import time
import asyncio
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """function that measures the total execution time"""
    start = time.time()
    for _ in range(n):
        asyncio.run(wait_n(1, max_delay))
    end = time.time()
    runtime = end - start
    return runtime / n
