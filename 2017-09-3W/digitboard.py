class Digitboard:
    def __init__(self):
        self.board = []
        self.digit_dict = {}
        self.board_size = 5

    def read_board(self):
        for _ in range(5):
            self.read_line(input())

    def read_line(self, string):
        self.board.append(string.split())

    def solve(self):
        for x in range(self.board_size):
            for y in range(self.board_size):
                self.solve_dfs('', (x,y))

        answer = len(self.digit_dict.keys())
        print(answer)
        return answer

    def solve_dfs(self, string, coord):
        if len(string) == 6:
            # if not self.digit_dict.get(string, False):
                # print(string)
            self.digit_dict[string] = 1
            return
        
        x, y = coord
        if x < 0 or x >= self.board_size:
            return
        if y < 0 or y >= self.board_size:
            return

        next_string = string + self.board[x][y]
        coord_list  = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]

        for next_coord in coord_list:
            self.solve_dfs(next_string, next_coord)


def main():
    db = Digitboard()
    db.read_board()
    db.solve()


if __name__ == '__main__':
    main()
