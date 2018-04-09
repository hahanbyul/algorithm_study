import pprint as pp

class Picnic:
    def __init__(self, n, m):
        self.students_num = n
        self.friends_num  = m
        self.relationship = [[False for _ in range(n)] for _ in range(n)]

        self.cache = {}

    def read_friends(self, string):
        pairs = [int(i) for i in string.split()]
        for m in range(self.friends_num):
            i, j = pairs[2*m], pairs[2*m+1]
            self.relationship[i][j] = True
            self.relationship[j][i] = True

    def solve(self, picked):
        if len(picked) == self.students_num:
            # print(f'picked: {picked}')
            return 1

        # picked.sort()
        """
        if self.cache.get(tuple(sorted(picked)), False):
            return self.cache[tuple(sorted(picked]
        """

        for one in range(self.students_num):
            if one not in picked:
                break

        ret = 0
        for another, is_friend in enumerate(self.relationship[one]):
            if not is_friend or another in picked:
                continue

            picked.append(one)
            picked.append(another)

            answer = self.solve(picked)
            self.cache[tuple(sorted(picked))] = answer
            ret += answer
            
            picked.pop()
            picked.pop()

        return ret


def main():
    C = int(input())
    for _ in range(C):
        n, m = [int(i) for i in input().split()]
        p = Picnic(n, m)
        p.read_friends(input())

        print(p.solve([]))


if __name__ == '__main__':
    main()
