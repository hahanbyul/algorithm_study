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
board_ex = "0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 1 1 0 0 0\n0 1 1 1 0 0 0 1 1 0 0 0 \
            \n0 1 1 1 1 1 1 0 0 0 0 0\n0 1 1 1 1 1 0 1 1 0 0 0\n0 1 1 1 1 0 0 1 1 0 0 0\n0 0 1 1 0 0 0 1 1 0 0 0 \
            \n0 0 1 1 1 1 1 1 1 0 0 0\n0 0 1 1 1 1 1 1 1 0 0 0\n0 0 1 1 1 1 1 1 1 0 0 0\n0 0 1 1 1 1 1 1 1 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0"

c = Cheese(board1)
c.row_edge_iter()
c.row_hole_iter()

c2 = Cheese(board2)
c2.row_edge_iter()
c2.row_hole_iter()

cheese_ex = Cheese(board_ex)

def test_col():
    assert c2.col(1) == [0, 1, 1, 1, 1, 0]
    assert c2.col(2) == [0, 1, 0, 1, 0, 0]


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

def test_print_melting_cheese():
    cheese_ex.edge_iter('row')
    cheese_ex.edge_iter('col')

    #cheese_ex.print_melting_cheese(cheese_ex.color_row_edge(cheese_ex.board))
    #cheese_ex.print_melting_cheese(cheese_ex.color_col_edge(cheese_ex.board))

    cheese_ex.hole_iter('row')
    cheese_ex.hole_iter('col')
    cheese_ex.color_row_hole(cheese_ex.board)
    cheese_ex.print_melting_cheese(cheese_ex.color_col_hole(cheese_ex.board))

    # cheese_ex.print_melting_cheese(cheese_ex.board)
    # cheese_ex.color_melting_cheese(cheese_ex.is_col_empty, cheese_ex.get_col_edge)
    # cheese_ex.row_edge_iter()
    # cheese_ex.row_hole_iter()

def test_general_edge_iter():
    cheese1 = Cheese(board1)
    cheese2 = Cheese(board1)

    cheese1.row_edge_iter()
    cheese2.edge_iter('row')

    assert cheese1.is_row_empty == cheese2.is_row_empty
    assert cheese1.row_first == cheese2.row_first
    assert cheese1.row_last == cheese2.row_last

def test_general_hole_iter():
    cheese1 = Cheese(board1)
    cheese2 = Cheese(board1)

    cheese1.row_edge_iter()
    cheese2.row_edge_iter()

    cheese1.row_hole_iter()
    cheese2.hole_iter('row')

    assert cheese1.is_row_empty == cheese2.is_row_empty
    assert cheese1.row_hole == cheese2.row_hole
