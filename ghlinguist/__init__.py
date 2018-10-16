import subprocess
import logging
from typing import List, Tuple, Union, Optional
from pathlib import Path
# takes too long to check if Linguist installed each time


def linguist(path: Path, rtype: bool=False) -> Optional[Union[str, List[Tuple[str, str]]]]:

    path = Path(path).expanduser()

    if not checkrepo(path):
        return None

    ret = subprocess.check_output(['github-linguist', str(path)],
                                  universal_newlines=True).split('\n')

# %% parse percentage
    lpct = []

    for i, line in enumerate(ret):
        L = line.split()
        if not L:  # EOF
            break
        lpct.append((L[1], L[0][:-1]))

    if rtype:
        return lpct[0][0]

    return lpct


def checkrepo(path: Path) -> bool:
    """basic check for healthy Git repo ready for Linguist to analyze"""

    path = Path(path).expanduser()

    if not (path / '.git').is_dir():
        logging.error(f'{path} does not seem to be a Git repository, and Linguist only works on files after "git commit"')
        return False

# %% detect uncommited (dirty)
    ret = subprocess.check_output(['git', 'status', '--porcelain'],
                                  cwd=path, universal_newlines=True)

    ADD = {'A', '?'}
    MOD = 'M'

    for line in ret.split('\n'):
        L = line.split()
        if not L:
            continue

        if ADD.intersection(L[0]) or (MOD in L[0] and L[1] == '.gitattributes'):
            logging.warning(f' {path} has uncommited changes: \n\n{ret}\n Linguist only works on files after "git commit"')
            return False

    return True
