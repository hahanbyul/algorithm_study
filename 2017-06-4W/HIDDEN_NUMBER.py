class HiddenNumber:
    def __init__(self, problem):
        self.problem = problem

    def isalpha(char):
        return char.isalpha()

    def isdigit(char):
        return char.isdigit()

    def find_end_idx_of_number_seq(self, seq, begin):
        it = begin + 1
        while it < len(seq) and seq[it].isdigit():
            it += 1
        return it

    def find_end_idx_of_alpha_seq(self, seq, begin):
        it = begin + 1
        while it < len(seq) and seq[it].isalpha():
            it += 1
        return it

    def solve(self):
        seq = self.problem
        print(f'seq: {seq}')
        begin = 0
        total_sum = 0

        while begin < len(seq):
            print(f'begin: {begin}')
            if seq[begin].isalpha():
                end = self.find_end_idx_of_alpha_seq(seq, begin)
            elif seq[begin].isdigit():
                end = self.find_end_idx_of_number_seq(seq, begin)
                if end - begin <= 6:
                    hidden_num = int(seq[begin:end])
                    print(hidden_num)
                    total_sum += hidden_num

            begin = end

        print(total_sum)
        return total_sum

def main():
    C = int(input())
    for _ in range(C):
        pass


if __name__ == '__main__':
    main()
