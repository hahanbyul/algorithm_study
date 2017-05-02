from CHEESE import Cheese
from CHEESE import Hole
import pprint as pp

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
c.edge_iter('row')
c.hole_iter('row')

c2 = Cheese(board2)
c2.edge_iter('row')
c2.hole_iter('row')

cheese_ex = Cheese(board_ex)

def test_col():
    assert c2.col(1) == [0, 1, 1, 1, 1, 0]
    assert c2.col(2) == [0, 1, 0, 1, 0, 0]

def test_hole():
    print(Hole((1,2), 'row', 3))

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
    assert c.get_row_hole(0) == []
    assert c.get_row_hole(1) == [(1,3)]
    assert c.get_row_hole(2) == [(1,3)]
    assert c.get_row_hole(3) == []
    assert c.get_row_hole(4) == []
    assert c.get_row_hole(5) == []

    assert c2.get_row_hole(0) == []
    assert c2.get_row_hole(1) == [(2,4)]
    assert c2.get_row_hole(2) == [(1,4)]
    assert c2.get_row_hole(3) == []
    assert c2.get_row_hole(4) == [(1,3),(3,5)]
    assert c2.get_row_hole(5) == []

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

def test_is_opended_hole():
    cheese_ex.edge_iter('row')
    cheese_ex.hole_iter('row')

    hole_list = cheese_ex.get_row_hole(3)
    assert hole_list == [(3,7)]
    assert cheese_ex.is_opened_hole(Hole(hole_list[0], 'row', 3))

    hole_list = cheese_ex.get_row_hole(5)
    assert not cheese_ex.is_opened_hole(Hole(hole_list[0], 'row', 5))
    hole_list = cheese_ex.get_row_hole(6)
    assert not cheese_ex.is_opened_hole(Hole(hole_list[0], 'row', 6))
    hole_list = cheese_ex.get_row_hole(7)
    assert not cheese_ex.is_opened_hole(Hole(hole_list[0], 'row', 7))

    cheese_ex.edge_iter('col')
    cheese_ex.hole_iter('col')

    hole_list = cheese_ex.get_col_hole(4)
    assert not cheese_ex.is_opened_hole(Hole(hole_list[0], 'col', 4))
    hole_list = cheese_ex.get_col_hole(5)
    assert not cheese_ex.is_opened_hole(Hole(hole_list[0], 'col', 5))
    hole_list = cheese_ex.get_col_hole(6)
    assert not cheese_ex.is_opened_hole(Hole(hole_list[0], 'col', 6))
    hole_list = cheese_ex.get_col_hole(7)
    assert not cheese_ex.is_opened_hole(Hole(hole_list[0], 'col', 7))
    hole_list = cheese_ex.get_col_hole(8)
    assert cheese_ex.is_opened_hole(Hole(hole_list[0], 'col', 8))

def test_connected():
    hole1 = Hole((3,5),'row',1)
    hole2 = Hole((4,8),'row',2)
    assert not hole1.is_connected(hole2)

def test_update_row_hole():
    cheese_ex.edge_iter('row')
    cheese_ex.hole_iter('row')

    cheese_ex.update_hole_relation('row')
    print(f'\nopened: {cheese_ex.opened_holes}')
    print('row_holes: ')
    pp.pprint(cheese_ex.row_hole)

def test_update_col_hole():
    cheese_ex.edge_iter('col')
    cheese_ex.hole_iter('col')

    cheese_ex.update_hole_relation('col')
    print(f'\nopened: {cheese_ex.opened_holes}')
    print('col_holes: ')
    pp.pprint(cheese_ex.col_hole)

def test_color_opened_holes():
    cheese_ex.edge_iter('row')
    cheese_ex.hole_iter('row')
    cheese_ex.update_hole_status('row')

    cheese_ex.edge_iter('col')
    cheese_ex.hole_iter('col')
    cheese_ex.update_hole_status('col')
    cheese_ex.print_melting_cheese(cheese_ex.color_opened_hole(cheese_ex.board))

def test_solve_iter():
    cheese_ex.solve_iter()
    print(cheese_ex.count_melting())
    cheese_ex.solve_iter()
    print(cheese_ex.count_melting())
    cheese_ex.solve_iter()
    cheese_ex.print_melting_cheese()
