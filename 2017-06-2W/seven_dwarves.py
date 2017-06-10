class SevenDwarves:
    def __init__(self):
        pass

    def find_seven_dwarves(self, all_heights):
        print(self.dfs([], 0, sorted(all_heights), 7, 100, 0))

    def dfs(self, picked, summed, cand, num_to_select, sum_to_select, i_begin):
        if len(picked) == num_to_select:
            print(picked)
            print(summed)
            if summed == sum_to_select:
                return picked

        for i in range(i_begin, len(cand)):
            picked.append(cand[i])
            summed += cand[i]

            ret = self.dfs(picked, summed, cand, num_to_select, sum_to_select, i + 1)
            if ret is not None:
                return ret

            picked.pop()
            summed -= cand[i]

def main():
    all_heights = []
    for _ in range(9):
        height = int(input())
        all_heights.append(height)

    sd = SevenDwarves()
    sd.find_seven_dwarves(all_heights)

if __name__ == '__main__':
    main()
