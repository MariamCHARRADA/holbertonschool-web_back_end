#!/usr/bin/env python3
""" function that encrypts passwords"""

import bcrypt


def hash_password(password: str) -> bytes:
    """encrypts a password"""
    p_bytes = password.encode()
    return bcrypt.hashpw(p_bytes, bcrypt.gensalt())
