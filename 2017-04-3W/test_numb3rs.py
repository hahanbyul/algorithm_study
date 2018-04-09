from NUMB3RS import Numb3rs
import numpy as np

ex1_table = '0 1 1 1 0\n1 0 0 0 1\n1 0 0 0 0\n1 0 0 0 0\n0 1 0 0 0'
ex2_table = '0 1 1 1 0 0 0 0\n1 0 0 1 0 0 0 0\n1 0 0 1 0 0 0 0\n1 1 1 0 1 1 0 0\n0 0 0 1 0 0 1 1\n0 0 0 1 0 0 0 1\n0 0 0 0 1 0 0 0\n0 0 0 0 1 1 0 0'

def test_ex1():
    n = Numb3rs(5, 2, 0)
    n.read_table_as_string(ex1_table)
    assert n.trans == [[0, 1/3, 1/3, 1/3, 0], [1/2, 0, 0, 0, 1/2], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 1, 0, 0, 0]]
    Q = [0, 2, 4]
    print(n.get_answer(Q))

def test_ex2():
    n = Numb3rs(8, 2, 3)
    n.read_table_as_string(ex2_table)
    Q = [3,1,2,6]
    print(n.get_answer(Q))

def test_matmul():
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[2, 1], [0, 3]]
    assert Numb3rs.matmul(None, mat1, mat2) == [[2.0, 7.0], [6.0, 15.0]]

def test_matpower():
    n = Numb3rs(5, 2, 0)
    mat1 = [[1, 0], [0, 1]]
    assert n.matpower(mat1, 100) == [[1.0, 0.0], [0.0, 1.0]]

    n2 = Numb3rs(5, 2, 0)
    mat2 = [[2, 3, 2], [1, 6, 2], [5, 2, 4]]
    assert n2.matpower(mat2, 10) == np.linalg.matrix_power(np.array(mat2), 10).tolist()
