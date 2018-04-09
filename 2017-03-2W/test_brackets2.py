from BRACKETS2 import Brackets2

def test_examples():
    br = Brackets2
    assert br.is_pair('()()') == "YES"
    assert br.is_pair('({[}])') == "NO"
    assert br.is_pair('({}[(){}])') == "YES"
