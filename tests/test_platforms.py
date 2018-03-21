# -*- coding: utf-8 -*-

"""Platform specific tests."""

import platform

from mylib.hello_platform import get_hello


def test_platform_system():
    """Test Platform Sysyem.

    Use this test to check coverage,
    i.e. make sure both windows, osx and linux have been tested.
    """
    _system = platform.system()
    if _system == "Windows":
        assert get_hello() == "Hello Windows!"
    elif _system == "Darwin":
        assert get_hello() == "Hello Mac OSX!"
    else:
        assert _system == "Linux"
        assert get_hello() == "Hello Linux!"
