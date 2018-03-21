# -*- coding: utf-8 -*-

"""Platform specific tests."""


def test_platform_system():
    """Test Platform Sysyem.

    Use this test to check coverage,
    i.e. make sure both windows, osx and linux have been tested.
    """
    import platform
    _system = platform.system()
    if _system == "Windows":
        assert _system == "Windows"
    elif _system == "Darwin":
        assert _system == "Darwin"
    else:
        assert _system == "Linux"
