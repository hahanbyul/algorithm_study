import string

class Dictionary:
    def __init__(self):
        self.words_list = list()
        self.vertex = dict()
        self.is_visited = dict()

    def read_words(self, N):
        for _ in range(N):
            word = input()
            #self.make_init_graph(word)
            self.words_list.append(word)

    def read_words_with_string(self, string):
        for word in string.split("\n"):
            #self.make_init_graph(word)
            self.words_list.append(word)

    def get_adjacent(self, char):
        adjacent = self.vertex.get(char, None)
        if adjacent is None:
            adjacent = set()
            self.vertex[char] = adjacent

        return adjacent
    
    def find_diff_idx(self, this_word, next_word):
        i = 0
        while i < len(this_word) and this_word[i] == next_word[i]:
            i += 1
        return i

    def find_graph(self):
        for i, this_word in enumerate(self.words_list[:-1]):
            next_word = self.words_list[i+1]

            diff_idx = self.find_diff_idx(this_word, next_word)
            if diff_idx == len(this_word):
                continue

            adjacent = self.get_adjacent(this_word[diff_idx])
            adjacent.add(next_word[diff_idx])

        return self.vertex

    def foo(self):
        try:
            char_list = list()
            for key in self.vertex.keys():
                self.dfs(key, char_list, list()) 
                if not self.is_visited.get(key, False):
                    char_list.append(key)
                self.is_visited[key] = True
                print(f'is_visited: {self.is_visited}')
                print(f'char_list: {char_list}')
        except Exception:
            print("INVALID HYPOTHESIS")
        self.char_list = char_list
        self.char_list.reverse()
        return self.char_list

    def dfs(self, char, char_list, cycle_check):
        print(f'dfs({char})')
        if self.is_visited.get(char, False) or char not in self.vertex.keys():
            print('return')
            return

        cycle_check.append(char)

        for adj in self.get_adjacent(char):
            print(f'adj: {self.get_adjacent(char)}')
            if adj in cycle_check:
                raise Exception

            self.dfs(adj, char_list, cycle_check)
            if not self.is_visited.get(adj, False):
                char_list.append(adj)
            self.is_visited[adj] = True

            print(f'is_visited: {self.is_visited}')
            print(f'char_list: {char_list}')

    def get_answer(self):
        self.find_graph()
        self.foo()
        if sorted(self.char_list) == self.char_list:
            return string.ascii_lowercase
        else:
            return "".join(self.char_list + [char for char in string.ascii_lowercase if char not in self.char_list])

def main():
    C = int(input())
    for _ in range(C):
        N = int(input())
        d = Dictionary()
        d.read_words(N)
        d.find_alphabet_order()


if __name__ == '__main__':
    main()
