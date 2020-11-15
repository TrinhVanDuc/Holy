from homework.Задача_4 import get_cartesian_product
import pytest

@pytest.mark.parametrize('func_args, result', [
    [([1, 2], [3, 4]), [(1, 3), (1, 4), (2, 3), (2, 4)]],
])
def test_product(func_args, result):
        assert get_cartesian_product(*func_args) == result

