from equal import Equal

def test_sub_min():
    assert Equal.sub_min([1, 2, 3, 4]) == [0, 1, 2, 3]
    assert Equal.sub_min([1, 3, 3, 3]) == [0, 2, 2, 2]

def test_compute_add_times():
    eq = Equal([])
    assert eq.compute_add_times(7) == 2
    assert eq.compute_add_times(8) == 3
    assert eq.compute_add_times(9) == 3

def test_count_zero():
    assert Equal.count_zero([0, 0, 2, 3]) == 2
    assert Equal.count_zero([0, 0, 2, 3, 0]) == 3

def test_ex1():
    eq = Equal([2, 2, 3, 7])
    assert eq.solve() == 2

def test_ex2():
    eq = Equal([53,361,188,665,786,898,447,562,272,123,229,629,670,848,994,54,822,46,208,17,449,302,466,832,931,778,156,39,31,777,749,436,138,289,453,276,539,901,839,811,24,420,440,46,269,786,101,443,832,661,460,281,964,278,465,247,408,622,638,440,751,739,876,889,380,330,517,919,583,356,83,959,129,875,5,750,662,106,193,494,120,653,128,84,283,593,683,44,567,321,484,318,412,712,559,792,394,77,711,977,785,146,936,914,22,942,664,36,400,857])
    assert eq.solve() == 10605

def test_ex3():
    eq = Equal([520,862,10,956,498,956,991,542,523,664,378,194,76,90,753,868,837,830,932,814,616,78,103,882,452,397,899,488,149,108,723,22,323,733,330,821,41,322,715,917,986,93,111,63,535,864,931,372,47,215,539,15,294,642,897,98,391,796,939,540,257,662,562,580,747,893,401,789,215,468,58,553,561,169,616,448,385,900,173,432,115,712])
    assert eq.solve() == 8198

def test_basic_case():
    eq = Equal([6, 6, 6, 6])
    assert eq.solve() == 0

def test_special_case():
    eq = Equal([1, 9, 9])
    answer = eq.solve()
    print(answer)

def test_one_case():
    for x in range(10):
        eq = Equal([x])
        answer = eq.solve()
        print(answer)
