#!/usr/bin/env python
import pylinguist as pl
import pytest
from pathlib import Path

R = Path(__file__).resolve().parents[1]

def test_linguist():
    langs = pl.linguist(R, False)

    assert langs[0][0] == 'Python'


if __name__ == '__main__':
    pytest.main(['-x', __file__])