class Dictionary:
    def __init__(self):
        self.words_list = list()
        self.vertex = dict()

    def read_words(self, N):
        for _ in range(N):
            word = input()
            self.make_init_graph(word)
            self.words_list.append(word)

    def make_init_graph(self, word):
        if len(self.words_list) == 0:
            return

        last_word = self.words_list[-1]
        if last_word[0] == word[0]:
            return

        adjacent = self.get_adjacent(last_word[0])
        adjacent.append(word[0])

    def get_adjacent(self, char):
        adjacent = self.vertex.get(char, None)
        if adjacent is None:
            adjacent = list()
            self.vertex[char] = adjacent

        return adjacent

    def read_words_with_string(self, string):
        for word in string.split("\n"):
            self.make_init_graph(word)
            self.words_list.append(word)

    def find_alphabet_order(self):
        pass
        

    def dfs(self, index, char, visited):
        if visited[-1] != self.words_list[index + 1][len(visited)-1]:
            return

class Vertex:
    def __init__(self, char):
        self.char = char
        self.edges = list()

def main():
    C = int(input())
    for _ in range(C):
        N = int(input())
        d = Dictionary()
        d.read_words(N)
        d.find_alphabet_order()


if __name__ == '__main__':
    main()
