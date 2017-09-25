def solve(n, k, b):
    # print(f'n: {n}, k: {k}, b: {b}')
    if k == 0 or k*(k+1)//2 < n:
        return -1

    if b == 1:
        if n <= k:
            return [n]
        else:
            return -1

    for num_to_add in range(k, 1, -1):
        if num_to_add >= n:
            continue

        ret = solve(n-num_to_add, num_to_add-1, b-1)
        if ret != -1:
            ret.append(num_to_add)
            return ret

    return -1


def main():
    t = int(input())
    cache = {}
    for _ in range(t):
        n, k, b = [int(x) for x in input().split()]
        if cache.get((n,k,b), False):
            answer = cache.get((n,k,b))
        else:
            answer = solve(n, k, b)
            cache[(n,k,b)] = answer

        if answer != -1:
            print(" ".join([str(x) for x in answer]))
        else:
            print('-1')


if __name__ == '__main__':
    main()
