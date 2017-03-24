import itertools

class Self_number:
    def __init__(self):
        pass

    def get_same_last_digit(self, num):
        num_str = "%04d" % num
        perms = set(itertools.permutations([d for d in num_str[:-1]]))
        return [int("".join(d) + num_str[-1]) for d in perms]

    def get_0_last_digit(self, num):
        num_str = "%04d" % num
        if num_str[0] != "0":
            return []
        
        perms = set(itertools.permutations([d for d in num_str[1:]]))
        return [int("".join(d) + "0") for d in perms]

    def sum_digits(self, num):
        return sum([int(d) for d in str(num)])

    def iterate(self, arr, num_to_pick):
        self.arr = arr
        self.dfs(0, [], num_to_pick)

    def dfs(self, start, picked, num_to_pick):
        if num_to_pick == 0:
            print(picked)
            return

        for i in range(start, len(self.arr) - num_to_pick + 1):
            picked.append(self.arr[i])
            self.dfs(i+1, picked, num_to_pick-1)
            picked.pop()
