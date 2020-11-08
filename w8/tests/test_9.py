from homework.Задача_9 import maximize
import pytest

lists = [
    [5, 4],
    [7, 8, 9],
    [5, 7, 8, 9, 10]
]
@pytest.mark.parametrize('in_put, result',[(maximize(lists, m=1000), 206)])
def test_maximize(in_put,result):
    assert in_put == result
