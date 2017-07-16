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
        max_need_sum, max_picked = self.solve_memo(self.capacity, 0)

        print('%d %d' % (max_need_sum, len(max_picked)))
        for thing in max_picked:
            print(thing)

        return max_need_sum, len(max_picked)

    def solve_memo(self, capacity, begin_idx):
        # print(f'cap: {capacity}, idx: {begin_idx}')
        ret = self.cache.get((capacity, begin_idx), False)
        if ret is not False:
            # print('cached!')
            return ret

        if begin_idx >= len(self.thing_list):
            return (0, [])

        this = self.thing_list[begin_idx]
        this_weight = this[1]
        this_need   = this[2]

        if capacity < this_weight:
            return (0, [])

        included_need, included_list = self.solve_memo(capacity - this_weight, begin_idx + 1)
        included_need += this_need
        included_list_new = [x for x in included_list]
        included_list_new.append(this[0])

        excluded_need, excluded_list = self.solve_memo(capacity, begin_idx + 1)
        excluded_list_new = [x for x in excluded_list]

        if included_need > excluded_need:
            ret = (included_need, included_list_new)
        else:
            ret = (excluded_need, excluded_list_new)

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
