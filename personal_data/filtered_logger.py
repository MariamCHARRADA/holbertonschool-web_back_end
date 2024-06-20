#!/usr/bin/env python3
""" function called filter_datum that returns the log message obfuscated"""

import re

def filter_datum(fields, redaction, message, separator):
    """returns the log message obfuscated"""
    for field in fields:
        pattern = rf"{field}=[^{re.escape(separator)}]*"
        replacement = f"{field}={redaction}"
        message = re.sub(pattern, replacement, message)
    return message
