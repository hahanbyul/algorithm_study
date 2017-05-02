from CHEESE import Cheese

line1 = [0,1,0,1,1,0]
board1 = [[0,0,0,0,0],
          [0,1,0,1,0],
          [0,1,0,1,0],
          [0,1,1,1,0],
          [0,1,0,0,0],
          [0,0,0,0,0]]
board2 = [[0,0,0,0,0,0,0],
          [0,1,1,0,1,1,0],
          [0,1,0,0,1,0,0],
          [0,1,1,1,1,1,0],
          [0,1,0,1,0,1,0],
          [0,0,0,0,0,0,0]]

c = Cheese(board1)
c.row_edge_iter()
c.row_hole_iter()

c2 = Cheese(board2)
c2.row_edge_iter()
c2.row_hole_iter()

def test_first_cheese():
    assert c.first_cheese(line1, 0) == 1
    assert c.first_cheese(line1, 1) == 3

def test_last_cheese():
    assert c.last_cheese(line1, len(line1)-1) == 4
    assert line1 == [0,1,0,1,1,0]
    assert c.last_cheese(line1, 4) == 1

def test_row_edge():
    assert c.get_row_edge(0) is None and c.get_row_edge(1) == (1,3) and c.get_row_edge(2) == (1,3) \
            and c.get_row_edge(3) == (1,3) and c.get_row_edge(4) == (1,1) and c.get_row_edge(5) is None

def test_col_edge():
    pass

def test_has_row_hole():
    assert c.get_row_hole(0) is None
    assert c.get_row_hole(1) == [(1,3)]
    assert c.get_row_hole(2) == [(1,3)]
    assert c.get_row_hole(3) is None
    assert c.get_row_hole(4) is None
    assert c.get_row_hole(5) is None

    assert c2.get_row_hole(0) is None
    assert c2.get_row_hole(1) == [(2,4)]
    assert c2.get_row_hole(2) == [(1,4)]
    assert c2.get_row_hole(3) is None
    assert c2.get_row_hole(4) == [(1,3),(3,5)]
    assert c2.get_row_hole(5) is None
