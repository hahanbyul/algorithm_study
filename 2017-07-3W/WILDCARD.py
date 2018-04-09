# https://algospot.com/judge/problem/read/WILDCARD
import string

class Wildcard:
    def __init__(self):
        pass

    @staticmethod
    def find_word_indices(pattern):
        if pattern == '':
            return 0, 0

        # 1. skip wildcard chars
        for i, char in enumerate(pattern):
            if char in string.ascii_letters or char in string.digits:
                break
        begin = i

        # 2. skip letters
        while i < len(pattern):
            if pattern[i] == '*' or pattern[i] == '?':
                break
            i += 1
        end = i
        return begin, end

    def solve(self, problem, pattern):
        # print(f'problem: {problem}, pattern: {pattern}')
        begin, end = self.find_word_indices(pattern)
        if begin == len(pattern)-1 and end == len(pattern)-1:
            return True
        if len(problem) == 0 and len(pattern) == 0:
            return True
        if len(pattern) == 0 and len(problem) > 0:
            return False

        if pattern[0] == '?':
            answer = self.solve(problem[1:], pattern[1:])
        elif pattern[0] == '*':
            start_idx = 0
            while start_idx < len(problem):
                result = problem.find(pattern[begin:end], start_idx)
                if result == -1:
                    return False
                length = end - begin
                answer = self.solve(problem[result + length:], pattern[end:])
                if answer:
                    return True
                start_idx = result + length
        else:
            if problem[:end] == pattern[:end]:
                answer = self.solve(problem[end:], pattern[end:])
            else:
                return False

        return answer


def main():
    w = Wildcard()
    C = int(input())
    for _ in range(C):
        pattern = input()
        N = int(input())
        answers = []
        for _ in range(N):
            problem = input()
            if w.solve(problem, pattern):
                answers.append(problem)

        answers.sort()
        for answer in answers:
            print(answer)



if __name__ == '__main__':
    main()
