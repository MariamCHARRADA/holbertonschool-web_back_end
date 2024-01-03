#!/usr/bin/env python3
"""returns a function that multiplies a float by another number"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by another number"""
    return lambda x: x * multiplier
