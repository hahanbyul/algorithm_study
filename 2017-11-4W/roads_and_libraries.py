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
        if self.cost_lib < self.cost_road:
            return self.num_city * self.cost_lib

        for num_lib in range(1, self.num_city):
            num_road = self.num_city - num_lib

            visited = [False for _ in range(self.num_city)]
            if self.is_possible_with_these(num_lib, num_road, visited):
                return num_lib * self.cost_lib + num_road * self.cost_road

        # if num_lib == num_city (not returned before)
        return self.num_city * self.cost_lib

    def is_possible_with_these(self, num_lib, num_road, visited):
        if num_road <= 0:
            return True if num_lib + num_road == 0 and all(visited) else False
        if num_lib == 0 and num_road == 0:
            return True if all(visited) else False

        for i, is_visited in enumerate(visited):
            if is_visited:
                continue

            remained_road = num_road - self.compute_how_many_cities_are_connected(i, visited)
            return self.is_possible_with_these(num_lib-1, remained_road, visited)

    def compute_how_many_cities_are_connected(self, city, visited):
        visited[city] = True

        sum_cities = 0
        for next_city, is_road in enumerate(self.road[city]):
            if not is_road or visited[next_city]:
                continue

            sum_cities += 1
            self.road[city][next_city] = False
            self.road[next_city][city] = False

            sum_cities += self.compute_how_many_cities_are_connected(next_city, visited)

        return sum_cities


def main():
    q = int(input().strip())
    for _ in range(q):
        ral = RoadsAndLibraries()
        ral.read_input()
        print(ral.solve())


if __name__ == '__main__':
    main()
