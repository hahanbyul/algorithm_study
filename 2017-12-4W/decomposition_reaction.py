class DecomReaction:
    def read_input(self, input_method):
        self.N, self.M = [int(x) for x in input_method().split()]
        self.connection = [[] for _ in range(self.N+1)]
        self.visited = [False for _ in range(self.N+1)]
        self.edges = []
        self.edges_to_index = {}

        for i in range(self.N-1):
            left_atom, right_atom = [int(x) for x in input_method().split()]
            edge = sorted((left_atom, right_atom))
            self.edges.append(edge)
            # self.edges_to_index[edge] = i

            self.connection[left_atom].append(right_atom)
            self.connection[right_atom].append(left_atom)

    def get_combinations(self, start, picked, remained, total):
        if remained == 0:
            print(picked)
            return picked

        for i in range(start, total):
            picked.append(i)
            self.get_combinations(i+1, picked, remained-1, total)
            picked.pop()

    def solve(self, M=None):
        if M is None:
            M = self.M

        # trivial cases
        if M == self.N or M == 0:
            return 0
        if M == 1:
            return 1
        
        answer = float('inf')
        for edge in self.edges:
            one, another = self.break_edge_and_count_connected(edge)
            if M == self.M:
                print(f'one: {one}, another: {another}')

            if one >= M:
                answer = min(answer, one)
            if another >= M:
                answer = min(answer, another)

            # if answer == M:
                # break

        answer = answer - M + 1
        return answer

    def solve3(self, M=None):
        if M is None:
            M = self.M

        queue = []
        cache = {}

        print(self.edges)
        for i, edge in enumerate(self.edges):
            print(f'i: {i}')
            print(f'edge: {edge}')

            left_atom, right_atom = edge
            one, another = self.break_edge_and_count_connected(edge)
            print(f'one: {one}, another: {another}')

            edge_list = i
            if one >= M:
                turnoff_list = right_atom
                queue.append(edge_list)
                cache[edge_list] = turnoff_list

            if another >= M:
                turnoff_list = left_atom
                queue.append(edge_list)
                cache[edge_list] = turnoff_list

            print(queue)


    def opposite_end(self, edge_index, one_end):
        left_atom, right_atom = self.edges[edge_index]
        return left_atom if right_atom == one_end else right_atom

    def break_edge_and_count_connected(self, edge):
        edge = sorted(edge)
        self.visited = [False for _ in range(self.N+1)]
        left_atom, right_atom = edge

        self.visited[right_atom] = True

        connected_atoms_left = self.count_connected(left_atom)
        ret = (connected_atoms_left, self.N - connected_atoms_left)
        self.cache = ret

        return ret

    # def break_edge_and_count_connected2(self, edge_indices):

    
    def count_connected(self, atom):
        self.visited[atom] = True
        ret = 1

        for next_atom in self.connection[atom]:
            if self.visited[next_atom]:
                continue

            ret += self.count_connected(next_atom)

        return ret

def main():
    dr = DecomReaction()
    dr.read_input(input)
    answer = dr.solve()

    print(answer)

if __name__ == '__main__':
    main()
