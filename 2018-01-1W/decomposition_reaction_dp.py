# problem: https://www.acmicpc.net/submit/2197

class DecomReaction:
    def read_input(self, input_method):
        self.N, self.M = [int(x) for x in input_method().split()]
        self.graph = [[] for _ in range(self.N)]
        self.tree  = [[] for _ in range(self.N)]
        self.vertex_count = [0 for _ in range(self.N)]
        self.subtree_count = [1 for _ in range(self.N)]

        for i in range(self.N-1):
            left_atom, right_atom = [int(x)-1 for x in input_method().split()]

            self.graph[left_atom].append(right_atom)
            self.graph[right_atom].append(left_atom)

            self.vertex_count[left_atom]  += 1
            self.vertex_count[right_atom] += 1

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


    def all_comb(self, start, children_num, goal, summed, picked, children=None, answer=None, root, root_cut):
        if start == children_num-1:
            ret = self.min_cut[root][root_cut]
            self.min_cut[root][root_cut] = min(ret, answer + self.solve(children[start], goal-summed))

        for num in range(goal+1):
            if summed + num > goal:
                continue

            picked.append(num)
            self.all_comb(start+1, children_num, goal, summed + num, picked, children, answer + self.solve(children[start], num), root, root_cut)
            picked.pop()

    def solve(self, node, cut, visited):
        if cut <= 1:
            return cut
        count = self.subtree_count[node]
        diff = count - cut
        if diff < 0:
            return float('inf')
        if 0 <= diff <= 1:
            return 1
        elif diff < cut:
            return self.solve(node, diff, visited)

        ret = cut
        children = self.tree[node]
        self.all_comb(0, len(children), cut, 0, [], children, 0)
        return self.min_cut[node][cut]

"""
