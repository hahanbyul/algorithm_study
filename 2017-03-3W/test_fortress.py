from FORTRESS import Fortress
from FORTRESS import Wall

w0 = Wall("100 100 20")
w1 = Wall("21 15 20")
w2 = Wall("15 15 10")
w3 = Wall("30 24 5")
w4 = Wall("32 10 7")
w5 = Wall("0 0 100")
w6 = Wall("98 98 1")

def test_is_inside():
    assert not w1.is_inside(w2) # should raise exception!
    assert not w0.is_inside(w1)
    assert w2.is_inside(w1)
    assert not w3.is_inside(w2)
    assert not w3.is_inside(w4)
    assert not w6.is_inside(w5)

def test_wall_operators():
    assert w2 in w1                 # contains
    assert w1 == Wall("21 15 20")   # eq 
    assert w2 < w1                  # lt
    assert not w4 < w3
    assert sorted([w2, w3, w1, w4]) == [w3, w4, w2, w1]

f = Fortress()
f.read_string('21 15 20\n15 15 10\n13 12 5\n12 12 3\n19 19 2\n30 24 5\n32 10 7\n32 9 4')
tree = f.make_tree()

f2 = Fortress()
f2.read_string('5 5 15\n5 5 10\n5 5 5')
tree2 = f2.make_tree()

f3 = Fortress()
f3.read_string('0 0 200\n0 0 100\n10 10 2\n10 10 1\n20 20 1\n20 20 2')
tree3 = f3.make_tree()

def test_fortress_init():
    assert str(f.walls) == '[(21, 15, 20), (15, 15, 10), (32, 10, 7), (13, 12, 5), (30, 24, 5), (32, 9, 4), (12, 12, 3), (19, 19, 2)]'

def test_fortress():
    assert str(tree) == '(21, 15, 20) - [(15, 15, 10) - [(13, 12, 5) - [(12, 12, 3)], (19, 19, 2)], (32, 10, 7) - [(32, 9, 4)], (30, 24, 5)]'

    assert [node.wall   for node in tree.inside_walls] == [(15, 15, 10), (32, 10, 7), (30, 24, 5)]
    assert [node.height for node in tree.inside_walls] == [3, 2, 1]

    assert str(tree2) == '(5, 5, 15) - [(5, 5, 10) - [(5, 5, 5)]]'

    assert [node.wall   for node in tree2.inside_walls] == [(5, 5, 10)]
    assert [node.height for node in tree2.inside_walls] == [2]

def test_max_height():
    assert tree.max_height() == 3
    assert tree.inside_walls[0].max_height() == 2

    assert tree2.max_height() == 2
    assert tree2.inside_walls[0].max_height() == 1

    assert tree3.max_height() == 3
    assert tree3.inside_walls[0].max_height() == 2

def test_max_leaf_to_leaf():
    assert tree.max_leaf_to_leaf() == 5
    assert tree.inside_walls[0].max_leaf_to_leaf() == 3
    assert tree.inside_walls[1].max_leaf_to_leaf() == 1
    assert tree.inside_walls[2].max_leaf_to_leaf() == 0

    assert tree2.max_leaf_to_leaf() == 2

    assert tree3.max_leaf_to_leaf() == 3
    assert tree3.inside_walls[0].max_leaf_to_leaf() == 4

def test_iterate():
    res = f.iterate(tree, [])
    print(res)
    assert len(res) == len(f.walls)

    res = f2.iterate(tree2, [])
    print(res)
    assert len(res) == len(f2.walls)

    res = f3.iterate(tree3, [])
    print(res)
    assert len(res) == len(f3.walls)

def test_max_walls():
    assert f.get_max_walls() == 5
    assert f2.get_max_walls() == 2
    assert f3.get_max_walls() == 4
