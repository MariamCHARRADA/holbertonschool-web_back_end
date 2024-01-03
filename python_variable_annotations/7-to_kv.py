#!/usr/bin/env python3
"""returns a tuple of key and square of value"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str,float]:
    """returns a tuple of key and square of value"""
    return (k, v**2)
