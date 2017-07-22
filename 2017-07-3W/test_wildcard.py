from WILDCARD import Wildcard

def test_find_word_indices():
    assert Wildcard.find_word_indices('*he*') == (1,3)
    assert Wildcard.find_word_indices('*he') == (1,3)
    assert Wildcard.find_word_indices('he') == (0,2)
    assert Wildcard.find_word_indices('**') == (2,2)
    assert Wildcard.find_word_indices('') == None

def test_solve():
    w = Wildcard()
    # assert w.solve('help', 'he?p')
    # assert w.solve('help', '*p')
    # assert not w.solve('help', '*s')
    # assert not w.solve('help', 'he')
    # assert not w.solve('help', 'p')
    # assert w.solve('help', 'h*p')
    # assert w.solve('help', '*p*')
    # assert not w.solve('helpp', 'he?p')
    # assert not w.solve('hello', '*p*')
    assert w.solve('happy', '*p*p*')
    assert not w.solve('hasee', '*se')
