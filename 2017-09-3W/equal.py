import math
import heapq

class Equal:
    def __init__(self, initial):
        self.array = initial

    @staticmethod
    def sub_min(array):
        min_val = min(array)
        for i in range(len(array)):
            array[i] -= min_val
        return array

    @staticmethod
    def compute_add_times(candy):
        add_5  = candy // 5
        remain = candy %  5
        add_2  = remain // 2
        add_1  = remain %  2

        return add_5 + add_2 + add_1

    def solve(self):
        self.sub_min(self.array)

        ret = 0
        for x in self.array:
            ret += self.compute_add_times(x)

        return ret

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        initial = [int(x) for x in input().split()]

        eq = Equal(initial)
        print(eq.solve_bfs())

if __name__ == '__main__':
    main()

