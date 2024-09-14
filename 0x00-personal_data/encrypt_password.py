#!/usr/bin/env python3


""" bcrypt package to perform the hashing (with hashpw)."""
import bcrypt


def hash_password(password: str) -> bytes:
    """function that expects one string argument name password and
    returns a salted, hashed password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks is a hashed password was formed.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
