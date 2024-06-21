#!/usr/bin/env python3
""" function that encrypts passwords"""

from bcrypt import hashpw, gensalt


def hash_password(password: str) -> bytes:
    """encrypts a password"""
    return hashpw(password.encode(), gensalt())
