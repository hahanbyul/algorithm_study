import itertools

class Self_number:
    def __init__(self):
        is_self_number = [True  for i in range(10001)]
        is_visited     = [False for i in range(10001)]

    def compute_self_number(self, num):
        # cache is_visited
        same = self.get_same_last_digit(num)
        zero = self.get_0_last_digit(num)

        s_next = self.sum_digits(num)
        if num % 10 + s_next < 10:
            ret = self.get_cand(same, zero, self.sum_digits(num))
        else:
            ret = self.get_next_not_self_nums(same, s_next) + self.get_next_not_self_nums(zero, s_next)

        print()
        print(same, zero)
        print(ret)
        return ret

    def get_next_not_self_nums(self, num_list, sum_of_digits):
        return [num + sum_of_digits for num in num_list]

    def get_cand(self, same, zero, sum_of_digits):
        not_self_num_same = self.get_next_not_self_nums(same, sum_of_digits)
        not_self_num_zero = self.get_next_not_self_nums(zero, sum_of_digits)
        # cache not self num

        next_num = not_self_num_same[0]
        s_next = self.sum_digits(next_num)

        if next_num % 10 + s_next < 10:
            return not_self_num_same + not_self_num_zero + self.get_cand(not_self_num_same, not_self_num_zero, s_next)
        else:
            # cache not self num
            temp = self.sum_digits(not_self_num_same[0])
            return not_self_num_same + not_self_num_zero + self.get_next_not_self_nums(not_self_num_same, temp) + self.get_next_not_self_nums(not_self_num_zero, temp)

    def get_same_last_digit(self, num):
        num_str = "%04d" % num
        perms = set(itertools.permutations([d for d in num_str[:-1]]))
        return sorted([int("".join(d) + num_str[-1]) for d in perms])

    def get_0_last_digit(self, num):
        num_str = "%04d" % num
        if num_str[0] != "0" or num % 10 == 0:
            return []
        
        perms = set(itertools.permutations([d for d in num_str[1:]]))
        return sorted([int("".join(d) + "0") for d in perms])

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
