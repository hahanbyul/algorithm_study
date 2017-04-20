from NUMB3RS import Numb3rs

ex1_table = '0 1 1 1 0\n1 0 0 0 1\n1 0 0 0 0\n1 0 0 0 0\n0 1 0 0 0'
ex2_table = '0 1 1 1 0 0 0 0\n1 0 0 1 0 0 0 0\n1 0 0 1 0 0 0 0\n1 1 1 0 1 1 0 0\n0 0 0 1 0 0 1 1\n0 0 0 1 0 0 0 1\n0 0 0 0 1 0 0 0\n0 0 0 0 1 1 0 0'

def test_ex1():
    n = Numb3rs(5, 2, 0)
    n.read_table_as_string(ex1_table)
    assert n.trans.tolist() == [[0, 1/3, 1/3, 1/3, 0], [1/2, 0, 0, 0, 1/2], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 1, 0, 0, 0]]
    Q = [0, 2, 4]
    print(n.get_answer(Q).tolist())

def test_ex2():
    n = Numb3rs(8, 2, 3)
    n.read_table_as_string(ex2_table)
    Q = [3,1,2,6]
    print(n.get_answer(Q).tolist())

