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
            word = raw_input()
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

    def compute_num_in(self):
        num_in = dict()
        for key, values in self.vertex.items():
            if not key in num_in:
                num_in[key] = 0

            for val in values:
                if not val in num_in:
                    num_in[val] = 0
                num_in[val] += 1

        return num_in

    def topo_sort(self):
        num_in_keys = self.compute_num_in()

        sorted_list = list()

        while len(num_in_keys) > 0:
            # print(f'num_in_keys: {num_in_keys}')
            tups = sorted(num_in_keys.items(), key=lambda x: x[1])

            i = 0
            while i < len(tups):
                key = tups[i][0]
                self.is_cycle(key, list())           # if cycle in graph, raise exception

                sorted_list.append(key)
                del num_in_keys[key]

                for val in self.vertex.get(key, []):
                    num_in_keys[val] -= 1
                i += 1

        self.char_list = sorted_list
        return sorted_list

    def is_cycle(self, key, visited):
        # print(f'key: {key}, visited: {visited}')
        if key in visited:
            raise Exception
        visited.append(key)

        for adj in self.vertex.get(key, []):
            self.is_cycle(adj, visited)
            visited.pop()

    def get_answer(self):
        try:
            self.find_graph()
            self.topo_sort()
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


def main():
    C = int(raw_input())
    for _ in range(C):
        N = int(raw_input())
        d = Dictionary()
        d.read_words(N)
        print d.get_answer()


if __name__ == '__main__':
    main()
