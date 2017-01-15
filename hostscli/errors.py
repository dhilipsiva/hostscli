#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
Some custom utility functions that we use
"""


class HostsCLIException(Exception):
    """
    A Custom Exception class
    """


class WebsiteImportError(HostsCLIException):
    """
    An error to raise when no Domain list found for given website
    """


class SudoRequiredError(HostsCLIException):
    """
    An error raised when the given hosts files is not writable.
    "sudo" permissions are required to run this command.
    """
