class Node:
    children = set()
    def __init__(self, string):
        self.L, self.R, self.K = [int(i) for i in string.split()]
        if self.L != 0: Node.children.add(self.L)
        if self.R != 0: Node.children.add(self.R)

    def find_root(self, N):
        root = set(range(1, N+1)).difference(Node.children)
        return root.pop() if len(root) == 1 else None

def main():
    node_list = list()

    C = int(input())
    for _ in range(C):

        N = int(input())
        for _ in range(N):
            node_list.append(Node(input()))


if __name__ == '__main__':
    main()
