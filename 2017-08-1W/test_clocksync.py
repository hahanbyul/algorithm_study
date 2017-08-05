from CLOCKSYNC import Clocksync

def test_init():
    cs = Clocksync()

def test_push_switch():
    cs = Clocksync()
    assert cs.push_switch(tuple([12,6,6,6,6,6,12,12,12,12,12,12,12,12,12,12]), 0) == (9,3,3,6,6,6,12,12,12,12,12,12,12,12,12,12)
    assert cs.push_switch(cs.push_switch(tuple([12,6,6,6,6,6,12,12,12,12,12,12,12,12,12,12]), 8), 8) == (12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12)

def test_get_next():
    cs = Clocksync()
    next_states = cs.get_next(tuple([12,6,6,6,6,6,12,12,12,12,12,12,12,12,12,12]))
    assert len(next_states) == 9
    print(next_states)

def test_ex1():
    cs = Clocksync()
    assert cs.bfs(tuple([12,6,6,6,6,6,12,12,12,12,12,12,12,12,12,12])) == 2

def test_ex2():
    cs = Clocksync()
    assert cs.bfs(tuple([int(i) for i in '12 9 3 12 6 6 9 3 12 9 12 9 12 12 6 6'.split()])) == 9
