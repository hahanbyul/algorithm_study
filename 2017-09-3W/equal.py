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
    def inc_1_except_0(array):
        for i in range(len(array)):
            if array[i] == 0:
                continue
            array[i] += 1
        return array

    @staticmethod
    def compute_add_times(candy):
        if candy == 0:
            return 0

        add_5  = candy // 5
        remain = candy %  5
        add_2  = remain // 2
        add_1  = remain %  2

        return add_5 + add_2 + add_1

    def sum_count(self, array):
        ret = 0
        for x in self.array:
            ret += self.compute_add_times(x)

        return ret

    def solve(self):
        array = self.sub_min(self.array)
        answer = self.sum_count(array)

        for i in range(1, 5):
            self.inc_1_except_0(array)
            answer = min(answer, self.compute_add_times(i) + self.sum_count(array))

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

