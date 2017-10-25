import pprint

VERTICAL = True
HORIZONTAL = False

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
            if direction == VERTICAL:
                x += 1 
            else:
                y += 1

        return cnt

    def get_condition(self, start, direction):
        x, y = start
        cond = ''

        while x < 10 and y < 10 and self.puzzle[x][y] != '+':
            cond += self.puzzle[x][y]
            if direction == VERTICAL:
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
            if direction == VERTICAL:
                x += 1 
            else:
                y += 1

        return cond

    def erase_puzzle(self, start, word, direction):
        x, y = start
        for char in word:
            self.puzzle[x][y] = char
            if direction == VERTICAL:
                x += 1 
            else:
                y += 1

    def solve(self):
        for x in range(10):
            for y in range(10):
                if self.puzzle[x][y] != '+':
                    ret = self.solve_this((x,y), VERTICAL)

    def is_solved(self):
        return '-' not in self.puzzle_to_string()

    def puzzle_to_string(self):
        return ''.join([''.join(row) for row in self.puzzle])

    def floor(self, start, direction):
        x, y = start
        if direction == VERTICAL:
            while x > 0 and self.puzzle[x-1][y] != '+':
                x -= 1
        else:
            while y > 0 and self.puzzle[x][y-1] != '+':
                y -= 1

        return (x, y)

    def solve_this(self, start, direction):
        print('start: (%d, %d)' % start)
        print('direction: %s' % direction)
        start = self.floor(start, direction)
        cond = self.get_condition(start, direction)
        if len(cond) == 1 or '-' not in cond:
            return 

        pprint.pprint(self.puzzle)

        for word in self.words:
            if not self.visited.get(word, False) and self.is_satisfied(cond, word):
                self.visited[word] = True
                prev = self.fill_puzzle(start, word, direction)
                pprint.pprint(self.puzzle)

                if self.is_solved():
                    return True

                x, y = start
                for delta in range(len(word)):
                    if direction == VERTICAL:
                        self.solve_this((x+delta,y), HORIZONTAL)
                    else:
                        self.solve_this((x,y+delta), VERTICAL)

                self.visited[word] = False
                self.erase_puzzle(start, prev, direction)

