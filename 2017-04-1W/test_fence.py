from FENCE import Fence

f1 = Fence(7, "7 1 5 9 6 7 3")
f2 = Fence(5, "1 1 1 3 4")
f3 = Fence(6, "1 3 3 3 3 3")
f4 = Fence(6, "1 4 4 4 4 1 1")
f5 = Fence(4, "1 8 2 2")

def test_find_max_cont_fences():
    assert f1.find_max_continuous_fences(f1.fences, 1) == 7
    assert f1.find_max_continuous_fences(f1.fences, 7) == 1
    assert f1.find_max_continuous_fences(f1.fences, 6) == 3
    assert f1.find_max_continuous_fences(f1.fences, 5) == 4
    assert f1.find_max_continuous_fences(f1.fences, 3) == 5

    assert f2.find_max_continuous_fences(f2.fences, 1) == 5
    assert f2.find_max_continuous_fences(f2.fences, 4) == 1
    assert f2.find_max_continuous_fences(f2.fences, 4) == 1

def test_make_smaller_fence():
    assert f1.make_smaller_fence(f1.fences, 1) == f1.fences
    assert f1.make_smaller_fence(f1.fences, 7) == [7, 0, 9, 0, 7, 0]
    assert f1.make_smaller_fence(f1.fences, 3) == [7, 0, 5, 9, 6, 7, 3]
    assert f1.make_smaller_fence(f1.fences, 9) == [9, 0]

def test_foo():
    assert f2.foo(f2.fences, 1, 1) == 5
    assert f2.foo(f2.fences, 2, 3) == 6
    assert f3.foo(f3.fences, 1, 3) == 15

def test_max_rect_fast():
    assert f1.max_rect_fast() == 20
    assert f2.max_rect_fast() == 6
    assert f3.max_rect_fast() == 15
    assert f4.max_rect_fast() == 16
    assert f5.max_rect_fast() == 8

