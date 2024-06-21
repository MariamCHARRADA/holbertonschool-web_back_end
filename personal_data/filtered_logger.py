#!/usr/bin/env python3
""" function called filter_datum that returns the log message obfuscated"""

import re
from typing import List
import logging


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        pattern = f"{field}=[^{separator}]+"
        replacement = f"{field}={redaction}"
        message = re.sub(pattern, replacement, message)
    return message
