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

from unittest import TestCase

from click.testing import CliRunner
from hostscli.constants import HOSTS_FILE
from hostscli.constants import TEST_WEBSITE, TEST_LINE
from hostscli.cli import websites, block, unblock, block_all, unblock_all

runner = CliRunner()


class TestUtils(TestCase):
    """
    Test cli.py
    """
    def setUp(self):
        """
        Initialize the CLIRunner
        """

    def test_websites(self):
        result = runner.invoke(websites)
        self.assertIn(TEST_WEBSITE, result.output)
        self.assertEqual(result.exit_code, 0)

    def test_block(self):
        """
        Test Blocking a website
        """
        result = runner.invoke(block, [TEST_WEBSITE])
        self.assertIn(TEST_LINE, open(HOSTS_FILE).read())
        self.assertEqual(result.exit_code, 0)

    def test_unblock(self):
        """
        Test Blocking a website
        """
        result = runner.invoke(unblock, [TEST_WEBSITE])
        self.assertNotIn(TEST_LINE, open(HOSTS_FILE).read())
        self.assertEqual(result.exit_code, 0)

    def test_block_all(self):
        """
        Test Blocking a website
        """
        result = runner.invoke(block_all)
        self.assertIn(TEST_LINE, open(HOSTS_FILE).read())
        self.assertEqual(result.exit_code, 0)

    def test_unblock_all(self):
        """
        Test Blocking a website
        """
        result = runner.invoke(unblock_all)
        self.assertNotIn(TEST_LINE, open(HOSTS_FILE).read())
        self.assertEqual(result.exit_code, 0)
