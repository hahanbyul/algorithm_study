from bit_change import compute_zero_to_next_carry
from bit_change import compute_summed_array
from bit_change import count_zero
from bit_change import compute_score
from bit_change import compute_odd_num
from bit_change import bit_change

def test_bit_format():
    print('{0:b}'.format(38))
    print(bin(38)+bin(1))

def test_cache():
    arr = compute_zero_to_next_carry(40)
    print(arr)
    print(compute_summed_array(arr))

def test_count_zero():
    assert count_zero('1000') == 3
    assert count_zero('1001') == 0
    assert count_zero('10010010') == 1
    assert count_zero('00') == 2

def test_compute_score():
    arr = compute_zero_to_next_carry(20)
    string = '1111'
    assert compute_score(string, arr) == 16

    string = '1110'
    assert compute_score(string, arr) == 16

    string = '0101'
    assert compute_score(string, arr) == 5

    string = '0110'
    assert compute_score(string, arr) == 7

def test_odd_num():
    assert compute_odd_num(10, 15) == 3
    assert compute_odd_num(18, 25) == 4

def test_bit_change():
    assert bit_change(11, 15) == 7
    assert bit_change(11, 16) == 12
    assert bit_change(22, 25) == 6
    # assert bit_change(220687542, 1053328179) == 1665281275
