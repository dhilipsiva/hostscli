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
from hostscli.cli import websites


def test_hostscli():
    runner = CliRunner()
    result = runner.invoke(websites)
    print(result.output)
    print(dir(result))
    assert 1 == 0
    assert result.exit_code == 0


test_hostscli()
