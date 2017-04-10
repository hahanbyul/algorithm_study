from DICTIONARY import Dictionary

d = Dictionary()
d.read_words_with_string("ba\naa\nab")

d2 = Dictionary()
d2.read_words_with_string("ba\naa\ncb")

def test_read_input():
    assert d.words_list == ["ba", "aa", "ab"]

def test_make_init_graph():
    assert d.vertex == {"b": ["a"]}
    assert d2.vertex == {"b": ["a"], "a": ["c"]}
