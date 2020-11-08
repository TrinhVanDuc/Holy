from homework.Задача_7 import get_combinations_with_r
import pytest

@pytest.mark.parametrize('in_put, result', [(get_combinations_with_r("cat", 2), ["aa", "ac", "at", "cc", "ct", "tt"])])
def test_combinations(in_put, result):
    assert in_put == result


