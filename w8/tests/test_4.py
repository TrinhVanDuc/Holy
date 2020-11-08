from homework.Задача_4 import get_cartesian_product
import pytest

@pytest.mark.parametrize('n,result',[(get_cartesian_product([1, 2], [3, 4]),[(1, 3), (1, 4), (2, 3), (2, 4)])])
def test_product(n,result):
    assert n == result

