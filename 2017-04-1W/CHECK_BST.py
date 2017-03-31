class Check_BST:
    def __init__(self):
        self.node_list = list()
        self.children = set()

    def add_node(self, string):
        node = Node(string)
        self.node_list.append(node)

        if node.L != 0: self.children.add(node.L)
        if node.R != 0: self.children.add(node.R)

    def find_root(self, N):
        root = set(range(1, N+1)).difference(self.children)
        return root.pop() if len(root) == 1 else None

class Node:
    def __init__(self, string):
        self.L, self.R, self.K = [int(i) for i in string.split()]

    def is_bst(self, node_list):
        if self.L == 0 and self.R == 0:
            return True

        ret = True
        left  = node_list[self.L-1]
        right = node_list[self.R-1]
        ret = ret and left.K < self.K and right.K > self.K and left.is_bst(node_list) and right.is_bst(node_list)
        return ret

def main():

    C = int(input())
    for _ in range(C):

        N = int(input())
        check = Check_BST()

        for _ in range(N):
            check.add_node(input())

        root_index = check.find_root(N)
        if root_index == None:
            print("NO")
            continue

        root = check.node_list[root_index-1]
        if root.is_bst(check.node_list):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()
