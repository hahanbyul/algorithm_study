from TRAVERSAL import Traversal
from TRAVERSAL import Node

def test_split_midorder():
    tree = Traversal([], [])
    assert tree.split_midorder([1,2,3,4], 3) == ([1,2], [4])
    assert tree.split_midorder([1,2,3,4], 4) == ([1,2,3], [])

def test_add_child_baseline():
    tree = Traversal([1, 2, 4, 3], [2, 4, 1, 3])
    assert tree.add_child([]) == None
    assert tree.add_child([2, 3, 4]) == None  # CASE: root is not in subset

def test_add_child():
    tree = Traversal([0, 1, 2], [2, 1, 0])
    node = tree.add_child([2, 1, 0])
    assert node.num == 0 and node.left.num == 1 and node.left.left.num == 2

    tree = Traversal([1, 2, 4, 3], [2, 4, 1, 3])
    node = tree.add_child([2, 4, 1, 3])
    assert node.num == 1 and node.left.num == 2 and node.right.num == 3 and node.left.right.num == 4

def test_postorder():
    tree = Traversal([1, 2, 4, 3], [2, 4, 1, 3])
    node = tree.add_child([2, 4, 1, 3])
    assert tree.postorder(node, []) == [4, 2, 3, 1]


