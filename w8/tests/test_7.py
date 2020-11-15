from homework.Задача_7 import get_combinations_with_r
import pytest

@pytest.mark.parametrize('in_put, result', [
    [("cat", 2), ["aa", "ac", "at", "cc", "ct", "tt"]]
])
def test_combinations(in_put, result):
    assert get_combinations_with_r(*in_put) == result


