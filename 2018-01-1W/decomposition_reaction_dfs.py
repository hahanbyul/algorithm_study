# problem: http://www.acmicpc.net/problem/2197
import sys

class DecomReaction:
    def read_input(self, input_method):
        self.N, self.M = [int(x) for x in input_method().split()]
        self.tree = [[] for _ in range(self.N)]
        self.size = [1 for _ in range(self.N)]

        self.min_cut_with_root = [[float('inf') for _ in range(self.N+1)] for _ in range(self.N+1)]
        self.min_cut_without_root = [[float('inf') for _ in range(self.N+1)] for _ in range(self.N+1)]

        for _ in range(self.N-1):
            left_atom, right_atom = [int(x)-1 for x in input_method().split()]

            self.tree[left_atom].append(right_atom)
            self.tree[right_atom].append(left_atom)

    def dfs(self, node, parent):
        print(f'dfs: {node}')
        min_cut_with_root = self.min_cut_with_root
        min_cut_without_root = self.min_cut_without_root

        min_cut_with_root[node][0] = 1
        children = self.tree[node]
        min_cut_with_root[node][1] = len(children)-1
        if parent == -1:
            min_cut_with_root[node][1] = len(children)

        prev_child = -1
        for child in children:
            if child == parent:
                continue

            self.dfs(child, node)
            self.size[node] += self.size[child]

            for i in range(self.size[child]+1):
                print(f'i: {i}')
                min_cut_without_root[node][i] = min(min_cut_without_root[node][i], 1 + min_cut_with_root[child][i])
                min_cut_without_root[node][i] = min(min_cut_without_root[node][i], min_cut_without_root[child][i])
                print(f'without: {min_cut_without_root[node]}')

                if prev_child == -1:
                    prev_child = child
                    break

                for j in range(self.size[prev_child]+1):
                    print(f'j: {j}')
                    min_cut_with_root[node][i+j+1] = min(min_cut_with_root[node][i+j+1], min_cut_with_root[child][i] + min_cut_with_root[prev_child][j])
                    print(f'with: {min_cut_with_root[node]}')
            prev_child = child
        min_cut_with_root[node][self.size[node]] = 0

    def solve(self):
        dfs(0, -1)
        return min(min_cut_with_root[0][self.M], min_cut_without_root[0][self.M])


def main():
    dr = DecomReaction()
    dr.read_input(sys.stdin.readline)
    answer = dr.solve()
    print(answer)

if __name__ == '__main__':
    main()


