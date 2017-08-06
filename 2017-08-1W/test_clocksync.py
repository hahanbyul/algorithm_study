from CLOCKSYNC import Clocksync
import pprint as pp
import numpy as np

cs = Clocksync()

def test_push_switch():
    assert cs.push_switch(tuple([12,6,6,6,6,6,12,12,12,12,12,12,12,12,12,12]), 0) == (9,3,3,6,6,6,12,12,12,12,12,12,12,12,12,12)
    assert cs.push_switch(cs.push_switch(tuple([12,6,6,6,6,6,12,12,12,12,12,12,12,12,12,12]), 8), 8) == (12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12)

def test_get_next():
    next_states = cs.get_next(tuple([12,6,6,6,6,6,12,12,12,12,12,12,12,12,12,12]))
    assert len(next_states) == 9
    print(next_states)

def test_ex1():
    assert cs.bfs(tuple([12,6,6,6,6,6,12,12,12,12,12,12,12,12,12,12])) == 2

def test_ex2():
    assert cs.bfs(tuple([int(i) for i in '12 9 3 12 6 6 9 3 12 9 12 9 12 12 6 6'.split()])) == 9

def test_switch_mat():
    print()
    switch_mat = cs.get_switch_mat()
    pp.pprint(switch_mat.T)
    """
    switch_mat_inv = np.linalg.inv(cs.get_switch_mat())
    pp.pprint(switch_mat_inv)
    pp.pprint(np.dot(switch_mat, switch_mat_inv))
    """

    asdf = np.array([
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
             [0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [-1, -2, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0],
             [0, 0, 0, -1, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, -1, 0, 1, 0, 0, 0, 0, 0, 0],
             [1, 0, -1, 0, 0, 0, -1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, -1, 0, 0, 1, -1, -1, 2, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1, 0, -1, 0],
             [0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1],
             ])

    print(np.matmul(asdf, switch_mat.T))

    ex1 = np.array([0, 2, 2, 2, 2, 2, 0, 0, 0, 0])

def test_add_multiple_row():
    mat = [[1, 1], [1, 0]]
    assert cs.add_multiple_row(mat, 0, 1, -1) == [[1,1], [0,-1]]

def test_identity_mat():
    print()
    print(cs.get_identity_mat())

def test_pivotting():
    cs = Clocksync()
    for i in range(10):
        cs.pivotting(cs.switch_mat, i)

def test_swap_rows():
    mat = [[1, 1], [1, 0]]
    assert cs.swap_rows(mat, 0, 1) == [[1, 0], [1, 1]]

    mat = [[-1, 1], [1, -1]]
    assert cs.swap_rows(mat, 0, 1) == [[1, -1], [-1, 1]]
