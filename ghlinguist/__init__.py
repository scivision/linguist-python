import subprocess
import logging
from typing import List, Tuple, Union
from pathlib import Path
import shutil

EXE = shutil.which("github-linguist")
GIT = shutil.which("git")


def linguist(path: Path, rtype: bool = False) -> Union[str, List[Tuple[str, str]]]:
    """runs Github Linguist Ruby script"""

    if not EXE:
        raise ImportError("GitHub Linguist not found, did you install it per README?")

    path = Path(path).expanduser()

    if not checkrepo(path):
        return None

    ret = subprocess.check_output([EXE, str(path)], universal_newlines=True).split("\n")

    # %% parse percentage
    lpct = []

    for line in ret:
        L = line.split()
        if not L:  # EOF
            break
        lpct.append((L[1], L[0][:-1]))

    if rtype:
        return lpct[0][0]

    return lpct


def checkrepo(path: Path) -> bool:
    """basic check for healthy Git repo ready for Linguist to analyze"""

    if not GIT:
        raise ImportError("Git not found")

    path = Path(path).expanduser()

    if not (path / ".git").is_dir():
        logging.error(f'{path} does not seem to be a Git repository, and Linguist only works on files after "git commit"')
        return False

    # %% detect uncommited (dirty)
    ret = subprocess.check_output([GIT, "status", "--porcelain"], cwd=path, universal_newlines=True)

    ADD = {"A", "?"}
    MOD = "M"

    for line in ret.split("\n"):
        L = line.split()
        if not L:
            continue

        if ADD.intersection(L[0]) or (MOD in L[0] and L[1] == ".gitattributes"):
            logging.warning(f' {path} has uncommited changes: \n\n{ret}\n Linguist only works on files after "git commit"')
            return False

    return True
