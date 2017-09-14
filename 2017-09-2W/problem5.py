def dfs(land, picked, row_index, prev_i):
    if row_index >= len(land):
        print(picked)
        return

    for col_index, x in enumerate(land[row_index]):
        if prev_i == col_index:
            continue
        picked.append(x)
        dfs(land, picked, row_index+1, col_index)
        picked.pop()

def solve(land, picked, row_index, prev_i):
    print(picked)
    if row_index >= len(land):
        return 0

    ret = 0
    for index, x in enumerate(land[row_index]):
        if index == prev_i:
            continue
        picked.append(x)
        ret = max(ret, x + solve(land, picked, row_index+1, index))
        picked.pop()

    return ret

def solution(land):
    answer = solve(land, [], 0, -1)
    return answer
