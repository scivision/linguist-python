#!/usr/bin/env python
from argparse import ArgumentParser
import ghlinguist as ghl


def main():
    p = ArgumentParser()
    p.add_argument('path', help='path to examine with GitHub Linguist', nargs='?', default='.')
    p.add_argument('-t', '--type', help='print only detected repo type (as GitHub would declare)', action='store_true')
    p = p.parse_args()

    langs = ghl.linguist(p.path, rtype=p.type)

    if isinstance(langs, str):
        print(langs)
    elif isinstance(langs, list):
        for l in langs:
            print(f'{l[0]} {l[1]}%')


if __name__ == '__main__':
    main()
