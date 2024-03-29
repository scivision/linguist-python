# linguist-python

![ci](https://github.com/scivision/linguist-python/workflows/ci/badge.svg)
[![pypi versions](https://img.shields.io/pypi/pyversions/ghlinguist.svg)](https://pypi.python.org/pypi/ghlinguist)
[![PyPi Download stats](http://pepy.tech/badge/ghlinguist)](http://pepy.tech/project/ghlinguist)

Pure Python command-line wrapper of Ruby-based Github [Linguist](https://github.com/github/linguist).
Linguist detects the language of a Git repo based on the `commit`ed files.
The repo file
[.gitattributes](https://github.com/github/linguist#using-gitattributes)
is used to configure Linguist to not get distracted by `docs` or archive files, etc. using several straightforward rules.

This Python wrapper makes Linguist more intuitive by warning users of uncommitted changes or additions that could make Linguist silently give inaccurate results, since Linguist only works on files that have been `git commit`ed.

## Install

Ruby is required for Linguist:

* Windows: Windows Subsystem for Linux is recommended.
* Linux: see Notes section at bottom of this README
* MacOS / Linux Homebrew: `brew install ruby`

1. Install Linguist as usual:

   ```sh
   gem install github-linguist
   ```
2. Install this Python wrapper:

   ```sh
   pip install ghlinguist
   ```

## Usage

From Terminal:

```sh
python -m ghlinguist
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
python -m ghlinguist -t
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
   apt install --no-install-recommends ruby-dev libssl-dev libicu-dev zlib1g-dev libcurl4-openssl-dev

   gem update --system
   ```
2. be sure Gems are installed to home directory, NOT system (no sudo) by adding to `~/.bashrc`:

   ```sh
   # Install Ruby Gems to ~/gems
   export GEM_HOME=$HOME/gems
   export PATH=$HOME/gems/bin:$PATH
   ```
