from TRIANGLEPATH import Trianglepath

def test_ex1():
    tp = Trianglepath()
    for line in '6\n1  2\n3  7  4\n9  4  1  7\n2  7  5  9  4'.split('\n'):
        print(line)
        tp.read_line(line)

    print(tp.max_path(4, 2))
    print(tp.cache)
    assert tp.solve(5) == 28

def test_ex2():
    tp = Trianglepath()
    for line in '1\n2 4\n8 16 8\n32 64 32 64\n128 256 128 256 128'.split('\n'):
        tp.read_line(line)

    assert tp.solve(5) == 341

