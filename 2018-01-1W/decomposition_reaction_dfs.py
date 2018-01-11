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


        is_first_child = True
        for child in children:
            if child == parent:
                continue

            self.dfs(child, node)
            self.size[node] += self.size[child]

            for i in range(1, self.size[child]+1):
                min_cut_without_root[node][i] = min(min_cut_without_root[node][i], 1 + min_cut_with_root[child][i])
                min_cut_without_root[node][i] = min(min_cut_without_root[node][i], min_cut_without_root[child][i])

                if is_first_child:
                    min_cut_with_root[node][i+1] = min_cut_with_root[child][i] + min_cut_with_root[node][1] - 1
                    continue

                ret = [x for x in min_cut_with_root[node]]

                print('before')
                print(f'with (child): {min_cut_with_root[child]}')
                print(f'with (node):  {min_cut_with_root[node]}')
                print(f'with (ret):   {ret}')

                for j in range(1, self.size[node]-i+1):
                    print(f'child: {child}, i: {i}, j: {j}')
                    if i + j < 2:
                        continue
                    ret[i+j] = min(ret[i+j], min_cut_with_root[child][i] + min_cut_with_root[node][j] - 1)

                print('after')
                print(f'with: {ret}')

                min_cut_with_root[node] = ret

            is_first_child = False

        print(f'without: {min_cut_without_root[node]}')
        print(f'with: {min_cut_with_root[node]}')
        print('dfs end')

    def solve(self):
        self.dfs(0, -1)
        return min(self.min_cut_with_root[0][self.M], self.min_cut_without_root[0][self.M])


def main():
    dr = DecomReaction()
    dr.read_input(sys.stdin.readline)
    answer = dr.solve()
    print(answer)

if __name__ == '__main__':
    main()


