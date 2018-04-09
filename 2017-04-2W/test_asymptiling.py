from ASYMTILING import Asymtiling

def test_example():
    t = Asymtiling()
    assert t.compute(1) == 1
    assert t.compute(5) == 8
    # print(t.compute(100))
    assert t.compute(100) == 782204094

def test_asymtiling():
    t = Asymtiling()
    assert t.compute_asym(2) == 0
    assert t.compute_asym(4) == 2
    assert t.compute_asym(92) == 913227494

