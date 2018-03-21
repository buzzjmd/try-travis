# -*- coding: utf-8 -*-

"""Python specific tests."""

import sys

from mylib.hello_python import get_hello


def test_python_versions():
    """Test Pythons.

    Use this test to check coverage,
    i.e. make sure both python2 and python3 have been tested.
    """
    if sys.version_info.major < 3:
        assert get_hello() == "Hello Python2 or earlier!"
    else:
        assert get_hello() == "Hello Python3 or later!"
