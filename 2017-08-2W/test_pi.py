from PI import Pi


def test_combinations():
    pi = Pi()
    pi.dfs([], 8)
    pi.dfs([], 10)
    pi.dfs([], 12)

def test_difficulty():
    pi = Pi()
    assert pi.score('333') == 1
    assert pi.score('5555') == 1

    assert pi.score('23456') == 2
    assert pi.score('3210') == 2

    assert pi.score('323') == 4
    assert pi.score('54545') == 4

    assert pi.score('147') == 5
    assert pi.score('8642') == 5

def test_ex1():
    pi = Pi()
    pi.string = '12341234'
    assert pi.solve(0) == 4

def test_ex2():
    pi = Pi()
    pi.string = '11111222'
    assert pi.solve(0) == 2

def test_ex3():
    pi = Pi()
    pi.string = '12122222'
    assert pi.solve(0) == 5

def test_ex4():
    pi = Pi()
    pi.string = '22222222'
    assert pi.solve(0) == 2

def test_ex5():
    pi = Pi()
    pi.string = '12673939'
    assert pi.solve(0) == 14
