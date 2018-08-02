#!/usr/bin/env python
import subprocess
from argparse import ArgumentParser
from pathlib import Path
from typing import List, Tuple


def ling(path: Path, verbose: bool) -> List[Tuple[str, str]]:
    V = '--breakdown' if verbose else ''

    ret = subprocess.check_output(['linguist', str(path), V],
                                  universal_newlines=True)
# %% parse
    langs = []

    for line in ret.split('\n'):
        L = line.split()
        if not L:  # EOF
            break
        langs.append((L[1], L[0][:-1]))

    return langs


def main():
    p = ArgumentParser()
    p.add_argument('path', help='path to examine with Linguist',
                   nargs='?', default='.')
    p.add_argument('-v', '--verbose', action='store_true')
    p = p.parse_args()

    ling(Path(p.path).expanduser(), p.verbose)


if __name__ == '__main__':
    main()
