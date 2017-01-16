#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""



Installation
============

    pip install -U hostscli


Help
====

    Type `hostscli --help` to get a help on all the available commands


Usage
=====

**Please note that we require `sudo` permissions to change `/etc/hosts` file**

.. automodule:: hostscli.cli
    :members:
    :undoc-members:
    :show-inheritance:


Built-in utility functions
==========================

.. automodule:: hostscli.utils
    :members:
    :undoc-members:
    :show-inheritance:


Custom Errors
=============

.. automodule:: hostscli.errors
    :members:
    :undoc-members:
    :show-inheritance:


Special Lists
=============

I have compiles few special lists from various sources to block Ads, Tracking & Disturbing sites.

All the website list that starts with `list_` is a special list. So far, I have these lists:

1. list_ads -> Domains of known ad servers

2. list_malwares -> Domins that potentially have malwares

3. list_misc -> Sites that may have offensive / disturbing content.

These lists can be blocked / unblocked like you do with other websites
::
    $ sudo hostscli block list_ads


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

"""
