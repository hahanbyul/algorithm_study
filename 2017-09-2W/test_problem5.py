from problem5 import solution
from problem5 import dfs

def test_basic_test():
    assert solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]) == 16

def test_basic_test2():
    assert solution([[1,2,3,4],[4,3,2,1]]) == 8

def test_dfs():
    dfs([[1,2,3,5],[5,6,7,8],[4,3,2,1]], [], 0, -1)

