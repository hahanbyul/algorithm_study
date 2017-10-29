from set_align import setAlign
from set_align import get_factorial

def test_factorial():
    factorial = get_factorial(10)
    assert factorial[5] == 120
    assert factorial[7] == 5040
    assert factorial[10] == 3628800
    assert len(factorial) == 11

def test_range():
    print(range(7, 0, -1))

def test_setAlign():
    assert setAlign(3, 1) == [1, 2, 3]
    assert setAlign(3, 2) == [1, 3, 2]
    assert setAlign(3, 3) == [2, 1, 3]
    assert setAlign(3, 4) == [2, 3, 1]
    assert setAlign(3, 5) == [3, 1, 2]
    assert setAlign(3, 6) == [3, 2, 1]

def test_setAlign2():
    n = 5
    factorial = get_factorial(n)
    for k in range(1, factorial[n]+1):
        print(setAlign(n, k))

