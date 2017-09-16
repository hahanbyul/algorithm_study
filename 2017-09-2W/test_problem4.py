from problem4 import solution

def test_sum():
    assert sum([0, 1, 2]) == 3
    print(sum([[0, 1, 2], [0, 1, 1]]))
    assert sum([[0, 1, 2], [0, 1, 1]]) == 5

def test_basic_test():
    board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
    assert solution(board) == 9

def test_basic_test2():
    board2 = [[0,0,1,1],[1,1,1,1]]
    assert solution(board2) == 4
    board3 = [[0,0,0,1],[0,0,0,0]]
    assert solution(board3) == 1

