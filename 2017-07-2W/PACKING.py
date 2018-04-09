# https://algospot.com/judge/problem/read/PACKING

class Packing:
    def __init__(self, capacity):
        self.capacity = capacity
        self.thing_list = []
        self.cache = {}

    def read_line(self, string):
        thing, vol, need = string.split()
        self.thing_list.append((thing, int(vol), int(need)))

    def solve(self):
        self.thing_list.sort(key=lambda tup: tup[1]) # sort by volume
        max_need_sum = self.solve_memo(self.capacity, 0)
        max_picked = self.reconstruct(self.capacity, 0, [])
        # print(f'max_picked: {max_picked}')

        print('%d %d' % (max_need_sum, len(max_picked)))
        for thing in max_picked:
            print(thing)

        return max_need_sum, len(max_picked)

    def reconstruct(self, capacity, begin_idx, picked):
        # print(f'cap: {capacity}, idx: {begin_idx}, picked: {picked}')
        if begin_idx >= len(self.thing_list):
            return picked

        this = self.thing_list[begin_idx]
        this_weight = this[1]
        this_need   = this[2]

        # print(f'left: {self.solve_memo(capacity, begin_idx)}')
        # print(f'right: {self.solve_memo(capacity - this_weight, begin_idx + 1)}')

        if self.solve_memo(capacity, begin_idx) == this_need + self.solve_memo(capacity - this_weight, begin_idx + 1):
            picked.append(this[0])
            ret = self.reconstruct(capacity - this_weight, begin_idx + 1, picked)
        else:
            ret = self.reconstruct(capacity, begin_idx + 1, picked)

        return ret

    def solve_memo(self, capacity, begin_idx):
        # print(f'cap: {capacity}, idx: {begin_idx}')
        ret = self.cache.get((capacity, begin_idx), False)
        if ret is not False:
            # print('cached!')
            return ret

        if begin_idx >= len(self.thing_list):
            return 0

        this = self.thing_list[begin_idx]
        this_weight = this[1]
        this_need   = this[2]

        if capacity < this_weight:
            return 0

        ret = max(this_need + self.solve_memo(capacity - this_weight, begin_idx + 1), self.solve_memo(capacity, begin_idx + 1))
        self.cache[(capacity, begin_idx)] = ret

        return ret


def main():
    C = int(input())
    for _ in range(C):
        N, W = [int(i) for i in input().split()]
        p = Packing(W)
        for _ in range(N):
            p.read_line(input())

        p.solve()

if __name__ == '__main__':
    main()
