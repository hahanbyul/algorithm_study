# https://algospot.com/judge/problem/read/WORDCHAIN
import string

ALPHABET_NUM = 26

class Wordchain:
    def __init__(self):
        self.graph     = [[list() for _ in range(ALPHABET_NUM)] for _ in range(ALPHABET_NUM)]
        self.indegree  = [0 for _ in range(ALPHABET_NUM)]
        self.outdegree = [0 for _ in range(ALPHABET_NUM)]

    def find_index(self, char):
        return string.ascii_lowercase.find(char)

    def read_words(self, N):
        for _ in range(N):
            word = raw_input()
            self.add_edge(word)

    def read_words_with_string(self, string):
        for word in string.split():
            self.add_edge(word)

    def add_edge(self, word):
        here  = self.find_index(word[0])
        there = self.find_index(word[-1])

        self.graph[here][there].append(word)
        self.outdegree[here] += 1
        self.indegree[there] += 1

    def get_euler_circuit(self, here, circuit):
        for there in range(ALPHABET_NUM):
            while len(self.graph[here][there]) != 0:
                self.outdegree[here] -= 1
                self.indegree[there] -= 1

                word = self.graph[here][there].pop(0)
                self.get_euler_circuit(there, circuit)
                circuit.append(word)

    def get_euler_trail_or_circuit(self):
        pass

    def is_euler(self):
        ret = True
        self.start = -1
        self.end   = -1

        for i in range(ALPHABET_NUM):
            if self.indegree[i] == self.outdegree[i]:
                continue

            if self.outdegree[i] == self.indegree[i] + 1:
                if self.start == -1:
                    self.start = i
                else:
                    return False

            if self.indegree[i] == self.outdegree[i] + 1:
                if self.end == -1:
                    self.end = i
                else:
                    return False

        return ret

    def solve(self):
        circuit = list()
        if self.is_euler():
            if self.start == -1: 
                # find euler circuit
                for i in range(ALPHABET_NUM):
                    if self.outdegree[i] > 0:
                        self.get_euler_circuit(i, circuit)
            else:
                # find euler trail (because not found start point)
                self.get_euler_circuit(self.start, circuit)

            if all(u == 0 for u in self.indegree) and all(v == 0 for v in self.outdegree):
                circuit.reverse()
                return circuit


def main():
    C = int(raw_input())
    for _ in range(C):
        N = int(raw_input())
        wordchain = Wordchain()
        wordchain.read_words(N)
        
        answer = wordchain.solve()
        if answer is None:
            print "IMPOSSIBLE"
        else:
            print " ".join(answer)


if __name__ == '__main__':
    main()

