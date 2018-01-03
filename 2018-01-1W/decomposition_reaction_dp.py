# problem: https://www.acmicpc.net/submit/2197

class DecomReaction:
    def read_input(self, input_method):
        self.N, self.M = [int(x) for x in input_method().split()]
        self.connection = [[] for _ in range(self.N)]
        self.vertex_count = [0 for _ in range(self.N)]
        self.subtree_count = [1 for _ in range(self.N)]

        for i in range(self.N-1):
            left_atom, right_atom = [int(x)-1 for x in input_method().split()]

            self.connection[left_atom].append(right_atom)
            self.connection[right_atom].append(left_atom)

            self.vertex_count[left_atom]  += 1
            self.vertex_count[right_atom] += 1

    def count_subtree(self, node, visited):
        visited[node] = True

        children = self.connection[node]
        for child in children:
            if visited[child]:
                continue

            self.subtree_count[node] += self.count_subtree(child, visited)
            visited[child] = False

        return self.subtree_count[node]

    def solve(self, root, node, cut, visited):
        visited[node] = True

        count = self.subtree_count[node]
        diff = count - cut
        if 0 <= diff <= 1:
            return 1
        elif diff < cut:
            return self.min_cut[root][diff]

        children = self.connection[node]
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


    def all_comb(self, start, children_num, goal, summed, picked):
        if start == children_num-1:
            picked.append(goal-summed)
            print(picked)
            picked.pop()
            return

        for num in range(goal+1):
            if summed + num > goal:
                continue

            picked.append(num)
            self.all_comb(start+1, children_num, goal, summed + num, picked)
            picked.pop()

    def solve(self, node, cut, visited):
