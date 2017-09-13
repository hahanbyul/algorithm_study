def solve(land, row_index, prev_i):
    if row_index >= len(land):
        return 0

    ret = 0
    for index, x in enumerate(land[row_index]):
        if index == prev_i:
            continue
        ret = max(ret, x + solve(land, row_index+1, index))

    return ret

def solution(land):
    answer = solve(land, 0, -1)
    return answer
