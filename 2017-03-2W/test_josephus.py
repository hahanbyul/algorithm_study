from JOSEPHUS import Josephus
def test_initial():
    jo = Josephus(3, 2)
    assert jo.survivors == [1, 2, 3]

def test_iterate():
    jo = Josephus(3, 2)
    assert jo.iterate() == [1, 3]

    jo = Josephus(3, 4)
    assert jo.iterate() == [1, 2, 3]

def test_iterate2():
    jo = Josephus(7, 9)
    assert jo.iterate2() == [1, 4, 2, 3, 7, 5, 6]

    jo = Josephus(5, 2)
    assert jo.iterate2() == [1, 3, 5, 4, 2]

def test_get_survivors():
    jo = Josephus(7, 9)
    assert jo.get_survivors() == [5, 6]

    jo = Josephus(5, 2)
    assert jo.get_survivors() == [2, 4]

    jo = Josephus(6, 3)
    assert jo.get_survivors() == [3, 5]

    jo = Josephus(40, 3)
    assert jo.get_survivors() == [11, 26]
