def compute_zero_to_next_carry(N):
    array = [0 for _ in range(N+1)]
    for i in range(2, N+1):
        array[i] = array[i-1] + i

    return array
def count_zero(string):
    return count_cont_char(string, '0')

def count_one(string):
    return count_cont_char(string, '1')

def count_cont_char(string, char):
    cnt = 0
    while cnt < len(string) and string[-1-cnt] == char:
        cnt += 1
    return cnt

def compute_score(string, array):
    score = 0
    for i, ch in enumerate(string[:-1:-1]):
        if ch == '1':
            score += array[i]

    return score

def bit_change(x, y):
    zero_to_next_carry = compute_zero_to_next_carry(len(bin(y - x)))

    num = y - x + 1
    even_num = num // 2 if x % 2 == 1 and y % 2 == 0 else num // 2 - 1

    current = x
    summed = even_num

    while y - current > 0:
        zero_num = count_zero(bin(current))
        if zero_num == 0:
            one_num = count_one(current)
            summed += one_num + 1
            current += 1
            continue

        if zero_num == 1:
            one_num = count_one(bin(current+1))
            summed += one_num + 1
            current += 2
            continue
        
        diff = y - current
        skip = 2 ** zero_num - 1

        if diff > skip:
            summed += zero_to_next_carry[zero_num] + zero_to_next_carry[zero_num-1]
            current += skip

            one_num = count_one(current)
            summed += one_num + 1
            current += 1
        else:
            summed += compute_score(bin(diff), zero_to_next_carry)

    return summed
