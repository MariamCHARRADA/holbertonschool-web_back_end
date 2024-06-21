#!/usr/bin/env python3
""" function that encrypts passwords"""

import bcrypt

def hash_password(password: str) -> bytes:
    """encrypts a password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
