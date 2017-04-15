from WORDCHAIN import Wordchain

def index(char):
    return Wordchain.find_index(None, char)

ex1 = "dog god dragon need"
ex2 = "aa ab bb"
ex3 = "ab cd"

def test_add_edge():
    w = Wordchain()
    w.read_words_with_string(ex1)

    assert w.graph[index('d')][index('g')] == ['dog']
    assert w.graph[index('d')][index('n')] == ['dragon']
    assert w.graph[index('g')][index('d')] == ['god']
    assert w.graph[index('n')][index('d')] == ['need']

    assert w.indegree[index('d')] == 2
    assert w.outdegree[index('d')] == 2
    assert w.indegree[index('g')] == 1
    assert w.outdegree[index('g')] == 1
    assert w.indegree[index('n')] == 1
    assert w.outdegree[index('n')] == 1

def test_euler_circuit():
    w = Wordchain()
    w.read_words_with_string(ex1)

    circuit = list()
    w.get_euler_circuit(index('d'), circuit)
    circuit.reverse()
    assert circuit == ["dog", "god", "dragon", "need"]
