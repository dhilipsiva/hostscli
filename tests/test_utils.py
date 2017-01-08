#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: test_utils.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2017-01-08
"""


from hostscli.utils import sudo_required
from hostscli.errors import SudoRequiredError


def test_sudo_required():
    """
    Test Sudo required
    """

    @sudo_required
    def dummy_fuction():
        assert True

    try:
        dummy_fuction('test')
    except SudoRequiredError:
        assert True
    else:
        assert False
