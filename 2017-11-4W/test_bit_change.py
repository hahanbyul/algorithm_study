from bit_change import compute_array_advance
from bit_change import count_zero
from bit_change import count_one
from bit_change import compute_score
from bit_change import compute_odd_num
from bit_change import bit_change
from bit_change import bit_change_ref
from bit_change import next_change

def test_bit_format():
    print('{0:b}'.format(38))
    print(bin(38)+bin(1))

def test_cache():
    M = 10
    arr, _ = compute_array_advance(M)

    arr2 = [0 for _ in range(M+1)]
    for i in range(M+1):
        if i <= 1:
            arr2[i] = 0
            continue

        upper = 2 ** (i-1)
        arr2[i] = bit_change_ref(0, upper) - compute_odd_num(0, upper)

    assert arr == arr2

def test_count_zero():
    assert count_zero('1000') == 3
    assert count_zero('1001') == 0
    assert count_zero('10010010') == 1
    assert count_zero('00') == 2

def test_count_one():
    assert count_one('1111') == 4
    assert count_one('111111') == 6
    assert count_one('1000') == 0

def test_compute_score():
    arr = compute_array_advance(20)
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

def test_bit_change_ref():
    assert bit_change_ref(11, 15) == 7
    assert bit_change_ref(11, 16) == 12
    assert bit_change_ref(22, 25) == 6
    # assert bit_change_ref(220687542, 1053328179) == 1665281275

def test_bit_change_for_examples():
    assert bit_change(11, 15) == bit_change_ref(11, 15)
    assert bit_change(22, 25) == bit_change_ref(22, 25)
    assert bit_change(220687542, 1053328179) == 1665281275

def test_bit_change_for_range():
    for i in range(11, 100):
        print('================> (10, %d) <=================' % i)
        assert bit_change(10, i) == bit_change_ref(10, i)

def test_next_change():
    assert next_change('0') == 1
    assert next_change('1') == 2
    assert next_change('11111') == 6
