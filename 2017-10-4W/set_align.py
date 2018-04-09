# https://programmers.co.kr/learn/challenge_codes/159

def get_factorial(n):
    factorial = [1 for _ in range(n+1)]
    for i in range(2, n+1):
        factorial[i] = i * factorial[i-1]

    return factorial

def setAlign(n, k):
    factorial = get_factorial(n)
    digits = [x+1 for x in range(factorial[n])]

    rem = k-1
    answer = []
    for i in range(n, 0, -1):
        d = rem // factorial[i-1]
        rem = rem % factorial[i-1]
        answer.append(digits.pop(d))

    return answer
