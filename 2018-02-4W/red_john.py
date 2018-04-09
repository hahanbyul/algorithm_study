import sys

cache = {}
is_prime_cache = {}
prime_num_cache = {}

def solve(n):
    return find_num_of_prime(redJohn(n))

def redJohn(n):
    if cache.get(n, False):
        print('cached')
        return cache[n]

    print(n)
    if n < 4:
        cache[n] = 1
        return 1

    ret = redJohn(n-1) + redJohn(n-4)
    cache[n] = ret

    return ret

def find_num_of_prime(n):
    if prime_num_cache.get(n, False):
        return prime_num_cache[n]

    if len(prime_num_cache.keys()) == 0:
        answer = 0
        for i in range(2, n):
            answer += is_prime(n)
        prime_num_cache[n] = answer
        return answer

    for key in sorted(prime_num_cache.keys(), reverse=True)[::-1]:
        if key < n:
            answer = prime_num_cache[key]
            for i in range(key+1, n):
                answer += is_prime(n)
            prime_num_cache[n] = answer
            return answer

def is_prime(n):
    if n <= 1:
        return False

    if is_prime_cache.get(n, False):
        return is_prime_cache[n]

    for i in range(2, n // 2):
        if n % i == 0:
            is_prime_cache[n] = False
            return False

    is_prime_cache[n] = True
    return True

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = solve(n)
        print(result)
