from TILING2 import Tiling

def test_example():
    t = Tiling(1)
    assert t.compute(1) == 1

    t = Tiling(5)
    assert t.compute(5) == 8

    t = Tiling(100)
    print(t.compute(100) % 1000000007)
    assert t.compute(100) % 1000000007 == 782204094
