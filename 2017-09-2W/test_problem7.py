from problem7 import solution

def test_ex1():
    assert solution(["ba","na","n","a"], "banana") == 3

def test_ex2():
    assert solution(["app","ap","p","l","e","ple","pp"], "apple") == 2

def test_ex3():
    assert solution(["ba","an","nan","ban","n"], "banana") == -1
