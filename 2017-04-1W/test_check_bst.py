from CHECK_BST import Check_BST
from CHECK_BST import Node

strings = "3 2 4\n0 0 5\n4 5 2\n0 0 1\n0 0 3"
check = Check_BST(5)
check.read_string(strings)

strings2 = "0 0 2\n4 3 3\n1 0 3\n0 0 1"
check2 = Check_BST(4)
check2.read_string(strings2)

strings3 = "2 3 3\n0 4 1\n0 0 4\n0 0 3"
check3 = Check_BST(4)
check3.read_string(strings3)

def test_find_root():
    #Node.children = set([1, 2, 3, 4])
    #assert Node.find_root(None, 5) == 5
    #assert Node.find_root(None, 10) == None

    assert check.find_root(5) == 1
    assert check2.find_root(4) == 2

def test_is_bst():
    assert check.is_bst() == True
    assert check2.is_bst() == False
    assert check3.is_bst() == False
