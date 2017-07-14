# https://algospot.com/judge/problem/read/PACKING

class Packing:
    def __init__(self, weight):
        self.weight = weight
        self.max_need_sum = 0
        self.thing_list = []

    def read_line(self, string):
        thing, vol, need = string.split()
        self.thing_list.append((thing, int(vol), int(need)))

    def solve(self):
        self.thing_list.sort(key=lambda tup: tup[1]) # sort by volume
        self.dfs([], 0, 0, 0)

        # print(f'{self.max_need_sum} {len(self.max_picked)}')
        print('%d %d' % (self.max_need_sum, len(self.max_picked)))
        for thing in self.max_picked:
            print(thing[0])
        return self.max_need_sum, len(self.max_picked)

    def dfs(self, picked, begin_idx, vol_sum, need_sum):
        # print(f'picked: {picked}')
        # print(f'need_sum: {need_sum}, vol_sum: {vol_sum}')

        if need_sum > self.max_need_sum:
            self.max_need_sum = need_sum
            self.max_picked = [thing for thing in picked]

        for i in range(begin_idx, len(self.thing_list)):
            ith_thing = self.thing_list[i]
            picked.append(ith_thing)
            next_vol  = vol_sum + ith_thing[1]
            next_need = need_sum + ith_thing[2]

            if next_vol > self.weight:
                picked.pop()
                break

            self.dfs(picked, i+1, next_vol, next_need)
            picked.pop()


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
