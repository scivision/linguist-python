[![Build Status](https://travis-ci.com/scivision/linguist-python.svg?branch=master)](https://travis-ci.com/scivision/linguist-python)
[![Coverage Status](https://coveralls.io/repos/github/scivision/linguist-python/badge.svg?branch=master)](https://coveralls.io/github/scivision/linguist-python?branch=master)
[![Build status](https://ci.appveyor.com/api/projects/status/95502ny5y0bsy8ll?svg=true)](https://ci.appveyor.com/project/scivision/linguist-python)
[![pypi versions](https://img.shields.io/pypi/pyversions/ghlinguist.svg)](https://pypi.python.org/pypi/ghlinguist)
[![PyPi Download stats](http://pepy.tech/badge/ghlinguist)](http://pepy.tech/project/ghlinguist)

# linguist-python
Simple Python command-line wrapper of Ruby-based Github Linguist.
[Linguist](https://github.com/github/linguist)
(and hence this Python wrapper) detect the language of a Git repo, based on the `commit`ed files
[`.gitattributes`](https://github.com/github/linguist#using-gitattributes) 
is used to configure Linguist to not get distracted by `docs` or archive files, etc. using several straightforward rules.

This Python wrapper attempts to make Linguist a little more careful by warning users of uncommitted changes or additions that could make Linguist silently give very skewed (inaccurate) results, since Linguist only works on files/changes *after* `git commit`.

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

If the directory is not a Git repo, `None` is returned

### Examples
The primary reason behind creating this Python Linguist wrapper is automatically detecting the repo type, so that appropriate templates can be applied *en masse* to a large number of repos.
Thus to get the repo language from the command line, as GitHub would:
```sh
ghlinguist -t
```

or as a Python module:
```python
import ghlinguist as ghl

lang = ghl.linguist('~/mypath', rpath=True)
```

Both cases simply return the string `Python` or `Fortran` etc.

## Notes
ghLinguist parses text output from 
[GitHub Linguist](https://github.com/github/linguist#using-emacs-or-vim-modelines), 
which is a Ruby program.
We call `github-linguist` executable since `linguist` overlaps with QT Lingiust.

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

