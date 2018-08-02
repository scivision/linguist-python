[![Build Status](https://travis-ci.com/scivision/linguist-python.svg?branch=master)](https://travis-ci.com/scivision/linguist-python)
[![Coverage Status](https://coveralls.io/repos/github/scivision/linguist-python/badge.svg?branch=master)](https://coveralls.io/github/scivision/linguist-python?branch=master)

# python-linguist
Simple command-line wrapper of Ruby-based Github Linguist

## Prereqs

Since we are merely parsing the original Linguist command-line output, we need to install Linguist as usual. Assuming Linux:

1. setup RubyGems:
   ```sh
   apt install ruby-dev libssl-dev
   
   gem update --system
   ```
2. be sure Gems are installed to home directory, NOT system (no sudo) by adding to `~/.bashrc`:
   ```sh
   # Install Ruby Gems to ~/gems
   export GEM_HOME=$HOME/gems
   export PATH=$HOME/gems/bin:$PATH
   ```
3. install Github Linguist:
   ```sh
   gem install github-linguist
   ```

## Install

```sh
pip install -e .
```
