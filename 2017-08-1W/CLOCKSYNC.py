# https://algospot.com/judge/problem/read/CLOCKSYNC
class Clocksync:
    def __init__(self):
        self.switch = {0: (0, 1, 2), \
                1: (3, 7, 9, 11), \
                2: (4, 10, 14, 15), \
                3: (0, 4, 5, 6, 7), \
                4: (6, 7, 8, 10, 12), \
                5: (0, 2, 14, 15), \
                6: (3, 14, 15), \
                7: (4, 5, 7, 14, 15), \
                8: (1, 2, 3, 4, 5), \
                9: (3, 4, 5, 9, 13)}

        self.answer = tuple([12] * 16)

    def solve(self, problem):
        return self.bfs(tuple([int(i) for i in problem.split()]))

    def bfs(self, problem):
        visited = {}
        queue = []
        queue.append((problem, 0))

        while len(queue) > 0:
            cur_state, distance = queue.pop(0)
            # print(f'state: {cur_state}, dist: {distance}')
            if cur_state == self.answer:
                return distance
            if distance > 30:
                return -1

            # print(f'next: {self.get_next(cur_state)}')
            for next_state in self.get_next(cur_state):
                if not visited.get(next_state, False):
                    queue.append((next_state, distance + 1))
                    visited[next_state] = True
            # print(f'q: {queue}')

    def get_next(self, cur_state):
        next_state_list = []
        for switch_num, indices in enumerate(self.switch.values()):
            # if any([cur_state[i] != 12 for i in indices]):
            next_state = self.push_switch(cur_state, switch_num)
            next_state_list.append(next_state)

        return next_state_list

    def push_switch(self, cur_state, switch_num):
        next_state = list(cur_state)
        for i in self.switch[switch_num]:
            next_state[i] += 3
            if next_state[i] == 15:
                next_state[i] = 3

        return tuple(next_state)


def main():
    C = int(input())
    cs = Clocksync()
    for _ in range(C):
        clocks = tuple([int(i) for i in input().split()])
        print(cs.bfs(clocks))

if __name__ == '__main__':
    main()
