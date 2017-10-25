class Puzzle:
    def __init__(self):
        self.puzzle = []
        self.visited = {}

    def read_puzzle(self):
        for _ in range(10):
            self.puzzle.append([x for x in input()])

    def read_words(self):
        self.words = set(input().split(';'))

    def get_empty_len(self, start, direction):
        x, y = start
        cnt = 0

        while x < 10 and y < 10 and self.puzzle[x][y] == '-':
            cnt += 1
            if direction == 'v':
                x += 1 
            else:
                y += 1

        return cnt

    def get_condition(self, start, direction):
        x, y = start
        cond = ''

        while x < 10 and y < 10 and self.puzzle[x][y] != '+':
            cond += self.puzzle[x][y]
            if direction == 'v':
                x += 1 
            else:
                y += 1

        return cond

    @staticmethod
    def is_satisfied(condition, word):
        if len(condition) != len(word):
            return False

        for ch1, ch2 in zip(condition, word):
            if ch1 != '-' and ch1 != ch2:
                return False

        return True
        
    def fill_puzzle(self, start, word, direction):
        x, y = start
        cond = self.get_condition(start, direction)
        if len(cond) == 1 or not self.is_satisfied(cond, word):
            return False

        for char in word:
            self.puzzle[x][y] = char
            if direction == 'v':
                x += 1 
            else:
                y += 1

        return cond

    def erase_puzzle(self, start, word, direction):
        x, y = start
        for char in word:
            self.puzzle[x][y] = char
            if direction == 'v':
                x += 1 
            else:
                y += 1

"""
    def solve(self):
        for x in range(10):
            for y in range(10):
                if self.puzzle[x][y] == '-':
                    for word in self.words:
                        if not visited.get(word, False) and self.is_satisfied(cond, word):


        pass



"""
