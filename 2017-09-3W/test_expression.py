from expression import Expression

def test_move_right():
    array = [2, 3, 4]
    assert Expression.move_right(array, 9) == 12 and array == [3, 4, 5]
    assert Expression.move_right(array, 12) == 15 and array == [4, 5, 6]

def test_get_initial_array():
    assert Expression.get_initial_array(15) == ([1, 2, 3, 4, 5], 15)
    assert Expression.get_initial_array(20) == ([1, 2, 3, 4, 5, 6], 21)

def test_ex():
    ex = Expression()
    assert ex.solve(15) == 4

