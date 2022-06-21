#!/usr/bin/env python3
""" Module named auth to the class Auth """


from flask import request
from typing import List, TypeVar


class Auth():
    """Class to manage the API authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ public method that return false """
        if (
            path is None or excluded_paths is None or len(excluded_paths) == 0
        ):
            return True
        if (path[-1] != '/'):
            path += '/'
        for e in excluded_paths:
            if (e.endswith('*')):
                if (path.startswith(e[:1])):
                    return False
        return False if path in excluded_paths else True

    def authorization_header(self, request=None) -> str:
        """ Public method that return None.
            Args:
                request -> will be the Flask request object.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Public method that return None.
            Args:
                request -> will be the Flask request object.
        """
        return None
