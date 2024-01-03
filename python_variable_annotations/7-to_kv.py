#!/usr/bin/env python3
"""returns a tuple of key and square of value"""
from typing import Tuple


def to_kv(k: str, v: int | float) -> Tuple[str,float]:
    """returns a tuple of key and square of value"""
    return (k, v**2)
