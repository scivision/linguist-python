import subprocess
from typing import List, Tuple
from pathlib import Path


def linguist(path: Path, verbose: bool) -> List[Tuple[str, str]]:
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