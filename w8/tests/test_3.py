import pytest
@pytest.mark.parametrize('n,result', [(list(map(abs,[1,-4])),[1,4]),(list(map(int,['1','2'])),[1,2])])
def test_map(n, result):
    assert n == result

def test_zip():
    assert list(zip([1, 2, 3], ['a', 'b', 'c']) )== [(1, 'a'), (2, 'b'), (3, 'c')]
    assert list(zip(range(5), range(100))) == [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

def test_filter():
    assert list(filter(None, [11, False, 18, 21, "", 12, 34, 0, [], {}])) == [11, 18, 21, 12, 34]
    
def test_enumerate():
    assert list(enumerate(['a','b','c'])) ==[(0,'a'),(1,'b'),(2,'c')]
