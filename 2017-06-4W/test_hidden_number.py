from HIDDEN_NUMBER import HiddenNumber

example = "ab13c9d07jeden"
def test_isdigit_method():
    assert "0".isdigit() == True
    assert "A".isdigit() == False

    assert example[0].isdigit() == False
    assert example[2].isdigit() == True

def test_isalpha_method():
    assert "a".isalpha() == True
    assert "A".isalpha() == True
    assert "0".isalpha() == False

def test_find_end_idx_of_number_seq():
    hn = HiddenNumber(example)
    assert hn.find_end_idx_of_number_seq(example, 2) == 4
    assert hn.find_end_idx_of_number_seq(example, 5) == 6
    assert hn.find_end_idx_of_number_seq(example, 7) == 9

    assert hn.find_end_idx_of_number_seq('ab012345bc', 2) == 8

    assert hn.find_end_idx_of_number_seq('ab01234', 2) == 7
    assert hn.find_end_idx_of_number_seq('ab012345', 2) == 8
    assert hn.find_end_idx_of_number_seq('ab0123456', 2) == 9

def test_find_end_idx_of_alpha_seq():
    hn = HiddenNumber(example)
    assert hn.find_end_idx_of_alpha_seq(example, 0) == 2
    assert hn.find_end_idx_of_alpha_seq(example, 4) == 5
    assert hn.find_end_idx_of_alpha_seq(example, 6) == 7
    assert hn.find_end_idx_of_alpha_seq(example, 6) == 7

    assert hn.find_end_idx_of_alpha_seq('asdf', 0) == 4

def test_solve():
    hn = HiddenNumber(example)
    hn.solve()

    hn = HiddenNumber('ab01233323bc323')
    hn.solve()

