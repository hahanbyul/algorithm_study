from crossword_puzzle import Puzzle
import pprint 

ex1_puzzle = '+-++++++++\n+-++++++++\n+-++++++++\n+-----++++\n+-+++-++++\n+-+++-++++\n+++++-++++\n++------++\n+++++-++++\n+++++-++++'

def test_read():
    p = Puzzle()
    p.read_puzzle()
    p.read_words()

    print(p.puzzle)
    print(p.words)

def test_get_empty_len():
    ex1 = Puzzle()
    ex1.puzzle = ex1_puzzle.split('\n')

    assert ex1.get_empty_len((0,1), 'v') == 6
    assert ex1.get_empty_len((3,5), 'v') == 7
    assert ex1.get_empty_len((3,1), 'h') == 5

def test_is_satified():
    assert not Puzzle.is_satisfied('-----E', 'LONDON')
    assert not Puzzle.is_satisfied('----', 'LONDON')
    assert Puzzle.is_satisfied('-----N', 'LONDON')
    assert Puzzle.is_satisfied('L----N', 'LONDON')

def test_fill_puzzle():
    ex1 = Puzzle()
    ex1.puzzle = [[x for x in row] for row in ex1_puzzle.split('\n')]

    print()
    prev = ex1.fill_puzzle((0,1), 'LONDON', 'v')
    print(prev)
    pprint.pprint(ex1.puzzle)
    prev = ex1.erase_puzzle((0,1), prev, 'v')
    pprint.pprint(ex1.puzzle)


