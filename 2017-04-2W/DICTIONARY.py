# https://algospot.com/judge/problem/read/DICTIONARY
import string


class Dictionary:
    def __init__(self):
        self.words_list = list()
        self.vertex = dict()

        self.is_visited = dict()
        self.char_list = list()

    def read_words(self, N):
        for _ in range(N):
            word = input()
            self.words_list.append(word)

    def read_words_with_string(self, string):
        for word in string.split("\n"):
            self.words_list.append(word)

    def get_adjacent(self, char):
        adjacent = self.vertex.get(char, None)
        if adjacent is None:
            adjacent = set()
            self.vertex[char] = adjacent

        return adjacent

    def find_diff_idx(self, this_word, next_word):
        length = min(len(this_word), len(next_word))
        i = 0
        while i < length and this_word[i] == next_word[i]:
            i += 1
        return i

    def find_graph(self):
        for i, this_word in enumerate(self.words_list[:-1]):
            next_word = self.words_list[i+1]

            diff_idx = self.find_diff_idx(this_word, next_word)
            length = min(len(this_word), len(next_word))
            if diff_idx == length:
                continue

            adjacent = self.get_adjacent(this_word[diff_idx])
            adjacent.add(next_word[diff_idx])

        return self.vertex

    def find_answer(self):
        self.is_visited = dict()
        self.char_list = list()

        for key in self.vertex.keys():
            self.dfs(key, self.char_list, list())
            if not self.is_visited.get(key, False):
                self.char_list.append(key)
            self.is_visited[key] = True
            # print(f'is_visited: {self.is_visited}')
            # print(f'char_list: {char_list}')
        self.char_list.reverse()
        return self.char_list

    def dfs(self, char, char_list, cycle_check):
        # print(f'dfs({char})')
        if self.is_visited.get(char, False) or char not in self.vertex.keys():
            # print('return')
            return

        cycle_check.append(char)

        for adj in self.get_adjacent(char):
            # print(f'adj: {self.get_adjacent(char)}')
            if adj in cycle_check:
                raise Exception

            self.dfs(adj, char_list, cycle_check)
            if not self.is_visited.get(adj, False):
                char_list.append(adj)
            self.is_visited[adj] = True

            # print(f'is_visited: {self.is_visited}')
            # print(f'char_list: {char_list}')

    def get_answer(self):
        try:
            self.find_graph()
            # self.find_answer()
            self.topological_sort()
            if sorted(self.char_list) == self.char_list:
                return string.ascii_lowercase
            else:
                remain_chars = [char for char in string.ascii_lowercase if char not in self.char_list]
                return "".join(self.char_list + remain_chars)
        except Exception:
            return "INVALID HYPOTHESIS"

    def transform_graph(self):
        adj = [[0 for _ in range(26)] for _ in range(26)]
        for key in self.vertex.keys():
            here = string.ascii_lowercase.find(key)
            for val in self.vertex[key]:
                there = string.ascii_lowercase.find(val)
                adj[here][there] = 1

        self.adj = adj
        return adj

    def dfs_book(self, here):
        self.is_visited[here] = True
        for there in range(0, 26):
            if self.adj[here][there] and not self.is_visited.get(there, False):
                self.dfs_book(there)
        self.char_list.append(here)

    def topological_sort(self):
        self.is_visited = dict()
        self.char_list = list()
        self.transform_graph()

        for i in range(26):
            if not self.is_visited[i]:
                self.dfs_book(i)
        self.char_list.reverse()

        for i in range(26):
            for j in range(i+1, 26):
                if self.adj[self.char_list[j]][self.char_list[i]]:
                    raise Exception

        self.char_list = [string.ascii_lowercase[i] for i in self.char_list]
        return self.char_list
        

def main():
    C = int(input())
    for _ in range(C):
        N = int(input())
        d = Dictionary()
        d.read_words(N)
        print(d.get_answer())


if __name__ == '__main__':
    main()
