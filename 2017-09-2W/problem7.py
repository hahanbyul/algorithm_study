def solve(strs, t, start):
    if len(t) == 0:
        return 0

    ret = 20000
    for piece in strs:
        print(f'word: {piece}')
        if piece[0] < t[0]:
            continue
        if piece[0] > t[0]:
            break
        
        if piece == t[:len(piece)]:
            remainder = solve(strs, t[len(piece):], start + len(piece))
            if remainder == -1:
                continue
            ret = min(ret, 1 + remainder)

    print(f't: {t}, ret: {ret}')

    if ret == 20000:
        return -1

    return ret

def solution(strs, t):
    strs.sort()
    print(f'strs: {strs}')
    answer = solve(strs, t, 0)

    return answer
