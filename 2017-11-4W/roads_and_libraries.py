#!/bin/python3
# problem url: https://www.hackerrank.com/challenges/torque-and-development/problem

class RoadsAndLibraries():
    def read_input_file(self, filename):
        f = open(filename, 'r')
        n, m, x, y = f.readline().strip().split(' ')
        self.num_city, self.num_road, self.cost_lib, self.cost_road = [int(n), int(m), int(x), int(y)]

        # initialize graph
        self.library = [False for _ in range(self.num_city)]
        self.road    = [[False for _ in range(self.num_city)] for _ in range(self.num_city)]
        
        for a1 in range(self.num_road):
            city_1, city_2 = f.readline().strip().split(' ')
            city_1, city_2 = [int(city_1), int(city_2)]

            self.road[city_1-1][city_2-1] = True
            self.road[city_2-1][city_1-1] = True

    def read_input(self):
        n, m, x, y = input().strip().split(' ')
        self.num_city, self.num_road, self.cost_lib, self.cost_road = [int(n), int(m), int(x), int(y)]

        # initialize graph
        self.library = [False for _ in range(self.num_city)]
        self.road    = [[False for _ in range(self.num_city)] for _ in range(self.num_city)]
        
        for a1 in range(self.num_road):
            city_1, city_2 = input().strip().split(' ')
            city_1, city_2 = [int(city_1), int(city_2)]

            self.road[city_1-1][city_2-1] = True
            self.road[city_2-1][city_1-1] = True

    def solve(self):
        if self.cost_lib <= self.cost_road:
            return self.num_city * self.cost_lib

        num_lib = self.find_unions()
        num_road = self.num_city - num_lib
        return num_lib * self.cost_lib + num_road * self.cost_road

    def compute_how_many_cities_are_connected(self, start, visited):
        sum_cities = 0
        queue = []
        queue.append(start)
        visited[start] = True

        while len(queue) > 0:
            city = queue.pop()
            sum_cities += 1

            for next_city, is_road in enumerate(self.road[city]):
                if not is_road:
                    continue

                if not visited[next_city]:
                    visited[next_city] = True
                    queue.append(next_city)

                    self.road[city][next_city] = False
                    self.road[next_city][city] = False

        return sum_cities-1

    def find_unions(self):
        visited = [False for _ in range(self.num_city)]
        num_unions = 0

        for city, is_visited in enumerate(visited):
            if is_visited:
                continue

            self.compute_how_many_cities_are_connected(city, visited)
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
