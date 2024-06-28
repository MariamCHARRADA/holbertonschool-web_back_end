#!/usr/bin/env python3
"""session authentication module"""

import base64
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """session Authentication class"""

    pass
