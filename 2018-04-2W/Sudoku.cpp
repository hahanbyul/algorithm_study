#include <iostream>
#include <vector>
using namespace std;

class Sudoku {
    string boardStr[9];
    int board[9][9];
    int rowPos[9], colPos[9];
    int remainedZero;
    vector<int> countInRow[9], countInCol[9], countInBox[9];

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
                    ++remainedZero;
                    marked[i][j] = vector<int>(10, POSSIBLE);
                    check(i, j);
                    possibleLength[i][j] = getCandLength(i, j);
                }
                else possibleLength[i][j] = 0;
            }
        }

        for (int i = 0; i < 9; ++i) {
            countInRow[i] = vector<int>(10, 0);
            countInCol[i] = vector<int>(10, 0);
            countInBox[i] = vector<int>(10, 0);
        }

        getCount(); 

    }

    void getCount() {
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                for (int k = 1; k < 10; ++k) {
                    if (board[i][j] == 0 && marked[i][j][k] == POSSIBLE) {
                        ++countInRow[i][k];
                        ++countInCol[j][k];
                        ++countInBox[getBoxNum(i, j)][k];
                    }
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



    void fill(int i, int j, bool VERBOSE=false) {
        if (VERBOSE) cout << "[FILL] " << i << ", " << j << endl;
        if (VERBOSE) cout << board[i][j] << " " << possibleLength[i][j] << endl;
        if (board[i][j] != 0 || possibleLength[i][j] != 1) return;

        int k = 0;
        while (++k < 10 && marked[i][j][k] != POSSIBLE);
        if (k == 10) return;
        if (VERBOSE) cout << "k: " << k << endl;

        board[i][j] = -k;
        --remainedZero;
        printBoard();

        mark(i, j, k);
        
        for (int n = 0; n < 9; ++n) {
            fill(i, n, VERBOSE);
            fill(n, j, VERBOSE);
        }

        int box = getBoxNum(i, j);
        for (int r = rowPos[box]; r < rowPos[box] + 3; ++r) {
            for (int c = colPos[box]; c < colPos[box] + 3; ++c) {
                fill(r, c, VERBOSE);
            }
        }
    }

    void mark(int i, int j, int k) {
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
        // printf("mark: (%d, %d)", i, j);
        if (board[i][j] > 0) return;
        if (marked[i][j][k] == POSSIBLE || marked[i][j][k] == GUESS) {
            marked[i][j][k] = IMPOSSIBLE;
            --possibleLength[i][j];
        }
    }

    bool markGuess(int i, int j, int k) {
        if (board[i][j] != 0) return true;
    }

    void restore(int i, int j, int k) {
        if (marked[i][j][k] == GUESS) {
            marked[i][j][k] = POSSIBLE;
            ++possibleLength[i][j];
        }
    }

    void solve() {
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                if (possibleLength[i][j] == 1) fill(i, j);
            }
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
        if (ch == 0)      cout << "\033[1;31m" <<  ch << "\033[0m";
        else if (ch <  0) cout << "\033[1;34m" << -ch << "\033[0m";
        else              cout << ch;
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
        for (int n = 1; n < 10; ++n)
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
    sdk.solve();

    for (int i = 0; i < 9; ++i)
        sdk.printColCand(i);

    return 0;
}
