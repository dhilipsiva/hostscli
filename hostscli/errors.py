#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: errors.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-12-29
"""


class HostsCLIException(Exception):
    """
    A Custom Exception class
    """


class WebsiteImportError(HostsCLIException):
    """
    No Domain list found for website
    """


class SudoRequiredError(HostsCLIException):
    """
    "sudo" permissions are required to run this command.
    """
