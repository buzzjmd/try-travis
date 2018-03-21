# -*- coding: utf-8 -*-

"""Hello module tests."""

import platform
import sys

from mylib.hello import get_hello


def test_get_hello():
    system = platform.system()
    if sys.version_info.major < 3:
        python = 'Python2 or earlier'
    else:
        python = 'Python3 or later'
    assert get_hello() == "Hello {system}, I'm {python}!".format(
        system='Mac OSX' if system == 'Darwin' else system,
        python=python)
