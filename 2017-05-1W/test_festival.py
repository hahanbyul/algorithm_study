from FESTIVAL import Festival

ex1 = Festival([1,2,3,1,2,3],3,6)
ex2 = Festival([1,2,3,1,2,3],2,6)

def test_sum_n():
    assert ex1.sum_n([1,2,3,1,2,3], 3) == [6, 6, 6, 6]

def test_sum_using_cache():
    ex1.sum_init()
    assert ex1.sum_using_cache(4) == [7, 8, 9]

def test_mean():
    ex1.sum_init()
    assert ex1.mean(3) == 2.0

def test_solve():
    print(ex2.solve())
