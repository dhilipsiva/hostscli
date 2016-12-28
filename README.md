# hostscli

A CLI tool to block / unblock websites using /etc/hosts. Super simple and easily extendable.

## Installation

```
pip install -U hostscli
```

## Usage

*** Please note that we require `sudo` permissions to change `/etc/hosts` file ***

To block `facebook`:

```
sudo hostscli block facebook
```

To unblock `facebook`:

```
sudo hostscli block facebook
```

To list supported websites:

```
hostscli websites
```

## More websites?

If you need to add more websites, just create a `<website>.py` file in `hostscli/websites/` directory with list of domains declared as variable `DOMAINS`.
Please look at `hostscli/websites/facebook.py` file for reference
