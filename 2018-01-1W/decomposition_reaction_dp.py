# problem: https://www.acmicpc.net/submit/2197

class DecomReaction:
    def read_input(self, input_method):
        self.N, self.M = [int(x) for x in input_method().split()]
        self.graph = [[] for _ in range(self.N)]
        self.tree  = [[] for _ in range(self.N)]
        self.subtree_count = [1 for _ in range(self.N)]

        self.min_cut_with_root = [[float('inf') for _ in range(self.N)] for _ in range(self.N)]
        self.min_cut_without_root = [[float('inf') for _ in range(self.N)] for _ in range(self.N)]

        for i in range(self.N-1):
            left_atom, right_atom = [int(x)-1 for x in input_method().split()]

            self.graph[left_atom].append(right_atom)
            self.graph[right_atom].append(left_atom)

    def construct_tree(self):
        visited = [False for _ in range(self.N)]
        self.root = 0
        self.add_child(self.root, visited)

    def add_child(self, node, visited):
        visited[node] = True
        children = self.graph[node]

        for child in children:
            if visited[child]:
                continue

            self.tree[node].append(child)
            self.add_child(child, visited)

    def count_subtree(self, node=None):
        if node is None:
            node = self.root

        children = self.tree[node]
        for child in children:
            self.subtree_count[node] += self.count_subtree(child)

        return self.subtree_count[node]

    def solve_without_root(self, node, cut):
        print(f'without_root ({node}, {cut})')
        count = self.subtree_count[node] 
        if count <= cut:
            print('answer: inf')
            return float('inf')

        ret = float('inf')
        children = self.tree[node]
        for child in children:
            ret = min(ret, 1 + self.solve_with_root(child, cut))
            ret = min(ret, self.solve_without_root(child, cut))

        print(f'answer: {ret}')
        return ret

    def solve_with_root(self, node, cut):
        print(f'with_root ({node}, {cut})')
        children = self.tree[node]
        if cut == 0:
            print('answer: 1')
            return 1
        if cut == 1:
            print(f'answer: {len(children)}')
            return len(children)
        count = self.subtree_count[node] 
        if count < cut:
            print('answer: inf')
            return float('inf')
        if count == cut:
            print('answer: 0')
            return 0

        self.solve_all_combination(0, cut-1, 0, 0, node, cut)
        print(f'answer: {self.min_cut_with_root[node][cut]}')
        return self.min_cut_with_root[node][cut]

    def solve_all_combination(self, start, goal, progress, answer, root, cut):
        children = self.tree[root]
        if start == len(children)-1:
            old_answer = self.min_cut_with_root[root][cut]
            new_answer = answer + self.solve_with_root(children[start], goal - progress)
            print(f'sum: {new_answer}')
            self.min_cut_with_root[root][cut] = min(old_answer, new_answer)
            return

        for step in range(goal+1):
            if progress + step > goal:
                continue
            delta = self.solve_with_root(children[start], step)
            self.solve_all_combination(start+1, goal, progress + step, answer + delta, root, cut)
