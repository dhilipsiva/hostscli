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

from hostscli.constants import HOSTS_FILE
from hostscli.utils import get_websites, get_lines, block, unblock

TEST_WEBSITE = 'test'
TEST_LINE = '127.0.0.1 test.com\n'


def test_get_websites():
    """
    Test listing supported websites
    """
    websites = get_websites()
    assert TEST_WEBSITE in websites


def test_get_lines():
    """
    Test if its getting domains from file
    """
    lines = get_lines(TEST_WEBSITE)
    assert TEST_LINE in lines


def test_block_unblock():
    """
    Test blocking and unblocking websites
    """
    block(TEST_WEBSITE)
    assert TEST_LINE in open(HOSTS_FILE).read()
    unblock(TEST_WEBSITE)
    assert TEST_LINE not in open(HOSTS_FILE).read()
