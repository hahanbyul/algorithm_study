from SELF_NUMBER import Self_number

s = Self_number()

def test_get_num_with_same_last_digit():
    assert set(s.get_same_last_digit(1))   == set([1])
    assert set(s.get_same_last_digit(11))  == set([11, 101, 1001])
    assert set(s.get_same_last_digit(123)) == set([123, 213, 1023, 2013, 1203, 2103])

def test_get_num_with_0_last_digit():
    assert set(s.get_0_last_digit(1))    == set([10, 100, 1000])
    assert set(s.get_0_last_digit(11))   == set([110, 1100, 1010])
    assert set(s.get_0_last_digit(123))  == set([1230, 1320, 2130, 2310, 3120, 3210])
    assert set(s.get_0_last_digit(1234)) == set([])

def test_sum_digits():
    assert s.sum_digits(132) == 6
    assert s.sum_digits(9900) == 18
