from KLIS import KLIS

def test_ex1():
    lis = KLIS()
    lis.read_seq('5 1 6 4 3 2 8 7')
    lis.solve(6)
    lis.solve2(6)

def test_ex2():
    lis = KLIS()
    lis.read_seq('2 1 4 3 6 5 8 7')
    lis.solve(4)
    lis.solve2(4)

def test_ex3():
    lis = KLIS()
    lis.read_seq('5 6 7 8 1 2 3 4')
    lis.solve(2)
    lis.solve2(2)

def test_calc_number():
    lis = KLIS()
    lis.choices = {-1: [0, 4], 0: [1], 1: [2], 4: [5,6], 5: [7], 6: [7]}
    lis.kth_seq(1, -1, [], 3) == [0, 1, 2]
    lis.kth_seq(2, -1, [], 3) == [4, 5, 7]
    lis.kth_seq(3, -1, [], 3) == [4, 6, 7]

def test_get_char():
    lis = KLIS()
    lis.choices = {-1: [0, 4], 0: [1], 1: [2], 4: [5,6], 5: [7], 6: [7]}
    assert lis.get_comb_num(0, 3) == 1
    assert lis.get_comb_num(4, 3) == 2
    assert lis.get_comb_num(-1, 4) == 3


