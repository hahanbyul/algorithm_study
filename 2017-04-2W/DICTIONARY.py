class Dictionary:
    def __init__(self):
        self.words = list()

    def read_words(self, N):
        for _ in range(N):
            self.words.append(input())

    def read_words_with_string(self, string):
        self.words = string.split("\n")

    def find_alphabet_order(self):
        pass

def main():
    C = int(input())
    for _ in range(C):
        N = int(input())
        d = Dictionary()
        d.read_words(N)
        d.find_alphabet_order()


if __name__ == '__main__':
    main()
