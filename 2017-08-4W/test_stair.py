from STAIR import Stair

stair = Stair(6)
stair.score = [0,10,20,15,25,10,20]

def test_step():
    print(max(stair.solve(0), stair.solve(1)))

def test_ex():
    print(stair.solve(0))

