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

                for j in range(1, self.size[node]-i+1):
                    if i + j < 2:
                        continue
                    ret[i+j] = min(ret[i+j], min_cut_with_root[child][i] + min_cut_with_root[node][j] - 1)

                min_cut_with_root[node] = ret

            is_first_child = False


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


