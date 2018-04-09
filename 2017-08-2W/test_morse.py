from MORSE import Morse

m = Morse()

def test_factorial():
    assert m.factorial(10) == 3628800
    assert m.factorial(4) == 24
    assert m.factorial(5) == 120
    assert m.factorial(0) == 1
    assert m.factorial(1) == 1
    print(m.factorial_cache)

def test_combination():
    assert m.get_comb_num(2, 2) == 6
    assert m.get_comb_num(1, 2) == 3
    print(m.get_comb_num(100, 100))

def test_solve():
    assert m.solve(2, 2, 1) == '--oo'
    assert m.solve(2, 2, 2) == '-o-o'
    assert m.solve(2, 2, 3) == '-oo-'
    assert m.solve(2, 2, 4) == 'o--o'
    assert m.solve(2, 2, 5) == 'o-o-'
    assert m.solve(2, 2, 6) == 'oo--'

    assert m.solve(4, 8, 13) == '--o-ooo-oooo'
    assert m.solve(6, 4, 1) == '------oooo'

def test_print_all_cases():
    # m.print_all_cases(2,2)
    # m.print_all_cases(4,8)
    m.print_all_cases(6,4)
