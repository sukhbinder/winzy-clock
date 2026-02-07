# winzy-clock

[![PyPI](https://img.shields.io/pypi/v/winzy-clock.svg)](https://pypi.org/project/winzy-clock/)
[![Changelog](https://img.shields.io/github/v/release/sukhbinder/winzy-clock?include_prereleases&label=changelog)](https://github.com/sukhbinder/winzy-clock/releases)
[![Tests](https://github.com/sukhbinder/winzy-clock/workflows/Test/badge.svg)](https://github.com/sukhbinder/winzy-clock/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/sukhbinder/winzy-clock/blob/main/LICENSE)

Matrix style clock

![](clock-demo.gif)

## Installation

First [install winzy](https://github.com/sukhbinder/winzy) by typing

```bash
pip install winzy
```

Then install this plugin in the same environment as your winzy application.
```bash
winzy install winzy-clock
```
## Usage

To get help type ``winzy  clock --help``

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd winzy-clock
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
