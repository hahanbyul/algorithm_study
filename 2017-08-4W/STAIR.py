# https://www.acmicpc.net/problem/2579

class Stair:
    def __init__(self, N):
        self.score = [0]
        self.N = N

    def read_stairs(self):
        self.score.append(input())

    def solve(self, step_prev, index):
        print(f'index: {index}')
        if index == self.N:
            print(f'hist: {step_prev}')
            return self.score[self.N]

        ret = 0
        for step in [1, 2]:
            if len(step_prev) >= 2 and step_prev[-1] ==  1 and step == 1:
                continue
            if index + step > self.N:
                break

            step_prev.append(step)
            ret2 = self.score[index] + self.solve(step_prev, index + step)
            ret = max(ret, ret2)
            print(f'ret: {ret2}')
            step_prev.pop()

        print(f'max_ret: {ret}')
        return ret


def main():
    stair_num = int(input())
    stair = Stair(stair_num)
    for _ in range(stair_num):
        stair.read_stairs()
    print(stair.solve([], 0))


if __name__ == '__main__':
    main()
