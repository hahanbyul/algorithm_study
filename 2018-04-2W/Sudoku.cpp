#include <iostream>
#include <vector>
using namespace std;

class Sudoku {
    string boardStr[9];
    int board[9][9];
    int rowPos[9], colPos[9];
    int remainedZero;
    vector<vector<int> > countInRow, countInCol, countInBox;
    vector<vector<vector<int> > > marked;
    int possibleLength[9][9];
    enum Condition { IMPOSSIBLE, POSSIBLE };

public:
    Sudoku() : remainedZero(0) {
        readBoard();

        // save box index
        for (int i = 0; i < 9; ++i) {
            rowPos[i] = i / 3 * 3;
            colPos[i] = i % 3 * 3;
        }

        getPossible();
        getCount(); 

    }

    void readBoard() {
        for (int i = 0; i < 9; ++i)
            for (int j = 0; j < 9; ++j)
                scanf("%d", &board[i][j]);
    }

    void getPossible() {
        for (int i = 0; i < 9; ++i) {
            marked.push_back(vector<vector<int> >());
            for (int j = 0; j < 9; ++j) {
                marked[i].push_back(vector<int>());
                if (board[i][j] == 0) {
                    ++remainedZero;
                    marked[i][j] = vector<int>(10, POSSIBLE);
                    check(i, j);
                    possibleLength[i][j] = getCandLength(i, j);
                }
                else possibleLength[i][j] = 0;
            }
        }
    }

    void getCount() {
        for (int i = 0; i < 9; ++i) {
            countInRow.push_back(vector<int>(10, 0));
            countInCol.push_back(vector<int>(10, 0));
            countInBox.push_back(vector<int>(10, 0));
        }

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
        // cout << "remained: " << remainedZero << "\n\n";
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
                printf("(%d) ", possibleLength[row][col]);
            }
        }
        printf("\n");
    }

    void printColCand(int col) {
        for (int row = 0; row < 9; ++row) {
            if (board[row][col] == 0) {
                printf("(%d, %d): ", row, col);
                printCand(marked[row][col]);
                printf("(%d) ", possibleLength[row][col]);
            }
        }
        printf("\n");
    }

    void printBoxCand(int box) {
        for (int i = rowPos[box]; i < rowPos[box] + 3; ++i) {
            for (int j = colPos[box]; j < colPos[box] + 3; ++j) {
                if (board[i][j] == 0) {
                    printf("(%d, %d): ", i, j);
                    printCand(marked[i][j]);
                    printf("(%d) ", possibleLength[i][j]);
                }
            }
        }
        printf("\n");
    }

    void printCount(const vector<int>& array) {
        for (int k = 1; k <= 9; ++k)
            printf("%d ", array[k]);
        cout << "\n";
    }

    void printCountInRow(int row) {
        printf("%d) ", row);
        printCount(countInRow[row]);
    }

    void printCountInCol(int col) {
        printf("%d) ", col);
        printCount(countInCol[col]);
    }

    void printCountInBox(int box) {
        printf("%d) ", box);
        printCount(countInBox[box]);
    }


    void fill(int i, int j) {
        int box = getBoxNum(i, j);

        if (board[i][j] != 0) return;

        int k;
        for (k = 1; k < 10; ++k) {
            if (marked[i][j][k] != POSSIBLE) continue;
            // printf("%d) %d %d %d\n", k, countInRow[i][k], countInCol[j][k], countInBox[box][k]);
            if (possibleLength[i][j] == 1 || countInRow[i][k] == 1 || countInCol[j][k] == 1 || countInBox[box][k] == 1) break;
        }

        if (k == 10) return;

        mark(i, j, k);
        // printBoard();
        
        for (int n = 0; n < 9; ++n) {
            fill(i, n);
            fill(n, j);
        }

        for (int r = rowPos[box]; r < rowPos[box] + 3; ++r)
            for (int c = colPos[box]; c < colPos[box] + 3; ++c)
                fill(r, c);
    }

    void mark(int i, int j, int k) {
        board[i][j] = k;
        --remainedZero;

        int box = getBoxNum(i, j);
        for (int kk = 1; kk <= 9; ++kk) {
            if (marked[i][j][kk] == POSSIBLE) {
                marked[i][j][kk] = IMPOSSIBLE;
                --countInRow[i][kk];
                --countInCol[j][kk];
                --countInBox[box][kk];
            }
        }

        for (int n = 0; n < 9; ++n) {
            markImpossible(i, n, k);
            markImpossible(n, j, k);
        }

        for (int r = rowPos[box]; r < rowPos[box] + 3; ++r)
            for (int c = colPos[box]; c < colPos[box] + 3; ++c)
                markImpossible(r, c, k);
    }

    void markImpossible(int i, int j, int k) {
        if (board[i][j] != 0) return;
        if (marked[i][j][k] == POSSIBLE) {
            marked[i][j][k] = IMPOSSIBLE;
            --possibleLength[i][j];
            --countInRow[i][k];
            --countInCol[j][k];
            --countInBox[getBoxNum(i, j)][k];
        }
    }

    void fillDefinite() {
        for (int i = 0; i < 9; ++i)
            for (int j = 0; j < 9; ++j)
                fill(i, j);
    }

    void printAllCand() {
        cout << "row cand.: \n";
        for (int i = 0; i < 9; ++i)
            printRowCand(i);
        cout << "col cand.: \n";
        for (int i = 0; i < 9; ++i)
            printColCand(i);
        cout << "box cand.: \n";
        for (int i = 0; i < 9; ++i)
            printBoxCand(i);
    }

    void printAllCount() {
        cout << "row count: \n";
        for (int i = 0; i < 9; ++i)
            printCountInRow(i);
        cout << "col count: \n";
        for (int i = 0; i < 9; ++i)
            printCountInCol(i);
        cout << "box count: \n";
        for (int i = 0; i < 9; ++i)
            printCountInBox(i);
    }

    void confirm() {
        for (int i = 0; i < 9; ++i)
            for (int j = 0; j < 9; ++j)
                if (board[i][j] < 0) board[i][j] = -board[i][j];
    }

    bool dfs() { return dfs(remainedZero); }
    bool dfs(int remained) {
        // printBoard();
        if (remained == 0) return true;
        
        // find next empty
        int i, j;
        for (i = 0; i < 9; ++i) {
            for (j = 0; j < 9; ++j) {
                if (board[i][j] == 0) break;
            }
            if (j != 9 && board[i][j] == 0) break;
        }

        vector<int> cand(10, POSSIBLE);
        checkRow(i, cand);
        checkCol(j, cand);
        checkBox(getBoxNum(i, j), cand);

        for (int k = 1; k <= 9; ++k) {
            if (marked[i][j][k] != POSSIBLE) continue;

            // check consistency
            if (cand[k] != POSSIBLE) continue;

            board[i][j] = k;
            bool result = dfs(remained - 1);
            if (result) return true;
        }

        board[i][j] = 0;
        return false;
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
    Sudoku sdk;
    // sdk.printBoard();

    sdk.fillDefinite();
    // sdk.printBoard();
    // sdk.confirm();

    sdk.dfs();
    sdk.printBoard();

    return 0;
}
