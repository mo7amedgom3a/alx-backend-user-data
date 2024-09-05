#!/usr/bin/env python3
"""
Module for authentication
"""


from typing import List, TypeVar
from flask import request


class Auth:
    """_summary_
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """_summary_

        Args:
                path (str): _description_
                excluded_paths (List[str]): _description_

        Returns:
                bool: _description_
        """
        if path is None or excluded_paths is None:
            return True
        check = path.endswith('/')
        if path in excluded_paths:
            return False
        if check:
            path = path[:-1]
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self) -> str:
        """_summary_

        Returns:
                str: _description_
        """
        return None

    def current_user(self) -> TypeVar('User'):
        """_summary_

        Returns:
                TypeVar('User'): _description_
        """
        return None
