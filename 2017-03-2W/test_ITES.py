from ITES import ITES

def test_init():
    ites = ITES(5)
    assert ites.A == [1983, 8791, 4770, 7665, 3188]
