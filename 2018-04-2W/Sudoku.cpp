#include <iostream>
#include <vector>
using namespace std;

class Sudoku {
    string boardStr[9];
    int board[9][9];
    int rowPos[9], colPos[9];
    int remainedZero;

    vector<int> marked[9][9];
    int possibleLength[9][9];

    enum Condition { IMPOSSIBLE, POSSIBLE, GUESS };

public:
    Sudoku() : remainedZero(0) {
        readBoard();

        for (int i = 0; i < 9; ++i) {
            rowPos[i] = i / 3 * 3;
            colPos[i] = i % 3 * 3;
        }

        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                if (board[i][j] == 0) {
                    marked[i][j] = vector<int>(10, POSSIBLE);
                    ++remainedZero;
                    check(i, j);
                    possibleLength[i][j] = getCandLength(i, j);
                }
            }
        }
    }

    void check(int i, int j) {
        vector<int>& cand = marked[i][j];
        checkRow(i, cand);
        checkCol(j, cand);
        checkBox(getBoxNum(i, j), cand);
    }

    void readBoard() {
        for (int i = 0; i < 9; ++i)
            cin >> boardStr[i];

        for (int i = 0; i < 9; ++i)
            for (int j = 0; j < 9; ++j)
                board[i][j] = boardStr[i][j] - '0';
    }

    void printRow(int i) {
        for (int j = 0; j < 9; ++j) {
            printChar(board[i][j]);
            cout << " ";
        }
        cout << "\n";
    }

    void printBoard() {
        for (int i = 0; i < 9; ++i)
            printRow(i);
        cout << "remained: " << remainedZero << "\n\n";
    }

    void printCol(int c) {
        for (int i = 0; i < 9; ++i) {
            printChar(board[i][c]);
            cout << "\n";
        }
    }

    void printBox(int b) {
        for (int i = rowPos[b]; i < rowPos[b] + 3; ++i) {
            for (int j = colPos[b]; j < colPos[b] + 3; ++j) {
                printChar(board[i][j]);
                cout << " ";
            }
            cout << "\n";
        }
    }

    void printRowCand(int row) {
        for (int col = 0; col < 9; ++col) {
            if (board[row][col] == 0) {
                printf("(%d, %d): ", row, col);
                printCand(marked[row][col]);
                printf("(%d)\n", possibleLength[row][col]);
            }
        }
    }

    void printColCand(int col) {
        for (int row = 0; row < 9; ++row) {
            if (board[row][col] == 0) {
                printf("(%d, %d): ", row, col);
                printCand(marked[row][col]);
                printf("(%d)\n", possibleLength[row][col]);
            }
        }
    }

    void printBoxCand(int box) {
        for (int i = rowPos[box]; i < rowPos[box] + 3; ++i) {
            for (int j = colPos[box]; j < colPos[box] + 3; ++j) {
                if (board[i][j] == 0) {
                    printf("(%d, %d): ", i, j);
                    printCand(marked[i][j]);
                    printf("(%d)\n", possibleLength[i][j]);
                }
            }
        }
    }
    void fill(int i, int j) {
        if (board[i][j] != 0 || possibleLength[i][j] != 1) return;
        int k = 0;
        while (++k <= 9 && marked[i][j][k] != POSSIBLE);

        board[i][j] = k;
        --possibleLength[i][j];

        for (int n = 0; n < 9; ++n) {
            markImpossible(i, n, k);
            markImpossible(n, j, k);
        }

        int box = getBoxNum(i, j);
        for (int r = rowPos[box]; r < rowPos[box] + 3; ++r) {
            for (int c = colPos[box]; c < colPos[box] + 3; ++c) {
                markImpossible(r, c, k);
            }
        }
    }

    void markImpossible(int i, int j, int k) {
        if (marked[i][j][k] == POSSIBLE || marked[i][j][k] == GUESS) {
            marked[i][j][k] = IMPOSSIBLE;
            --possibleLength[i][j];
        }
    }

    void restore(int i, int j, int k) {
        if (marked[i][j][k] == GUESS) {
            marked[i][j][k] = POSSIBLE;
            ++possibleLength[i][j];
        }
    }

private:
    int getBoxNum(int i, int j) {
        return i/3*3 + j/3;
    }

    void printChar(char ch) {
        if (ch == '0') cout << "\033[1;31m" << ch << "\033[0m";
        else           cout << ch;
    }

    void printChar(int ch) {
        if (ch == 0) cout << "\033[1;31m" << ch << "\033[0m";
        else         cout << ch;
    }

    int toNumber(char ch) {
        return ch - '0';
    }

    void checkRow(int i, vector<int>& cand) {
        for (int n = 0; n < 9; ++n)
            cand[board[i][n]] = IMPOSSIBLE;
    }

    void checkCol(int i, vector<int>& cand) {
        for (int n = 0; n < 9; ++n)
            cand[board[n][i]] = IMPOSSIBLE;
    }

    void checkBox(int box, vector<int>& cand) {
        for (int i = rowPos[box]; i < rowPos[box] + 3; ++i)
            for (int j = colPos[box]; j < colPos[box] + 3; ++j)
                cand[board[i][j]] = IMPOSSIBLE;
    }

    void printCand(vector<int>& cand) {
        for (int n = 1; n <= 9; ++n)
            if (cand[n] == POSSIBLE) cout << n << " ";
    }

    int getCandLength(int i, int j) {
        int ret = 0;
        for (int k = 1; k < 10; ++k)
            ret += marked[i][j][k];
        return ret;
    }
};


int main() {
    auto sdk = Sudoku();
    sdk.printBoard();
    sdk.printColCand(5);
    return 0;
}
