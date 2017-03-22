from TRAVERSAL import Traversal

def test_split_midorder():
    tree = Traversal([], [])
    assert tree.split_midorder([1,2,3,4], 3) == ([1,2], [4])
    assert tree.split_midorder([1,2,3,4], 4) == ([1,2,3], [])
