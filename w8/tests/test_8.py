from homework.Задача_8 import compress_string
import pytest

@pytest.mark.parametrize('in_put, result',[(compress_string('1222311'), [(1, 1), (3, 2), (1, 3), (2, 1)])])
def test_cartesian(in_put, result):
    assert in_put == result
