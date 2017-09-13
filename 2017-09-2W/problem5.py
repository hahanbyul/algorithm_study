def solve(cache, land, row_index, prev_i):
    if cache.get((row_index, prev_i), False):
        return cache[(row_index, prev_i)]

    if row_index >= len(land):
        return 0

    ret = 0
    for index, x in enumerate(land[row_index]):
        if index == prev_i:
            continue
        ret = max(ret, x + solve(cache, land, row_index+1, index))

    cache[(row_index, prev_i)] = ret
    return ret

def solution(land):
    cache = {}
    answer = solve(cache, land, 0, -1)
    return answer
