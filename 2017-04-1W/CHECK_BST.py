class Node:
    children = set()
    def __init__(self, string):
        self.L, self.R, self.K = [int(i) for i in string.split()]
        if self.L != 0: Node.children.add(self.L)
        if self.R != 0: Node.children.add(self.R)

    def find_root(self, N):
        root = set(range(1, N+1)).difference(Node.children)
        return root.pop() if len(root) == 1 else None

    def is_bst(self, node_list):
        if self.L == 0 and self.R == 0:
            return True

        ret = True
        left  = node_list[self.L-1]
        right = node_list[self.R-1]
        ret = ret and left.K < self.K and right.K > self.K and left.is_bst(node_list) and right.is_bst(node_list)
        return ret

def main():
    node_list = list()

    C = int(input())
    for _ in range(C):

        N = int(input())
        for _ in range(N):
            node_list.append(Node(input()))

        root = Node.find_root(None, N)
        if root == None:
            print("NO")
            continue

        if node_list[root].is_bst(node_list):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()
