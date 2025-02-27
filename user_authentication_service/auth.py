#!/usr/bin/env python3
"""Auth module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash a password using bcrypt"""
    password_bytes = password.encode("utf-8")

    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

    return hashed_password
