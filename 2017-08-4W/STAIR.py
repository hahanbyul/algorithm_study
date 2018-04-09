# https://www.acmicpc.net/problem/2579

class Stair:
    def __init__(self, N):
        self.score = [0]
        self.N = N
        self.cache = {}

    def read_stairs(self):
        self.score.append(int(input()))

    def solve(self, index):
        if self.cache.get(index, False):
            return self.cache[index]

        if index == self.N:
            return self.score[self.N]
        if index == self.N-1:
            return self.score[self.N] + self.score[self.N-1]
        if index == self.N-2:
            return self.score[self.N] + self.score[self.N-2]
        
        step_1_2 = self.score[index] + self.score[index+1] + self.solve(index+3)
        step_2   = self.score[index] + self.solve(index+2)

        ret = max(step_1_2, step_2)
        self.cache[index] = ret
        return ret


def main():
    stair_num = int(input())
    stair = Stair(stair_num)
    for _ in range(stair_num):
        stair.read_stairs()
    print(max(stair.solve(0), stair.solve(1)))


if __name__ == '__main__':
    main()
