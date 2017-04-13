from DICTIONARY import Dictionary
import string

d = list()
for i in range(8):
    d.append(Dictionary())

d[0].read_words_with_string("ba\naa\nab")
d[1].read_words_with_string("aa\nba\nbc")
d[2].read_words_with_string("gg\nkia\nlotte\nlg\nhanhwa")

def test_new_func():
    d[2].find_graph()
    print(d[2].compute_num_in())
    d[2].topo_sort()

def test_is_cycle():
    D = Dictionary()
    D.vertex = {'a': ['b', 'c'], 'b': ['d'], 'c': ['a']}
    D.is_cycle('a', list())

def test_read_input():
    assert d[0].words_list == ["ba", "aa", "ab"]

def test_find_diff_idx():
    assert d[0].find_diff_idx("fa", "gb") == 0
    assert d[0].find_diff_idx("fa", "fb") == 1
    assert d[0].find_diff_idx("fa", "faa") == 2
    assert d[0].find_diff_idx("abcd", "ab") == 2

def test_find_graph():
    assert d[0].find_graph() == {'b': {'a'}, 'a': {'b'}}
    assert d[1].find_graph() == {'a': {'b', 'c'}}
    assert d[2].find_graph() == {'g': {'k'}, 'k': {'l'}, 'o': {'g'}, 'l': {'h'}}

def test_find_answer():
    try: 
        # d[0].find_answer()
        some_d = Dictionary()
        some_d.vertex = {'a': ['b'], 'b': ['c'], 'c': ['a']}
    except Exception:
        assert True
    assert d[1].find_answer() == ['a', 'b', 'c'] or d[1].find_answer() == ['a', 'c', 'b']

    b = ['h', 'l', 'k', 'g', 'o']
    b.reverse()
    assert d[2].find_answer() == b

    d[3].vertex = {'a': ['b'], 'b': ['c', 'd'], 'd': 'c'}
    c = ['c', 'd', 'b', 'a']
    c.reverse()
    assert d[3].find_answer() == c
    
    d[4].vertex = {'a': ['b', 'c'], 'b': ['d'], 'c': ['d']}
    answer = d[4].find_answer()
    assert answer == ['a', 'b', 'c', 'd'] or answer == ['a', 'c', 'b', 'd']

    d[5].vertex = {'a': ['d'], 'b': ['d'], 'c': ['b'], 'd': ['c']}
    try:
        answer = d[5].find_answer()
    except Exception:
        assert True

    d[6].vertex = {'a': ['b'], 'e': ['f']}
    answer = d[6].find_answer()
    assert "".join(answer) == "abef" or "".join(answer) == "efab"

    d[7].vertex = {'a': ['b', 'c'], 'b': ['c']}
    answer = d[7].find_answer()
    assert "".join(answer) == "abc"

def test_get_answer():
    dd = Dictionary()
    dd.read_words_with_string("gg\nkia\nlotte\nlg\nhanhwa")
    dd.get_answer() == 'ogklhabcdefijmnpqrstuvwxyz'

    ddd = Dictionary()
    ddd.read_words_with_string("dictionary\nenglish\nis\nordered\nordinary\nthis")
    ddd.get_answer() == string.ascii_lowercase

def test_transform_graph():
    d[0].transform_graph() == [[0,1],[1,0]]
    d[1].transform_graph() == [[0,1,1],[0,0,0],[0,0,0]]

def test_equal():
    d[2].find_answer == d[2].topological_sort()
