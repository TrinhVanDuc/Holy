from homework.Задача_9 import maximize
import pytest

lists = [
    [5, 4],
    [7, 8, 9],
    [5, 7, 8, 9, 10]
]
def test_maximize():
    assert maximize(lists,1000) == 206
