# YAAB - Yet another automation base #

An easy to maintenance automation base for web based end-to-end tests.

This base is using py.test framework, for an easy xml report (that later can be used by any CI).
For any other purpose it's possible to just run as a regular Unittest.

The env is setup by default to work on a headless browser in the same instance,
to change this for mobilefarm or any other selenium-hub based env please see the last section in this README.

I've attached a demo test for a search of the term "Hummus" in DuckDuckGo.
(guess it's easy and yummy enough as an example)

## Installation

1. Clone the repo to an ubuntu based aws-ec2 instance.
2. Install XVFB: sudo apt-get install xvfb (for headless testing)
3. Download and install Google Chrome:
```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
```
4. Run init.sh for initialize dependencies:
```bash
chomod +x init.sh
./init.sh
```


## How to use cloud base mobile farm\Selenium Hub:

1. Edit utils/base.py.
2. See func 'create_driver'.
3. Rewrite command_executor for remote webdriver.


## Credits

Gilad Maoz - gilad@maoz.info