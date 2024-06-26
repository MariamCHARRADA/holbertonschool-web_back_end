#!/usr/bin/env python3
"""basic authentication module"""

from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Authentication class"""

    pass
