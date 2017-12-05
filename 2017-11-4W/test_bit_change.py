from bit_change import compute_zero_to_next_carry
from bit_change import count_zero

def test_bit_format():
    print('{0:b}'.format(38))
    print(bin(38)+bin(1))

def test_compute_zero_to_next_carry():
    print(compute_zero_to_next_carry(8))

def test_count_zero():
    assert count_zero('1000') == 3
    assert count_zero('1001') == 0
    assert count_zero('10010010') == 1
    assert count_zero('00') == 2
