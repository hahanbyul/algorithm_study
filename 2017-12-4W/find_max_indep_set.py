# url: https://www.acmicpc.net/problem/2213

class FindMaxIndepSet:
    def __init__(self):
        self.cache = {}

    def read_input(self, input_method=None):
        if input_method is None:
            input_method = input

        N = int(input_method())
        self.N = N

        self.weight = [0] + [int(w) for w in input_method().split()]
        
        self.visited = [False for _ in range(N+1)]

        self.tree = [[] for _ in range(N+1)]
        for _ in range(N-1):
            one, the_other = [int(x) for x in input_method().split()]
            self.tree[one].append(the_other)
            self.tree[the_other].append(one)

    def solve(self):
        self.tree[0].append(1)
        max_size, max_indep_set = self.solve_(node=0, is_this_node_included=False)
        max_indep_set.sort()

        print(max_size)
        print(" ".join([str(x) for x in max_indep_set]))

    def get_bigger_answer(self, one, another):
        if one[0] >= another[0]:
            return one
        else:
            return another

    def sum_children_answers(self, parent, is_parent_included):
        max_size = self.weight[parent] if is_parent_included else 0
        max_list = [parent] if is_parent_included else []

        INCLUDED = True

        children = self.tree[parent]
        for child in children:
            if self.visited[child]:
                continue

            not_included_answer = self.solve_(child, not INCLUDED)

            if is_parent_included:
                bigger_answer = not_included_answer
            else:
                included_answer = self.solve_(child, INCLUDED)
                bigger_answer = self.get_bigger_answer(not_included_answer, included_answer)
            max_size += bigger_answer[0]
            max_list += bigger_answer[1]

            self.visited[child] = False

        return (max_size, max_list)

    def solve_(self, node, is_this_node_included):
        if self.cache.get((node, is_this_node_included), False):
            return self.cache[(node, is_this_node_included)]

        self.visited[node] = True

        answer = self.sum_children_answers(node, is_this_node_included)

        self.cache[(node, is_this_node_included)] = answer
        return answer


def main():
    fmis = FindMaxIndepSet()
    fmis.read_input()
    fmis.solve()


if __name__ == '__main__':
    main()
