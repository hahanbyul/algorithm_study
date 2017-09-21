import math
import heapq

class Equal:
    def __init__(self, initial):
        self.array = initial

    @staticmethod
    def are_all_same(array):
        for x in array:
            if x != 0:
                return False
        return True

    @staticmethod
    def add(array, num, index):
        ret = [x + num for x in array]
        ret[index] -= num
        return ret

    @staticmethod
    def sub_min(array):
        min_val = min(array)
        for i in range(len(array)):
            array[i] -= min_val
        return array

    def solve(self, array):
        self.sub_min(array)
        if self.are_all_same(array):
            return 0

        min_val = min(self.array)
        max_val = max(self.array)
        max_idx = self.array.index(max_val)

        ret = math.inf
        for num in [1, 2, 5]:
            ret = min(ret, 1 + self.solve(self.add(array, num, max_idx)))

        return ret

    def solve_bfs(self):
        queue = [(0, self.array)]
        visited = dict()

        while len(queue) > 0:
            count, array = heapq.heappop(queue)
            # print(f'array: {array}')
            if self.are_all_same(array):
                return count

            max_val = max(array)
            max_idx = array.index(max_val)

            for num in [1, 2, 5]:
                next_array = self.add(array, num, max_idx)
                self.sub_min(next_array)

                if not visited.get(tuple(next_array), False):
                    visited[tuple(next_array)] = True
                    heapq.heappush(queue, (count+1, next_array))


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        initial = [int(x) for x in input().split()]

        eq = Equal(initial)
        print(eq.solve_bfs())

if __name__ == '__main__':
    main()

