# -*- coding: utf-8 -*-

"""Python specific tests."""


def test_python_versions():
    """Test Pythons.

    Use this test to check coverage,
    i.e. make sure both python2 and python3 have been tested.
    """
    import sys
    if sys.version_info.major < 3:
        # Python 2 or earlier
        assert sys.version_info.major < 3
    else:
        # Python 3 or later
        assert sys.version_info.major >= 3


def test_platforms():
    """Test Platforms.

    Use this test to check coverage,
    i.e. make sure both windows and linux have been tested.
    """
    import platform
    _platform = platform.system()
    if _platform == "Windows":
        assert _platform == "Windows"
    elif _platform == "Darwin":
        assert _platform == "Darwin"
    else:
        assert _platform == "Linux"
