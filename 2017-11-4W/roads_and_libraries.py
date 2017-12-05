#!/bin/python3
# problem url: https://www.hackerrank.com/challenges/torque-and-development/problem

class RoadsAndLibraries():
    def read_input_file(self, filename):
        f = open(filename, 'r')
        n, m, x, y = f.readline().strip().split(' ')
        self.num_city, self.num_road, self.cost_lib, self.cost_road = [int(n), int(m), int(x), int(y)]
        self.initialize(self.num_city)

        for _ in range(self.num_road):
            city_1, city_2 = f.readline().strip().split(' ')
            city_1, city_2 = [int(city_1)-1, int(city_2)-1]

            self.union(city_1, city_2)

    def read_input(self):
        n, m, x, y = input().strip().split(' ')
        self.num_city, self.num_road, self.cost_lib, self.cost_road = [int(n), int(m), int(x), int(y)]
        self.initialize(self.num_city)

        for _ in range(self.num_road):
            city_1, city_2 = input().strip().split(' ')
            city_1, city_2 = [int(city_1)-1, int(city_2)-1]

            self.union(city_1, city_2)

    def initialize(self, N):
        self.count = N
        self.id = [i for i in range(N)]
        self.size = [1 for _ in range(N)]

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return

        if self.size[i] < self.size[j]:
            self.id[i] = j
            self.size[j] += self.size[i]
        else:
            self.id[j] = i
            self.size[i] += self.size[j]
        self.count -= 1

    def solve(self):
        if self.cost_lib <= self.cost_road:
            return self.num_city * self.cost_lib

        num_lib = self.find_unions()
        num_road = self.num_city - num_lib
        return num_lib * self.cost_lib + num_road * self.cost_road

    def find_unions(self):
        num_unions = 0

        for i in range(self.num_city):
            if i == self.id[i]:
                num_unions += 1

        return num_unions


def main():
    q = int(input().strip())
    for _ in range(q):
        ral = RoadsAndLibraries()
        ral.read_input()
        print(ral.solve())


if __name__ == '__main__':
    main()
