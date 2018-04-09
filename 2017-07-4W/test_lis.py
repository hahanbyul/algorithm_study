from lis import LIS

def test_ex1():
    lis = LIS()
    lis.solve([1,2,3,4])
    print(lis.cache)

def test_ex2():
    lis = LIS()
    print(lis.max_length([5, 4, 3, 2, 1, 6, 7, 8], 5, 0))
    print(lis.max_length([4, 3, 2, 1, 6, 7, 8], 4, 1))
    print(lis.max_length([3, 2, 1, 6, 7, 8], 3, 2))
    print(lis.cache)

def test_solve():
    lis = LIS()
    lis.seq = [5,4,3,2,1,6,7,8]
    assert lis.solve() == 4
    print(lis.cache)
    print(lis.choices)
    print(lis.reconstruct())
    
def test_ex3():
    lis = LIS()
    lis.seq = [5,6,7,8,1,2,3,4]
    assert lis.solve() == 4
    print(lis.cache)
    print(lis.choices)
    print(lis.reconstruct())

def test_ex4():
    lis = LIS()
    lis.seq = [9, 1, 3, 7, 5, 6, 20]
    lis.solve() == 5
    print(lis.cache)
    print(lis.choices)
    print(lis.reconstruct())

def test_ex5():
    lis = LIS()
    lis.seq = [1, 3, 2, 5, 3, 4, 5]
    lis.solve() == 5
    print(lis.cache)
    print(lis.choices)
    print(lis.reconstruct())

