.. HostsCLI documentation master file, created by
   sphinx-quickstart on Sat Jan 14 12:09:30 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to HostsCLI's documentation!
====================================

A CLI tool to block / unblock websites using /etc/hosts. Super simple and easily extendable.

.. start-badges

.. list-table::
    :stub-columns: 1

    * - Docs
      - |docs|
    * - GitHub
      - | |gh-issues| |gh-forks| |gh-stars| |gh-license|
    * - Tests
      - | |travis| |requires|  |coverage| |code-climate| |cc-issues|
    * - Thanks
      - |say-thanks|

.. |docs| image:: https://readthedocs.org/projects/hostscli/badge/?version=latest
    :target: http://hostscli.readthedocs.io/?badge=latest
    :alt: Documentation Status

.. |gh-issues| image:: https://img.shields.io/github/issues/dhilipsiva/hostscli.svg
    :target: https://github.com/dhilipsiva/hostscli/issues
    :alt: GitHub Issues

.. |gh-forks| image:: https://img.shields.io/github/forks/dhilipsiva/hostscli.svg
    :target: https://github.com/dhilipsiva/hostscli/network
    :alt: GitHub Forks

.. |gh-stars| image:: https://img.shields.io/github/stars/dhilipsiva/hostscli.svg
    :target: https://github.com/dhilipsiva/hostscli/stargazers
    :alt: GitHub Stars

.. |gh-license| image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://raw.githubusercontent.com/dhilipsiva/hostscli/master/LICENSE
    :alt: GitHub LICENSE

.. |travis| image:: https://travis-ci.org/dhilipsiva/hostscli.svg?branch=master
    :target: https://travis-ci.org/dhilipsiva/hostscli
    :alt: Travis

.. |requires| image:: https://requires.io/github/dhilipsiva/hostscli/requirements.svg?branch=master
    :target: https://requires.io/github/dhilipsiva/hostscli/requirements/?branch=master
    :alt: Requirements Status

.. |coverage| image:: https://codecov.io/gh/dhilipsiva/hostscli/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/dhilipsiva/hostscli
    :alt: Coverage

.. |code-climate| image:: https://codeclimate.com/github/dhilipsiva/hostscli/badges/gpa.svg
    :target: https://codeclimate.com/github/dhilipsiva/hostscli
    :alt: Code Climate

.. |cc-issues| image:: https://codeclimate.com/github/dhilipsiva/hostscli/badges/issue_count.svg
    :target: https://codeclimate.com/github/dhilipsiva/hostscli
    :alt: Issue Count

.. |say-thanks| image:: https://img.shields.io/badge/saythanks.io-%E2%98%BC-1EAEDB.svg
    :target: https://saythanks.io/to/dhilipsiva
    :alt: Say thanks :)

.. end-badges

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


Installation
============


    pip install -U hostscli


Usage
=====

**Please note that we require `sudo` permissions to change `/etc/hosts` file**

To block ``facebook``:

``sudo hostscli block facebook
sudo hostscli block facebook,youtube  # To block multiple sites``

To unblock ``facebook``:

``sudo hostscli unblock facebook
sudo hostscli unblock facebook,youtube  # To unblock multiple sites``

To list supported websites:

``hostscli websites``

To Block all supported websites:

``sudo hostscli block_all
sudo hostscli block_all -i facebook,youtube  # To ignore some sites when blocking``

To Unblock all supported websites:

``sudo hostscli unblock_all
sudo hostscli unblock_all -i facebook,youtube  # To ignore some sites when unblocking``

More websites?
=============

If you need to add more websites, just create a ``<website>.py`` file in `hostscli/websites/ <https://github.com/dhilipsiva/hostscli/tree/master/hostscli/websites>`_ directory with list of domains declared as variable `DOMAINS`.
Please look at `hostscli/websites/facebook.py <https://github.com/dhilipsiva/hostscli/blob/master/hostscli/websites/facebook.py>`_ file for reference
