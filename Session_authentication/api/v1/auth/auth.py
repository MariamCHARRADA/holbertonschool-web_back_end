#!/usr/bin/env python3
"""authentication module"""

from flask import request
from typing import List, TypeVar
import os


class Auth:
    """class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """determines if the path requires authentication"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != "/":
            path += "/"
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """retrieves auth header from the request"""
        if request is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar("User"):
        """retrieves the current user from the request"""
        return None

    def session_cookie(self, request=None):
        """returns a cookie value from a request"""
        if request is None:
            return None
        session_name = os.getenv("SESSION_NAME")
        return request.cookies.get(session_name)
