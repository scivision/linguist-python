#!/usr/bin/env python
from argparse import ArgumentParser
from pathlib import Path
import ghlinguist as ghl


def main():
    p = ArgumentParser()
    p.add_argument('path', help='path to examine with GitHub Linguist',
                   nargs='?', default='.')
    p = p.parse_args()

    langs = ghl.linguist(Path(p.path).expanduser())

    for l in langs:
        print(f'{l[0]} {l[1]}%')


if __name__ == '__main__':
    main()
