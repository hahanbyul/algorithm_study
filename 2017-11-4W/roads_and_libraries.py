#!/bin/python3
# problem url: https://www.hackerrank.com/challenges/torque-and-development/problem

class RoadsAndLibraries():
    def read_input(self):
        case_num = int(input().strip())
        for _ in range(case_num):
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

        for num_lib in range(1, self.num_city+1):
            num_road = self.num_city - num_lib

            if is_possible_with_these(num_lib, num_road):
                return num_lib * cost_lib + num_road * cost_road

    def is_possible_with_these(self, num_lib, num_road):
        return
