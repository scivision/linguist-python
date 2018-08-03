import subprocess
from typing import List, Tuple, Union
from pathlib import Path


def linguist(path: Path, rtype: bool=False) -> Union[str, List[Tuple[str, str]]]:

    ret = subprocess.check_output(['linguist', str(path)],
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
