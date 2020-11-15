from homework.Задача_8 import compress_string
import pytest

def test_compress_string():
    assert compress_string('1222311') == [(1, 1), (3, 2), (1, 3), (2, 1)]
    assert compress_string('03112305') == [(1, 0), (1, 3), (2, 1), (1, 2), (1, 3), (1, 0), (1, 5)]
