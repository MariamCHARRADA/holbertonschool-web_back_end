#!/usr/bin/env python3
"""asynchronous generator that yields random numbers"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    async generator
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random()
