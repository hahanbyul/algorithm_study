from RUNNINGMEDIAN import Heap

def test_heap():
    h = Heap()
    h.put(0)
    assert h.get_heap() == [0]
    h.put(1)
    h.put(2)
    assert h.get_heap() == [2, 0, 1]
    h.put(3)
    assert h.get_heap() == [3, 2, 1, 0]
    h.put(0)
    assert h.get_heap() == [3, 2, 1, 0, 0]
    h.put(2)
    assert h.get_heap() == [3, 2, 2, 0, 0, 1]
    print(h.delete_max())
    print(h.delete_max())
    print(h.delete_max())
