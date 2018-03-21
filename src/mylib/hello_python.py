# -*- coding: utf-8 -*-

"""Python hello module."""

import sys


def get_hello():
    if sys.version_info.major < 3:
        return "Hello Python2 or earlier!"
    else:
        return "Hello Python3 or later!"
