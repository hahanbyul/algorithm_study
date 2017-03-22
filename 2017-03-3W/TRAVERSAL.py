class Node:
    def __init__(self, num):
        self.num   = num
        self.left  = None
        self.right = None

class Traversal:
    def __init__(self, preorder, midorder):
        self.preorder = preorder
        self.midorder = midorder
        self.cur_index = 0

    def print_postorder(self):
        tree = add_child(midorder)
        print(postorder(tree, []))

    def get_postorder(self):
        tree = add_child(midorder)
        return postorder(tree, [])

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

    def split_midorder(self, midorder, root):
        root_index = midorder.index(root)
        return midorder[:root_index], midorder[root_index+1:]
