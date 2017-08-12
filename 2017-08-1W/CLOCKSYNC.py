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
        queue.append((tuple([0]*10), problem, 0))

        while len(queue) > 0:
            cur_switch, cur_state, distance = queue.pop(0)
            # print(f'switch: {cur_switch}, state: {cur_state}, dist: {distance}')
            if cur_state == self.answer:
                return distance
            if distance > 30:
                return -1

            switch_list, state_list = self.get_next(cur_switch, cur_state)
            for next_switch, next_state in zip(switch_list, state_list):
                if not visited.get(next_state, False):
                    queue.append((tuple(next_switch), next_state, distance + 1))
                    visited[next_state] = True
            # print(f'q: {queue}')

    def get_next(self, switch_state, cur_state):
        next_switch_list = []
        next_state_list   = []
        for switch_idx in range(10):
            next_switch = [switch_num for switch_num in switch_state]
            next_switch[switch_idx] += 1

            if next_switch[switch_idx] > 3:
                continue

            next_switch_list.append(next_switch)
            next_state = self.push_switch(cur_state, switch_idx)
            next_state_list.append(next_state)

        return next_switch_list, next_state_list

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
