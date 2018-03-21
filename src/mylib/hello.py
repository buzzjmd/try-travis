# -*- coding: utf-8 -*-

"""Hello module."""

import platform
import sys


def get_hello():
    system = platform.system()
    py_version = sys.version_info.major

    if system == "Windows":
        if py_version < 3:
            return "Hello Windows, I'm Python2 or earlier!"
        else:
            return "Hello Windows, I'm Python3 or later!"
    elif system == "Darwin":
        if py_version < 3:
            return "Hello Mac OSX, I'm Python2 or earlier!"
        else:
            return "Hello Mac OSX, I'm Python3 or later!"
    else:
        if py_version < 3:
            return "Hello {}, I'm Python2 or earlier!".format(system)
        else:
            return "Hello {}, I'm Python3 or later!".format(system)
