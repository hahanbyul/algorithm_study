from ITES import ITES

def test_init():
    ites = ITES(5)
    assert ites.A == [1983, 8791, 4770, 7665, 3188]

def test_find():
    ites = ITES(5)
    assert ites.find_seq([1,4,2,1,4,3,1,6], 7) == {(1,4,2) , (4,2,1) , (2,1,4), (4,3), (1,6)}

