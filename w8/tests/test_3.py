from homework.Задача_3 import analis_zip, analis_map, analis_enumerate
import pytest

def test_map():
    assert list(analis_map(abs,[0,-1,-2])) == [0,1,2]

def test_zip():
    assert list(analis_zip([1, 2, 3], ['a', 'b', 'c']) )== [(1, 'a'), (2, 'b'), (3, 'c')]
    assert list(analis_zip(range(5), range(100))) == [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

    
def test_enumerate():
    assert list(analis_enumerate(['a','b','c'])) == [(0,'a'),(1,'b'),(2,'c')]
