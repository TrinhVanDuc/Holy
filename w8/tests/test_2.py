from homework.Задача_2 import fibonacci
import pytest

@pytest.mark.parametrize('n,result', [(list(fibonacci(2)),[1,1]),(list(fibonacci(3)),[1,1,2])])
def test_fibonacci(n, result):
    assert n == result
