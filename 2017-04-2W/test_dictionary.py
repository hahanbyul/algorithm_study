from DICTIONARY import Dictionary

d = Dictionary()
d.read_words_with_string("ba\naa\nab")

def test_read_input():
    assert d.words == ["ba", "aa", "ab"]
