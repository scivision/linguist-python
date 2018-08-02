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
