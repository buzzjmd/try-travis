# -*- coding: utf-8 -*-

"""Hello world module tests."""

import mylib.hello


def test_get_hello():
    assert mylib.hello.get_hello() == "Hello world!"
