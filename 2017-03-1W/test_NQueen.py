from NQUEEN import NQUEEN

def test_print():
    nqueen = NQUEEN(4)
    assert nqueen.to_board([]) == []
    assert nqueen.to_board([0,1,2,3]) == ["Q...", ".Q..", "..Q.", "...Q"]
    assert nqueen.to_board([3,1,2,0]) == ["...Q", ".Q..", "..Q.", "Q..."]

def test_is_diag():
    nqueen = NQUEEN(4)
    assert nqueen.is_diag([1, 3], 2) == True
    assert nqueen.is_diag([1, 3], 0) == False
    assert nqueen.is_diag([1, 3, 0], 2) == False
    assert nqueen.is_diag([1, 3, 0], 0) == False

def test_no_answer():
    nqueen = NQUEEN(2)
    assert nqueen.answers == []
    nqueen2 = NQUEEN(3)
    assert nqueen.answers == []

def test_answer():
    nqueen = NQUEEN(4)
    assert nqueen.answers == [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]

def test_answer2():
    nqueen = NQUEEN(6)
    print(nqueen.answers)
    assert True
    
