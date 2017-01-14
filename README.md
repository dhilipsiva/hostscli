# hostscli

A CLI tool to block / unblock websites using /etc/hosts. Super simple and easily extendable.

[![Build Status](https://travis-ci.org/dhilipsiva/hostscli.svg?branch=master)](https://travis-ci.org/dhilipsiva/hostscli)
[![codecov](https://codecov.io/gh/dhilipsiva/hostscli/branch/master/graph/badge.svg)](https://codecov.io/gh/dhilipsiva/hostscli)
[![Code Climate](https://codeclimate.com/github/dhilipsiva/hostscli/badges/gpa.svg)](https://codeclimate.com/github/dhilipsiva/hostscli)
[![Test Coverage](https://codeclimate.com/github/dhilipsiva/hostscli/badges/coverage.svg)](https://codeclimate.com/github/dhilipsiva/hostscli/coverage)
[![Issue Count](https://codeclimate.com/github/dhilipsiva/hostscli/badges/issue_count.svg)](https://codeclimate.com/github/dhilipsiva/hostscli)
[![Requirements Status](https://requires.io/github/dhilipsiva/hostscli/requirements.svg?branch=master)](https://requires.io/github/dhilipsiva/hostscli/requirements/?branch=master)


## Installation

```
pip install -U hostscli
```

## Usage

*** Please note that we require `sudo` permissions to change `/etc/hosts` file ***

To block `facebook`:

```
sudo hostscli block facebook
sudo hostscli block facebook,youtube  # To block multiple sites
```

To unblock `facebook`:

```
sudo hostscli unblock facebook
sudo hostscli unblock facebook,youtube  # To unblock multiple sites
```

To list supported websites:

```
hostscli websites
```

To Block all supported websites:

```
sudo hostscli block_all
sudo hostscli block_all -i facebook,youtube  # To ignore some sites when blocking
```

To Unblock all supported websites:

```
sudo hostscli unblock_all
sudo hostscli unblock_all -i facebook,youtube  # To ignore some sites when unblocking
```

## More websites?

If you need to add more websites, just create a `<website>.py` file in `hostscli/websites/` directory with list of domains declared as variable `DOMAINS`.
Please look at [`hostscli/websites/facebook.py`](https://github.com/dhilipsiva/hostscli/blob/master/hostscli/websites/facebook.py) file for reference
