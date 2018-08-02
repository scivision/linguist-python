#!/usr/bin/env python
from argparse import ArgumentParser
from pathlib import Path
import pylinguist as pl


def main():
    p = ArgumentParser()
    p.add_argument('path', help='path to examine with Linguist',
                   nargs='?', default='.')
    p.add_argument('-v', '--verbose', action='store_true')
    p = p.parse_args()

    langs = pl.linguist(Path(p.path).expanduser(), p.verbose)

    for l in langs:
        print(f'{l[0]} {l[1]}%')


if __name__ == '__main__':
    main()
