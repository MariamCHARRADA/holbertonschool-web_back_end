#!/usr/bin/env python3
"""awaits a random float and returns it"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """awaits a random float and returns it"""
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
