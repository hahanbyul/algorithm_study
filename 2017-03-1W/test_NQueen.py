from NQUEEN import NQUEEN

def test_print():
    nqueen = NQUEEN(4)
    assert nqueen.to_board([0,1,2,3]) == ["Q...", ".Q..", "..Q.", "...Q"]
    assert nqueen.to_board([3,1,2,0]) == ["...Q", ".Q..", "..Q.", "Q..."]

def test_check_diag():
    nqueen = NQUEEN(4)
    assert nqueen.check_diag([1, 3], 2) == True
    assert nqueen.check_diag([1, 3], 0) == False

