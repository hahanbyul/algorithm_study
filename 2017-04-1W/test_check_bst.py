from CHECK_BST import Node

def test_find_root():
    Node.children = set([1, 2, 3, 4])
    assert Node.find_root(None, 5) == 5
    assert Node.find_root(None, 10) == None

