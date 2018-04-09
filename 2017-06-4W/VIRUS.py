# https://www.acmicpc.net/problem/2606

class Virus:
    def __init__(self, computer_num):
        self.vertex_num = computer_num
        self.network = [[False for _ in range(computer_num)] for _ in range(computer_num)]

    def connect(self, string):
        src, target = [int(i) for i in string.split(' ')]
        self.network[src-1][target-1] = True
        self.network[target-1][src-1] = True

    def bfs(self):
        queue = [0]
        visited = {}
        connected_com = [0 for _ in range(self.vertex_num)]

        while len(queue) > 0:
            here = queue.pop(0)
            # print(f'here: {here+1}')
        
            for there, is_connected in enumerate(self.network[here]):
                is_visited = visited.get((here, there), False)
                if is_connected and not is_visited:
                    # print(f'there: {there+1}')
                    queue.append(there)
                    connected_com[there] = 1
                    visited[(here, there)] = True
                    visited[(there, here)] = True

        return connected_com

    def solve(self):
        connected_com = self.bfs()
        ret = sum(connected_com)
        print(ret)
        return ret


def main():
    computer_num = int(input())
    v = Virus(computer_num)

    connected_num = int(input())
    for _ in range(connected_num):
        v.connect(input())

    v.solve()

if __name__ == '__main__':
    main()
