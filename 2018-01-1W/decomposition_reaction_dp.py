# problem: http://www.acmicpc.net/problem/2197
import sys

class DecomReaction:
    def read_input(self, input_method):
        self.N, self.M = [int(x) for x in input_method().split()]
        self.tree = [[] for _ in range(self.N)]
        self.subtree_count = [1 for _ in range(self.N)]

        self.min_cut_with_root = {}
        self.min_cut_without_root = {}

        for i in range(self.N-1):
            left_atom, right_atom = [int(x)-1 for x in input_method().split()]

            self.tree[left_atom].append(right_atom)
            self.tree[right_atom].append(left_atom)

    def count_subtree(self, node=None, visited=None):
        if node is None and visited is None:
            self.root = 0
            node = self.root
            visited = [False for _ in range(self.N)]

        visited[node] = True

        children = self.tree[node]
        new_children = []
        for child in children:
            if visited[child]:
                continue

            self.subtree_count[node] += self.count_subtree(child, visited)
            new_children.append(child)

        self.tree[node] = new_children

        return self.subtree_count[node]

    def solve_without_root(self, node, cut):
        if self.min_cut_without_root.get((node, cut), False):
            return self.min_cut_without_root[(node, cut)]

        count = self.subtree_count[node] 
        if count <= cut:
            self.min_cut_without_root[(node, cut)] = float('inf')
            return float('inf')

        ret = float('inf')
        children = self.tree[node]
        for child in children:
            ret = min(ret, 1 + self.solve_with_root(child, cut))
            ret = min(ret, self.solve_without_root(child, cut))

        self.min_cut_without_root[(node, cut)] = ret
        return ret

    def solve_with_root(self, node, cut):
        if self.min_cut_with_root.get((node, cut), False):
            return self.min_cut_with_root[(node, cut)]

        children = self.tree[node]
        if cut == 0:
            self.min_cut_with_root[(node, cut)] = 1
            return 1
        if cut == 1:
            self.min_cut_with_root[(node, cut)] = len(children)
            return len(children)

        count = self.subtree_count[node] 
        if count < cut:
            return float('inf')
        if count == cut:
            self.min_cut_with_root[(node, cut)] = 0
            return 0

        self.solve_all_combination(0, cut-1, 0, 0, node, cut)
        return self.min_cut_with_root[(node, cut)]

    def solve_all_combination(self, start, goal, progress, answer, root, cut):
        children = self.tree[root]
        if start == len(children)-1:
            old_answer = self.min_cut_with_root.get((root, cut), float('inf'))
            new_answer = answer + self.solve_with_root(children[start], goal - progress)
            self.min_cut_with_root[(root, cut)] = min(old_answer, new_answer)
            return

        for step in range(self.subtree_count[children[start]]+1):
            if progress + step > goal:
                continue
            delta = self.solve_with_root(children[start], step)
            self.solve_all_combination(start+1, goal, progress + step, answer + delta, root, cut)

    def solve(self):
        self.count_subtree()
        return min(self.solve_with_root(self.root, self.M), self.solve_without_root(self.root, self.M))


def main():
    dr = DecomReaction()
    dr.read_input(sys.stdin.readline)
    answer = dr.solve()
    print(answer)

if __name__ == '__main__':
    main()
