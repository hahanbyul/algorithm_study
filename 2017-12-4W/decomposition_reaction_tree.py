# url: https://www.acmicpc.net/problem/2197

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

    def solve(self):
        root = self.vertex_count.index(1)
        visited = [False for _ in range(self.N+1)]
        self.count_subtree(root, visited)
        print(self.subtree_count)

        remainder = self.N - self.M
        if self.M in self.subtree_count or remainder in self.subtree_count:
            print(1)
            return 1

        array = [x for x in self.subtree_count if x < remainder]
        array.sort(reverse=True)

        answer = self.find_min_sum(array, remainder)
        print(answer)
        return answer

    def find_min_sum(self, array, goal):
        ret = float('inf')
        cache = {}
        for start in range(len(array)):
            min_sum = self.find_min_sum_(array, start, goal, cache)
            ret = min(ret, min_sum)

            if ret == 2:
                break
            if min_sum == float('inf'):
                break

        return ret

    def find_min_sum_(self, array, start, goal, cache):
        print(f'start: {start}, goal: {goal}, current: {array[start]}')
        if cache.get((start, goal), False):
            print('cached!!')
            return cache[(start, goal)]

        if start >= len(array):
            return float('inf')
        if array[start] == goal:
            return 1
        if array[start] > goal:
            # while start <= len(array) and array[start] <= goal:
                # start += 1
            return self.find_min_sum_(array, start+1, goal, cache)

        next_goal = goal - array[start]
        ret = float('inf')
        for next_start in range(start+1, len(array)):
            ret = min(ret, 1 + self.find_min_sum_(array, next_start, next_goal, cache))
        print(f'ret: {ret}')
        cache[(start, goal)] = ret
        return ret
