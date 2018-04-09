from FIBONACCI import Fibonacci

def test_fibonacci():
    f = Fibonacci()
    assert f.fibonacci(2) == 1
    assert f.fibonacci(4) == 3
    assert f.fibonacci(10) == 55
    print(f.cache_solve)
    print(f.cache_0call)
    print(f.cache_1call)

def test_ex():
    f = Fibonacci()
    assert f.solve(0) == (1, 0)
    assert f.solve(1) == (0, 1)
    assert f.solve(3) == (1, 2)

