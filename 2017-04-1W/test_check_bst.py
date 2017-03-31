from CHECK_BST import Check_BST
from CHECK_BST import Node

def test_find_root():
    #Node.children = set([1, 2, 3, 4])
    #assert Node.find_root(None, 5) == 5
    #assert Node.find_root(None, 10) == None

    strings = "3 2 4\n0 0 5\n4 5 2\n0 0 1\n0 0 3"
    check = Check_BST()
    for s in strings.split(sep="\n"):
        check.add_node(s)
    assert check.find_root(5) == 1

    strings2 = "0 0 2\n4 3 3\n1 0 3\n0 0 1"
    check2 = Check_BST()
    for s in strings2.split(sep="\n"):
        check2.add_node(s)
    assert check2.find_root(4) == 2
