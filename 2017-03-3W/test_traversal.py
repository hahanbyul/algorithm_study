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

def str2list(string):
    return [int(num) for num in string.split()]

def test_algospot_ex():
    assert str2list("9 12 16 27 36 54 72") == [9,12,16,27,36,54,72]
    preorders = [str2list("409 479 10 838 150 441"), str2list("27 16 9 12 54 36 72")]
    midorders = [str2list("409 10 479 150 838 441"), str2list("9 12 16 27 36 54 72")]

    tree = Traversal(preorders[0], midorders[0])
    node = tree.add_child(midorders[0])
    assert tree.postorder(node, []) == str2list("10 150 441 838 479 409")

    tree = Traversal(preorders[1], midorders[1])
    node = tree.add_child(midorders[1])
    assert tree.postorder(node, []) == str2list("12 9 16 36 72 54 27")
