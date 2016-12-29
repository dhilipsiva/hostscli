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
