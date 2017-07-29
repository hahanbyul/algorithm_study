from QUADTREE import Quadtree
from QUADTREE import Node

qt = Quadtree()

def test_node():
    n = Node('x')
    assert n.children == []
    n.add_child(Node('b'))
    n.add_child(Node('b'))
    n.add_child(Node('b'))
    n.add_child(Node('b'))
    n.add_child(Node('x'))

def test_make_tree_basecase():
    assert qt.make_tree('') == None
    assert qt.make_tree('b') == (Node('b'), '')

def test_ex0():
    root, _ = qt.make_tree('xbwwb')
    print(root)
    string = []
    qt.traverse_dfs(root, string) 
    assert ''.join(string) == 'xbwwb'

    print()
    string2 = []
    qt.traverse_opposite(root, string2)
    assert ''.join(string2) == 'xwbbw'
    
def test_ex1():
    root, _ = qt.make_tree('xbwxwbbwb')
    print(root)
    string = []
    qt.traverse_dfs(root, string) 

    print()
    string2 = []
    qt.traverse_opposite(root, string2)
    assert ''.join(string2) == 'xxbwwbbbw'

def test_ex2():
    root, _ = qt.make_tree('xxwwwbxwxwbbbwwxxxwwbbbwwwwbb')
    print(root)

    print()
    string2 = []
    qt.traverse_opposite(root, string2)
    assert ''.join(string2) == 'xxwbxwwxbbwwbwbxwbwwxwwwxbbwb'

def test_dfs():
    qt = Quadtree()
    qt.dfs(list(range(6)), 4, [], 0)

def test_print_3412():
    qt = Quadtree()
    qt.print_3412('bbww')
