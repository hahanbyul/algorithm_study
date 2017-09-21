class Equal:
    def __init__(self, initial):
        self.array = initial
        self.cache = {}

    @staticmethod
    def sub_min(array):
        min_val = min(array)
        for i in range(len(array)):
            array[i] -= min_val
        return array

    @staticmethod
    def inc_1_except_0(array):
        for i in range(len(array)):
            if array[i] == 0:
                continue
            array[i] += 1
        return array

    def compute_add_times(self, candy):
        if candy == 0:
            return 0

        if self.cache.get(candy, False):
            return self.cache[candy]

        add_5  = candy // 5
        remain = candy %  5
        add_2  = remain // 2
        add_1  = remain %  2

        answer = add_5 + add_2 + add_1
        self.cache[candy] = answer

        return answer

    def sum_count(self, array):
        ret = 0
        for x in self.array:
            ret += self.compute_add_times(x)

        return ret

    @staticmethod
    def count_zero(array):
        ret = 0
        for x in array:
            if x == 0:
                ret += 1

        return ret

    def solve(self):
        array = self.sub_min(self.array)
        answer = self.sum_count(array)

        zero_num = self.count_zero(array)
        for i in range(1, 5):
            self.inc_1_except_0(array)
            answer = min(answer, zero_num * self.compute_add_times(i) + self.sum_count(array))

        return answer

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        initial = [int(x) for x in input().split()]

        eq = Equal(initial)
        print(eq.solve())

if __name__ == '__main__':
    main()

