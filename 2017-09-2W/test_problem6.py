from problem6 import solution

def test():
    a = [1, 2, 3]
    print(a[3 % len(a)])

def test_ex1():
    assert solution([14, 6, 5, 11, 3, 9, 2, 10]) == 36

def test_ex2():
    assert solution([1, 3, 2, 5, 4]) == 8
