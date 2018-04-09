def solve(cache, strs, t, start):
    if len(t) == 0:
        return 0

    if cache.get(start, False):
        return cache[start]

    ret = 20000
    for piece in strs:
        if piece[0] < t[0]:
            continue
        if piece[0] > t[0]:
            break
        
        if piece == t[:len(piece)]:
            remainder = solve(cache, strs, t[len(piece):], start + len(piece))
            if remainder == -1:
                continue
            ret = min(ret, 1 + remainder)


    if ret == 20000:
        return -1

    cache[start] = ret
    return ret

def solution(strs, t):
    strs.sort()

    cache = {}
    answer = solve(cache, strs, t, 0)

    return answer
