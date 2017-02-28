from NQUEEN import NQUEEN

def test_print():
    nqueen = NQUEEN(4)
    assert nqueen.to_board([0,1,2,3]) == ["Q...", ".Q..", "..Q.", "...Q"]
    assert nqueen.to_board([3,1,2,0]) == ["...Q", ".Q..", "..Q.", "Q..."]
