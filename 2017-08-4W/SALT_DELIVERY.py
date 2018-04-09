# https://www.acmicpc.net/problem/2839

def main():
    N = int(input())
    i = 0
    while N >= 0:
        if N % 5 == 0:
            return N // 5 + i
        N -= 3
        i += 1

    return -1


if __name__ == '__main__':
    print(main())
