# -*- coding: utf-8 -*-

"""Hello from python module."""

import sys


def get_hello_from_python():
    if sys.version_info.major < 3:
        # Python 2 or earlier
        return "Hello! I'm Python2 or earlier."
    else:
        # Python 3 or later
        return "Hello! I'm at least Python3."
