def compute_zero_to_next_carry(N):
    array = [0 for _ in range(N+1)]
    for i in range(2, N+1):
        array[i] = array[i-1] + i

    return array

def compute_summed_array(array):
    summed_array = [0 for _ in range(len(array))]
    summed_array[0] = array[0]
    for i in range(1, len(summed_array)):
        summed_array[i] = summed_array[i-1] + array[i]

    return summed_array

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
    for i, ch in enumerate(string[::-1]):
        if ch == '1':
            score += array[i+1]

    return score

def compute_odd_num(x, y):
    num = y - x + 1
    odd_num = num // 2 - 1 if x % 2 == 1 and y % 2 == 0 else num // 2
    return odd_num

def bit_change(x, y):
    zero_to_next_carry = compute_zero_to_next_carry(len(bin(y - x)))
    zero_to_next_carry_summed = compute_summed_array(zero_to_next_carry)

    current = x
    summed = compute_odd_num(x, y)
    print('odd:',summed)

    while y - current > 0:
        diff = y - current
        print('current: %d,' % current, bin(current))
        print('y: %d,' % y, bin(y))
        print('diff: %d,' % diff, bin(diff))
        print('summed:',summed)
        zero_num = count_zero(bin(current))
        if zero_num == 0:
            one_num = count_one(bin(current))
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
            summed += zero_to_next_carry_summed[zero_num]
            current += skip

            one_num = count_one(bin(current))
            summed += one_num + 1
            current += 1
        elif diff == skip:
            summed += zero_to_next_carry_summed[zero_num]
            current += skip
        else:
            summed += compute_score(bin(diff), zero_to_next_carry)
            break
 
    return summed
