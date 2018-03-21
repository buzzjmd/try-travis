# -*- coding: utf-8 -*-

"""Platform hello module."""

import platform


def get_hello():
    _system = platform.system()
    if _system == "Windows":
        return "Hello Windows!"
    elif _system == "Darwin":
        return "Hello Mac OSX!"
    else:
        return "Hello {}!".format(_system)
