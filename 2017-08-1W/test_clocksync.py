from CLOCKSYNC import Clocksync
from CLOCKSYNC_MAT import Clocksync as Clocksync_mat
import pprint as pp
import numpy as np
from tkinter import Tk
import random

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
    cs = Clocksync_mat()
    print()
    switch_mat = cs.get_switch_mat()
    print(np.array(switch_mat))
    ex1 = np.array([0, 2, 2, 2, 2, 2, 0, 0, 0, 0])

def test_add_multiple_row():
    cs = Clocksync_mat()
    mat = [[1, 1], [1, 0]]
    answer = np.matmul([[1,0],[-1,1]], mat)
    cs.add_multiple_row(mat, 0, 1, -1)
    assert np.array_equal(mat, answer)

def test_identity_mat():
    cs = Clocksync_mat()
    print()
    print(np.array(cs.get_identity_mat()))

def test_pivotting():
    cs = Clocksync_mat()
    for i in range(10):
        cs.pivotting(cs.switch_mat, i)
        assert np.array_equal(cs.switch_mat, np.matmul(cs.identity_mat, cs.get_switch_mat()))
    print(np.array(cs.switch_mat))
    print(cs.identity_mat)

def test_swap_rows():
    mat = [[1, 1], [1, 0]]
    assert cs.swap_rows(mat, 0, 1) == [[1, 0], [1, 1]]

    mat = [[-1, 1], [1, -1]]
    assert cs.swap_rows(mat, 0, 1) == [[1, -1], [-1, 1]]

def test_get_state_mat():
    cs = Clocksync_mat()
    assert cs.get_state_mat('12 6 6 6 6 6 12 12 12 12 12 12 12 12 12 12') == [0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert cs.get_state_mat('12 9 3 12 6 6 9 3 12 9 12 9 12 12 6 6') == [0, 3, 1, 0, 2, 2, 3, 1, 0, 3, 0, 3, 0, 0, 2, 2]

def test_modularize():
    cs = Clocksync_mat()
    print(cs.modularize([-5, 1, 2]))

def test_ex1_mat_ver():
    cs = Clocksync_mat()
    for i in range(10):
        cs.pivotting(cs.switch_mat, i)
    A = np.array(cs.switch_mat)
    b = -np.array(cs.get_state_mat('12 6 6 6 6 6 12 12 12 12 12 12 12 12 12 12'))
    print(A)
    print(np.matmul(cs.identity_mat, b.T))

    b2 = -np.array(cs.get_state_mat('12 9 3 12 6 6 9 3 12 9 12 9 12 12 6 6'))
    print(np.matmul(cs.identity_mat, b2.T))

def test_solve():
    cs = Clocksync_mat()
    assert cs.solve('12 6 6 6 6 6 12 12 12 12 12 12 12 12 12 12') == 2

def test_solve_ex2():
    cs = Clocksync_mat()
    assert cs.solve('12 9 3 12 6 6 9 3 12 9 12 9 12 12 6 6') == 9

def test_compare():
    cs1 = Clocksync()
    cs2 = Clocksync_mat()
    while True:
        problem = ' '.join([str(random.randint(1, 4)*3) for _ in range(16)])
        print(problem)
        answer_mat = cs2.solve(problem)
        if answer_mat != -1:
            print(answer_mat)
            answer = cs.solve(problem)
            assert answer == answer_mat
            break
