# -*- coding: utf-8 -*-

"""Python specific tests."""

import sys

from mylib.hello_from_python import get_hello_from_python


def test_python_versions():
    """Test Pythons.

    Use this test to check coverage,
    i.e. make sure both python2 and python3 have been tested.
    """
    if sys.version_info.major < 3:
        # Python 2 or earlier
        assert sys.version_info.major < 3
        assert get_hello_from_python() == "Hello! I'm Python2 or earlier."
    else:
        # Python 3 or later
        assert sys.version_info.major >= 3
        assert get_hello_from_python() == "Hello! I'm at least Python3."
