from expression import move_right
from expression import get_initial_array
from expression import expressions

def test_move_right():
    array = [2, 3, 4]
    assert move_right(array, 9) == 12 and array == [3, 4, 5]
    assert move_right(array, 12) == 15 and array == [4, 5, 6]

def test_get_initial_array():
    assert get_initial_array(15) == ([1, 2, 3, 4, 5], 15)
    assert get_initial_array(20) == ([1, 2, 3, 4, 5, 6], 21)

def test_ex():
    # assert expressions(15) == 4
    assert expressions(30)

