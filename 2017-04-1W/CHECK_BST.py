class Check_BST:
    def __init__(self, N):
        self.node_list = list()
        self.children = set()
        self.N = N

    def read_string(self, string):
        for s in string.split(sep="\n"):
            self.add_node(s)

    def add_node(self, string):
        node = Node(string)
        self.node_list.append(node)

        if node.L != 0:
            self.children.add(node.L)
        if node.R != 0:
            self.children.add(node.R)

    def find_root(self, N):
        root = set(range(1, N+1)).difference(self.children)
        return root.pop() if len(root) == 1 else None

    def is_bst(self):
        root_index = self.find_root(self.N)
        if root_index is None:
            return False

        root = self.node_list[root_index-1]
        if root.is_bst(self.node_list, list()):
            return True
        else:
            return False


class Node:
    def __init__(self, string):
        self.L, self.R, self.K = [int(i) for i in string.split()]

    def __repr__(self):
        return "(%d, %d, %d)" % (self.L, self.R, self.K)

    def is_bst(self, node_list, key_list):
        if self.K in key_list:
            return False
        key_list.append(self.K)

        if self.L == 0 and self.R == 0:
            return True

        ret = True
        if self.L != 0:
            left = node_list[self.L-1]
            ret = ret and left.K < self.K and left.is_bst(node_list, key_list)

        if self.R != 0:
            right = node_list[self.R-1]
            ret = ret and right.K > self.K and right.is_bst(node_list, key_list)

        return ret


def main():
    C = int(input())
    for _ in range(C):

        N = int(input())
        check = Check_BST(N)

        for _ in range(N):
            check.add_node(input())

        if check.is_bst():
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()
