def solve(sticker, start, is_first_picked):
    if start == len(sticker)-1:
        if not is_first_picked:
            return sticker[start]
        else:
            return 0

    if start >= len(sticker):
        return 0

    if start == 0:
        ret = max(solve(sticker, start+1, False), sticker[start] + solve(sticker, start+2, True))
    else:
        ret = max(solve(sticker, start+1, is_first_picked), sticker[start] + solve(sticker, start+2, is_first_picked))

    return ret

def solution(sticker):
    answer = solve(sticker, 0, None)
    return answer
