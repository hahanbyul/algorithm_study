class HiddenNumber:
    def __init__(self, problem):
        self.problem = problem

    def isalpha(self, char):
        return char.isalpha()

    def isdigit(self, char):
        return char.isdigit()

    def find_end(self, compare, seq, begin):
        it = begin + 1
        while it < len(seq) and compare(seq[it]):
            it += 1
        return it

    def find_end_idx_of_number_seq(self, seq, begin):
        return self.find_end(self.isdigit, seq, begin)

    def find_end_idx_of_alpha_seq(self, seq, begin):
        return self.find_end(self.isalpha, seq, begin)

    def solve(self):
        seq = self.problem
        # print(f'seq: {seq}')
        begin = 0
        total_sum = 0

        while begin < len(seq):
            # print(f'begin: {begin}')
            if seq[begin].isalpha():
                end = self.find_end(self.isalpha, seq, begin)
            elif seq[begin].isdigit():
                end = self.find_end(self.isdigit, seq, begin)

                if end - begin <= 6:
                    hidden_num = int(seq[begin:end])
                    # print(hidden_num)
                    total_sum += hidden_num

            begin = end

        print(total_sum)
        return total_sum


def main():
    num = int(input())
    hn = HiddenNumber(input())
    hn.solve()

if __name__ == '__main__':
    main()
