from ITES import ITES

def test_init():
    ites = ITES(5)
    assert ites.A == [1983, 8791, 4770, 7665, 3188]

def test_find():
    ites = ITES(5)
    assert ites.find_seq(7, [1,4,2,1,4,3,1,6]) == {(1,4,2) , (4,2,1) , (2,1,4), (4,3), (1,6)}

def test_A_find():
    K, N = (8791, 20)
    ites = ITES(N)
    assert len(ites.find_seq(K)) == 1

    K, N = (5265, 5000)
    ites = ITES(N)
    assert len(ites.find_seq(K)) == 4

"""
    K, N = (3578452, 5000000)
    ites = ITES(N)
    assert len(ites.find_seq(K)) == 1049
"""
