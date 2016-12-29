#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: constants.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-12-29
"""

HOSTS_FILE = '/etc/hosts'
FORMAT = '127.0.0.1 %s\n'
WEBSITES_PACKAGE = 'hostscli.websites'

IMPORT_ERROR = """

No Domain list found for website: %s

Please raise a Issue here: https://github.com/dhilipsiva/hostscli/issues/new
if you think we should add domains for this website.

type `hostscli websites` to see a list of websites that you can block/unblock


"""

ROOT_ERROR = """

"sudo" permissions are required to run this command.

Please run the last command again with sudo

"""
