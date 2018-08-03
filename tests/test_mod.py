#!/usr/bin/env python
import ghlinguist as ghl
import pytest
from pathlib import Path

R = Path(__file__).resolve().parents[1]


def test_linguist():
    langs = ghl.linguist(R)

    assert langs[0][0] == 'Python'


def test_type():
    assert ghl.linguist(R, rtype=True) == 'Python'


def test_norepo(tmpdir):
    assert ghl.linguist(tmpdir.mkdir('empty')) is None


if __name__ == '__main__':
    pytest.main(['-x', __file__])
