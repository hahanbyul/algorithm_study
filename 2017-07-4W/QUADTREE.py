class Node:
    def __init__(self, char):
        self.char = char
        if char == 'x':
            self.children = []

    def __eq__(self, another):
        return self.char == another.char

    def __repr__(self):
        if self.char != 'x':
            return self.char
        else:
            return 'x - [%s %s %s %s]' % tuple(self.children)

    def add_child(self, node):
        if self.char == 'x' and len(self.children) < 4:
            self.children.append(node)

class Quadtree:
    def make_tree(self, string):
        if len(string) < 1:
            return

        char = string[0]
        root = Node(char)
        if char == 'x':
            substring = string[1:]
            for _ in range(4):
                child, substring = self.make_tree(substring)
                root.add_child(child)
            return root, substring
        else:
            return root, string[1:]

    def traverse_dfs(self, root, picked):
        # print(root.char, end='')
        picked.append(root.char)

        if root.char == 'x':
            for child in root.children:
                self.traverse_dfs(child, picked)

    def traverse_opposite(self, root, picked):
        # print(root.char, end='')
        picked.append(root.char)

        if root.char == 'x':
            for i in [2, 3, 0, 1]:
                self.traverse_opposite(root.children[i], picked)


def main():
    C = int(input())
    for _ in range(C):
        qt = Quadtree()
        root, _ = qt.make_tree(input())
        answer = []
        qt.traverse_opposite(root, answer)
        print(''.join(answer))


if __name__ == '__main__':
    main()
