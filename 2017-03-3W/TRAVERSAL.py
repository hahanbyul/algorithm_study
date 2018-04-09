class Node:
    def __init__(self, num):
        self.num   = num
        self.left  = None
        self.right = None

class Traversal:
    def __init__(self, preorder, inorder):
        self.preorder = preorder
        self.inorder = inorder
        self.cur_index = 0

    def print_postorder(self):
        node = self.add_child(self.inorder)
        print(" ".join([str(i) for i in self.postorder(node, [])]))

    def get_postorder(self):
        node = self.add_child(self.inorder)
        return self.postorder(node, [])

    def postorder(self, root, seq):
        if root == None:
            return

        self.postorder(root.left, seq)
        self.postorder(root.right, seq)
        if root.num != None:
            seq.append(root.num)
        return seq

    def add_child(self, subset):
        if not subset: 
            return None

        cur_num = self.preorder[self.cur_index]
        if not cur_num in subset:
            return None

        parent = Node(cur_num)
        self.cur_index += 1

        left_subset, right_subset = self.split_midorder(subset, cur_num)
        parent.left  = self.add_child(left_subset)
        parent.right = self.add_child(right_subset)

        return parent

    def split_midorder(self, inorder, root):
        root_index = inorder.index(root)
        return inorder[:root_index], inorder[root_index+1:]

def str2list(string):
    return [int(num) for num in string.split()]

def main():
    C = int(input())
    for _ in range(C):
        N = int(input())
        preorder = str2list(input())
        inorder  = str2list(input())
        tr = Traversal(preorder, inorder)
        tr.print_postorder()

if __name__ == '__main__':
    main()
