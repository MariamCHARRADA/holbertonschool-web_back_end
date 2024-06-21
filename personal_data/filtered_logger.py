#!/usr/bin/env python3
""" function called filter_datum that returns the log message obfuscated"""

import logging
import mysql.connector
import os
import re
from typing import List

PII_FIELDS = (
    "name",
    "email",
    "phone",
    "ssn",
    "password",
)


class RedactingFormatter(logging.Formatter):
    """class that inherits from built-in logging.Formatter"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """initializes the RedactingFormatter"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """formats records and filters sensitive info"""
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR
        )
        return super().format(record)


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        pattern = f"{field}=[^{separator}]+"
        replacement = f"{field}={redaction}"
        message = re.sub(pattern, replacement, message)
    return message


def get_logger() -> logging.Logger:
    """logger function"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
