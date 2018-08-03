#!/usr/bin/env python
import ghlinguist as ghl
import pytest
from pathlib import Path

R = Path(__file__).resolve().parents[1]


def test_linguist():
    langs = ghl.linguist(R)

    assert langs[0][0] == 'Python'


def test_type():
    lang = ghl.linguist(R, rtype=True)

    assert lang == 'Python'


if __name__ == '__main__':
    pytest.main(['-x', __file__])
