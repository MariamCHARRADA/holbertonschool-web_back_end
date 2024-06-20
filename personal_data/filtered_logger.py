#!/usr/bin/env python3
""" function called filter_datum that returns the log message obfuscated"""

import re


def filter_datum(fields: list[str], redaction: str, message: str, separator: str):
    """returns the log message obfuscated"""
    for field in fields:
        pattern = f"{field}=[^{separator}]+"
        replacement = f"{field}={redaction}"
        message = re.sub(pattern, replacement, message)
    return message
