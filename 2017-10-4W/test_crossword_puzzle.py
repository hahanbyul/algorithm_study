from crossword_puzzle import Puzzle
from pprint import pprint 

VERTICAL = True
HORIZONTAL = False

ex1_puzzle = '+-++++++++\n+-++++++++\n+-++++++++\n+-----++++\n+-+++-++++\n+-+++-++++\n+++++-++++\n++------++\n+++++-++++\n+++++-++++'

def test_read():
    p = Puzzle()
    p.read_puzzle()
    p.read_words()

    print(p.puzzle)
    print(p.words)

    print(p.puzzle_to_string())

def test_get_empty_len():
    ex1 = Puzzle()
    ex1.puzzle = ex1_puzzle.split('\n')

    assert ex1.get_empty_len((0,1), VERTICAL) == 6
    assert ex1.get_empty_len((3,5), VERTICAL) == 7
    assert ex1.get_empty_len((3,1), HORIZONTAL) == 5

def test_is_satified():
    assert not Puzzle.is_satisfied('-----E', 'LONDON')
    assert not Puzzle.is_satisfied('----', 'LONDON')
    assert Puzzle.is_satisfied('-----N', 'LONDON')
    assert Puzzle.is_satisfied('L----N', 'LONDON')

def test_fill_puzzle():
    ex1 = Puzzle()
    ex1.puzzle = [[x for x in row] for row in ex1_puzzle.split('\n')]

    print()
    prev = ex1.fill_puzzle((0,1), 'LONDON', VERTICAL)
    print(prev)
    pprint.pprint(ex1.puzzle)

    assert ex1.get_condition((3,1), HORIZONTAL) == 'D----'
    prev = ex1.fill_puzzle((3,1), 'DELHI', HORIZONTAL)
    print(prev)
    pprint.pprint(ex1.puzzle)

def test_solve():
    ex1 = Puzzle()
    ex1.puzzle = [[x for x in row] for row in ex1_puzzle.split('\n')]
    ex1.words = 'LONDON;DELHI;ICELAND;ANKARA'.split(';')
    ex1.solve_this((0,1), VERTICAL)

def test_floor():
    ex1 = Puzzle()
    ex1.puzzle = [[x for x in row] for row in ex1_puzzle.split('\n')]
    print()
    pprint(ex1.puzzle)
    assert ex1.floor((0,1), VERTICAL) == (0, 1)
    assert ex1.floor((3,3), HORIZONTAL) == (3, 1)
    assert ex1.floor((7,5), VERTICAL) == (3, 5)
    assert ex1.floor((7,5), HORIZONTAL) == (7, 2)

    prev = ex1.fill_puzzle((0,1), 'LONDON', VERTICAL)
    assert ex1.floor((3,3), HORIZONTAL) == (3, 1)
