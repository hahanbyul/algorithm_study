# https://www.acmicpc.net/problem/6603

class Lotto:
    def __init__(self):
        pass

    def read_line(self, string):
        self.S = string.split()
        self.S.pop(0)

    def solve(self):
        self.dfs([], 0)

    def dfs(self, picked, begin_idx):
        # print(f'picked: {picked}')
        if len(picked) == 6:
            print(' '.join(picked))
            return

        for i in range(begin_idx, len(self.S)):
            picked.append(self.S[i])
            self.dfs(picked, i+1)
            picked.pop()


def main():
    while True:
        line = input()
        if line == '0':
            break

        l = Lotto()
        l.read_line(line)
        l.solve()
        print()


if __name__ == '__main__':
    main()
