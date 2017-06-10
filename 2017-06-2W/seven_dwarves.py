class SevenDwarves:
    def __init__(self):
        pass

    def find_seven_dwarves(self, all_heights):
        pass

    def dfs(self, picked, cand, num_to_select, i_begin):
        if len(picked) == num_to_select:
            print(picked)

        for i in range(i_begin, len(cand)):
            picked.append(cand[i])
            self.dfs(picked, cand, num_to_select, i + 1)
            picked.pop()

def main():
    all_heights = []
    for _ in range(9):
        height = int(input())
        all_heights.append(height)

if __name__ == '__main__':
    main()
