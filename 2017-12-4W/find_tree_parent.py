# url: https://www.acmicpc.net/problem/11725

class FindTreeParent:
    def read_input(self):
        N = int(input())
        self.N = N
        self.tree = [[] for _ in range(N+1)]

        for _ in range(N-1):
            one, the_other = [int(x) for x in input().split()]
            self.tree[one].append(the_other)
            self.tree[the_other].append(one)

    def solve(self):
        self.visited = [False for _ in range(self.N+1)]
        self.parent = {}
        self.queue = [1]

        while len(self.queue) != 0:
            node = self.queue.pop(0)
            self.find_children(node)

        for node in range(2, self.N+1):
            print(self.parent[node])

    def find_children(self, node):
        self.visited[node] = True
        childeren = self.tree[node]

        for child in childeren:
            if self.visited[child]:
                continue

            self.parent[child] = node
            self.queue.append(child)


def main():
    ftp = FindTreeParent()
    ftp.read_input()
    ftp.solve()

if __name__ == '__main__':
    main()
