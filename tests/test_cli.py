#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: test.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-12-29
"""

from click.testing import CliRunner
from hostscli.constants import HOSTS_FILE
from hostscli.constants import TEST_WEBSITE, TEST_LINE
from hostscli.cli import websites, block, unblock, block_all, unblock_all

runner = CliRunner()


def test_websites():
    result = runner.invoke(websites)
    assert TEST_WEBSITE in result.output
    assert result.exit_code == 0


def test_block():
    """
    Test Blocking a website
    """
    result = runner.invoke(block, [TEST_WEBSITE])
    assert TEST_LINE in open(HOSTS_FILE).read()
    assert result.exit_code == 0


def test_unblock():
    """
    Test Blocking a website
    """
    result = runner.invoke(unblock, [TEST_WEBSITE])
    assert TEST_LINE not in open(HOSTS_FILE).read()
    assert result.exit_code == 0


def test_block_all():
    """
    Test Blocking a website
    """
    result = runner.invoke(block_all)
    assert TEST_LINE in open(HOSTS_FILE).read()
    assert result.exit_code == 0


def test_unblock_all():
    """
    Test Blocking a website
    """
    result = runner.invoke(unblock_all)
    assert TEST_LINE not in open(HOSTS_FILE).read()
    assert result.exit_code == 0
