#!/usr/bin/env python
import subprocess
from argparse import ArgumentParser
from pathlib import Path

def main():
    p = ArgumentParser()
    p.add_argument('path',help='path to examine with Linguist',nargs='?',default='.')
    p.add_argument('-v','--verbose', action='store_true')
    p = p.parse_args()

    path = Path(p.path).expanduser()

    V = '--breakdown' if p.verbose else ''

    ret = subprocess.check_output(['linguist', str(path), V], universal_newlines=True)

    print(ret)

if __name__ == '__main__':
    main()