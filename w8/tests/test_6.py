from homework.Задача_6 import get_combinations
import pytest

@pytest.mark.parametrize('in_put, result',[(get_combinations('cat',2),["a", "c", "t", "ac", "at", "ct"])])
def test_combinations(in_put, result):
    assert in_put == result

