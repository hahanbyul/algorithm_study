# problem: https://www.acmicpc.net/submit/2197

class DecomReaction:
    def read_input(self, input_method):
        self.N, self.M = [int(x) for x in input_method().split()]
        self.graph = [[] for _ in range(self.N)]
        self.tree  = [[] for _ in range(self.N)]
        self.subtree_count = [1 for _ in range(self.N)]
        self.min_cut = [[float('inf') for _ in range(self.N)] for _ in range(self.N)]
        self.visited = [[False for _ in range(self.N)] for _ in range(self.N)]

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

    """

    def solve(self, root, node, cut, visited):
        visited[node] = True

        count = self.subtree_count[node]
        diff = count - cut
        if 0 <= diff <= 1:
            return 1
        elif diff < cut:
            return self.min_cut[root][diff]

        children = self.graph[node]
        ret = cut
        for child in children:
            if visited[child]:
                continue
            if self.subtree_count[child] < cut:
                continue
            ret = min(ret, self.solve(root, child, cut, visited))

        if ret <= 2:
            return 

        self.solve_div(root, children, cut, 0, upper_bound)

    def solve_div(self, root, children, start, cut, summed, upper_bound):
        if start == len(children) and cut > 0:
            return float('inf')
        if upper_bound <= summed:
            return float('inf')

        child = children[start]
        
        ret = upper_bound
        for c in range(2, cut-1):
            ccc = self.min_cut[node][c]
            if ccc >= upper_bound-1:
                continue

            ret = min(ret, self.solve_div(root, children, start+1, cut - ccc, summed + ccc, upper_bound))


"""

    def solve(self, node, cut):
        print(f'node: {node}, cut: {cut}')
        if self.visited[node][cut]:
            print('cached!!')
            return self.min_cut[node][cut]

        self.visited[node][cut] = True

        count = self.subtree_count[node]
        if cut == 0:
            return 0
        if node <= self.N-1 and cut == 1:
            return 1

        if count < cut:
            return float('inf')
        if count == cut:
            return 1

        self.solve_all_combination(0, count - cut, 0, 0, node, cut)
        ret = self.min_cut[node][cut] + 1
        children = self.tree[node]
        for child in children:
            new_answer = self.solve(child, cut)
            print(f'new_answer: {new_answer}')
            ret = min(ret, new_answer)

        self.min_cut[node][cut] = ret
        return ret

    def solve_all_combination(self, start, goal, summed, answer, root, root_cut):
        children = self.tree[root]
        if start == len(children)-1:
            old_answer = self.min_cut[root][root_cut]
            new_answer = answer + self.solve(children[start], goal-summed)
            print(f'update ({root}, {root_cut}): {new_answer}')
            self.min_cut[root][root_cut] = min(old_answer, new_answer)
            return

        for num in range(goal+1):
            if summed + num > goal:
                continue

            self.solve_all_combination(start+1, goal, summed + num, answer + self.solve(children[start], num), root, root_cut)
