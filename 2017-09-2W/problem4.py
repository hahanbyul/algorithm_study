def sum_elements(board):
    ret = 0
    for row in board:
        ret += sum(row)
    return ret

def subboard(board, x, y, length):
    return [board[i][x:x+length] for i in range(y, y+length)]

def solve(board, length):
    area = length*length
    # dynamic programming
    for x in range(len(board[0]) - length + 1):
        for y in range(len(board) - length + 1):
            if sum_elements(subboard(board, x, y, length)) == area:
                return True

    return False

def solution(board):
    max_length = min(len(board), len(board[0]))
    for length in range(max_length, 0, -1):
        if solve(board, length):
            return length*length
