from FORTRESS import Fortress
from FORTRESS import Wall

w1 = Wall("21 15 20")
w2 = Wall("15 15 10")
w3 = Wall("30 24 5")
w4 = Wall("32 10 7")

def test_is_inside():
    #assert w1.is_inside(w2) # should raise exception!
    assert w2.is_inside(w1)
    assert not w3.is_inside(w2)
    assert not w3.is_inside(w4)

def test_wall_operators():
    assert w2 in w1                 # contains
    assert w1 == Wall("21 15 20")   # eq 
    assert w2 < w1                  # lt
    assert not w4 < w3

def test_sort():
    assert sorted([w2, w3, w1, w4]) == [w3, w4, w2, w1]

def test_fortress():
    f = Fortress()
    f.read_string('21 15 20\n15 15 10\n13 12 5\n12 12 3\n19 19 2\n30 24 5\n32 10 7\n32 9 4')
    assert str(f.walls) == '[(21, 15, 20), (15, 15, 10), (32, 10, 7), (13, 12, 5), (30, 24, 5), (32, 9, 4), (12, 12, 3), (19, 19, 2)]'

    tree = f.make_tree()
    assert [node.wall for node in tree.inside_walls] == [(15, 15, 10), (32, 10, 7), (32, 24, 5)]

"""
def test_tree():
    assert tree == '(21, 15, 20) - [(15, 15, 10) - [(13, 12, 5) - [(12, 12, 3)], (19, 19, 2)], (32, 10, 7) - [(32, 9, 4)], (30, 24, 5)]'
"""

