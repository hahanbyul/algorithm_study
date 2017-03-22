class Node:
    def __init__(self, num):
        self.num   = num
        self.left  = null
        self.right = null

class Traversal:
    def __init__(self, preorder, midorder):
        self.preorder = preorder
        self.midorder = midorder

    def postorder(self):
        root = Node(self.preorder[0])
        left_subset, right_subset = split_midorder(midorder, root)
        self.cur_index = 1

        root.left  = add_child(left_subset)
        root.right = add_child(right_subset)

    def add_child(self, subset):
        if not subset: 
            return null

        cur_num = self.preorder[self.cur_index]
        if not cur_num in subset:
            return null

        parent = Node(cur_num)
        self.cur_index += 1

        left_subset, right_subset = split_midorder(subset, parent)
        parent.left  = add_child(left_subset)
        parent.right = add_child(right_subset)

        return parent

    def split_midorder(self, midorder, root):
        root_index = midorder.index(root)
        return midorder[:root_index], midorder[root_index+1:]
