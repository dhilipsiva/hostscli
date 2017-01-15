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

from unittest import TestCase

from hostscli.constants import HOSTS_FILE
from hostscli.constants import TEST_WEBSITE, TEST_LINE
from hostscli.errors import WebsiteImportError, SudoRequiredError
from hostscli.utils import get_websites, get_lines, block, unblock


class TestUtils(TestCase):
    """
    Test utils.py
    """

    def test_get_websites(self):
        """
        Test listing supported websites
        """
        websites = get_websites()
        self.assertTrue(TEST_WEBSITE in websites)

    def test_get_lines(self):
        """
        Test if its getting domains from file
        """
        lines = get_lines(TEST_WEBSITE)
        self.assertTrue(TEST_LINE in lines)
        with self.assertRaises(WebsiteImportError):
            get_lines('a_website_that_does_not_exist')

    def test_block_unblock(self):
        """
        Test blocking and unblocking websites
        """
        block(TEST_WEBSITE)
        self.assertTrue(TEST_LINE in open(HOSTS_FILE).read())
        unblock(TEST_WEBSITE)
        self.assertFalse(TEST_LINE in open(HOSTS_FILE).read())
        with self.assertRaises(SudoRequiredError):
            block(TEST_WEBSITE, '/etc/hosts')
