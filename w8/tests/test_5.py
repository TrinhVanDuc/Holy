from homework.Задача_5 import get_permutations
import pytest

@pytest.mark.parametrize('func_args,result', [
    [("cat", 2), ["ac", "at", "ca", "ct", "ta", "tc"]]
    ])
def test_permutations(func_args, result):
    assert get_permutations(*func_args) == result 
