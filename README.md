[![Build Status](https://travis-ci.com/scivision/linguist-python.svg?branch=master)](https://travis-ci.com/scivision/linguist-python)
[![Coverage Status](https://coveralls.io/repos/github/scivision/linguist-python/badge.svg?branch=master)](https://coveralls.io/github/scivision/linguist-python?branch=master)
[![Build status](https://ci.appveyor.com/api/projects/status/95502ny5y0bsy8ll?svg=true)](https://ci.appveyor.com/project/scivision/linguist-python)

# linguist-python
Simple command-line wrapper of Ruby-based Github Linguist

## Install

1. Install Linguist as usual:
   ```sh
   gem install github-linguist
   ```
2. Install Python wrapper:
   ```sh
   pip install -e .
   ```

## Usage
From Terminal:
```
ghlinguist
```

Or import as a Python module.
```python
import ghlinguist as ghl

langs = ghl.linguist('~/mypath')
```
The functions return a list of tuples like:
```
[('Python'), (97.)]
[('Fortran'), (3.)]
```
where the second number is the percentage of code detected for that language.

## Notes
ghLinguist parses text output from 
[GitHub Linguist](https://github.com/github/linguist#using-emacs-or-vim-modelines), 
which is a Ruby program.


### Linux prereqs
If you don't already have RubyGems setup on Linux:

1. setup RubyGems:
   ```sh
   apt install ruby-dev libssl-dev libicu-dev zlib1g-dev libcurl4-openssl-dev
   
   gem update --system
   ```
2. be sure Gems are installed to home directory, NOT system (no sudo) by adding to `~/.bashrc`:
   ```sh
   # Install Ruby Gems to ~/gems
   export GEM_HOME=$HOME/gems
   export PATH=$HOME/gems/bin:$PATH
   ```

