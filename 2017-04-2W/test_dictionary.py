from DICTIONARY import Dictionary
import string

d = list()
for i in range(4):
    d.append(Dictionary())

d[0].read_words_with_string("ba\naa\nab")
d[1].read_words_with_string("aa\nba\nbc")
d[2].read_words_with_string("gg\nkia\nlotte\nlg\nhanhwa")

def test_read_input():
    assert d[0].words_list == ["ba", "aa", "ab"]

'''
def test_make_init_graph():
    assert d[0].vertex == {"b": ["a"]}
    assert d[1].vertex == {"b": ["a"], "a": ["c"]}
'''

def test_find_diff_idx():
    assert d[0].find_diff_idx("fa", "gb") == 0
    assert d[0].find_diff_idx("fa", "fb") == 1
    assert d[0].find_diff_idx("fa", "faa") == 2

def test_find_graph():
    assert d[0].find_graph() == {'b': {'a'}, 'a': {'b'}}
    assert d[1].find_graph() == {'a': {'b', 'c'}}
    assert d[2].find_graph() == {'g': {'k'}, 'k': {'l'}, 'o': {'g'}, 'l': {'h'}}

def test_find_answer():
    d[0].find_answer()
    '''
    try: 
        d[0].find_answer()
    except Exception:
        assert True
    '''
    assert d[1].find_answer() == ['a', 'b', 'c']

    b = ['h', 'l', 'k', 'g', 'o']
    b.reverse()
    assert d[2].find_answer() == b

    d[3].vertex = {'a': ['b'], 'b': ['c', 'd'], 'd': 'c'}
    c = ['c', 'd', 'b', 'a']
    c.reverse()
    assert d[3].find_answer() == c

def test_get_answer():
    dd = Dictionary()
    dd.read_words_with_string("gg\nkia\nlotte\nlg\nhanhwa")
    dd.get_answer() == 'ogklhabcdefijmnpqrstuvwxyz'

    ddd = Dictionary()
    ddd.read_words_with_string("dictionary\nenglish\nis\nordered\nordinary\nthis")
    ddd.get_answer() == string.ascii_lowercase
