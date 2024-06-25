#!/usr/bin/env python3
"""auth.py"""

from flask import request
from typing import List, TypeVar


class Auth:
    """class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """determines if the path requires authentication"""
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """retrieves auth header from the request"""
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """retrieves the current user from the request"""
        return None
