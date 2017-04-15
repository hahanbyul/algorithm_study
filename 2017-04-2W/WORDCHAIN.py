# https://algospot.com/judge/problem/read/WORDCHAIN
import string


class Wordchain:
    def __init__(self):
        self.graph     = [[list() for _ in range(26)] for _ in range(26)]
        self.indegree  = [0 for _ in range(26)]
        self.outdegree = [0 for _ in range(26)]

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

    def get_euler_circuit(self, here):
        pass

    def get_euler_trail_or_circuit(self):
        pass

    def is_euler(self):
        pass

    def solve(self):
        pass

def main():
    C = int(raw_input())
    for _ in range(C):
        N = int(raw_input())
        wordchain = Wordchain()
        wordchain.read_words(N)
        #print wordchain.solve()


if __name__ == '__main__':
    main()

