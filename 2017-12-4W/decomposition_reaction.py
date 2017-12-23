class DecomReaction:
    def read_input(self, input_method):
        self.N, self.M = [int(x) for x in input_method().split()]
        self.connection = [[] for _ in range(self.N+1)]
        self.visited = [False for _ in range(self.N+1)]
        self.edges = []

        for _ in range(self.N-1):
            left_atom, right_atom = [int(x) for x in input_method().split()]
            self.edges.append((left_atom, right_atom))
            self.connection[left_atom].append(right_atom)
            self.connection[right_atom].append(left_atom)

    def solve(self):
        # trivial cases
        if self.M == self.N or self.M == 0:
            return 0
        if self.M == 1:
            return 1
        
        answer = float('inf')
        for edge in self.edges:
            one, another = self.break_edge_and_count_connected(edge)

            if one >= self.M:
                answer = min(answer, one)
            if another >= self.M:
                answer = min(answer, another)

            if answer == self.M:
                break

        answer = answer - self.M + 1
        return answer

    def break_edge_and_count_connected(self, edge):
        self.visited = [False for _ in range(self.N+1)]
        left_atom, right_atom = edge
        self.visited[right_atom] = True
        connected_atoms_left = self.count_connected(left_atom)
        return connected_atoms_left, self.N - connected_atoms_left
    
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
