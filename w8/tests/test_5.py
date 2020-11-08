from homework.Задача_5 import get_permutations
import pytest

@pytest.mark.parametrize('in_put,result',[(get_permutations("cat", 2), ["ac", "at", "ca", "ct", "ta", "tc"])])
def test_permutations(in_put, result):
    assert in_put == result
