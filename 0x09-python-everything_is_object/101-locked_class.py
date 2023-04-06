#!/usr/bin/python3
# 101-locked_class.py
"""this defines a locked class"""

class LockedClass:
    class LockedClass:
    """
    this code stops the user from instantiating new LockedClass attributes for anything except attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
