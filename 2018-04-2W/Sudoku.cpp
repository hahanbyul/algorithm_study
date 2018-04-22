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

    void printBoard() {
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j)
                printf("%d ", board[i][j]);
            printf("\n");
        }
    }

    void fill(int i, int j) {
        int box = getBoxNum(i, j);

        if (board[i][j] != 0) return;

        int k;
        for (k = 1; k < 10; ++k) {
            if (marked[i][j][k] != POSSIBLE) continue;
            if (possibleLength[i][j] == 1 || countInRow[i][k] == 1 || countInCol[j][k] == 1 || countInBox[box][k] == 1) break;
        }

        if (k == 10) return;

        mark(i, j, k);
        
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

    bool dfs() { return dfs(0, 0, remainedZero); }
    bool dfs(int _i, int _j, int remained) {
        // printBoard();
        if (remained == 0) return true;
        
        // find next empty
        pair<int, int> p = findNextEmpty(_i, _j);
        int i = p.first;
        int j = p.second;

        vector<int> cand(10, POSSIBLE);
        checkRow(i, cand);
        checkCol(j, cand);
        checkBox(getBoxNum(i, j), cand);

        for (int k = 1; k <= 9; ++k) {
            if (marked[i][j][k] != POSSIBLE) continue;

            // check consistency
            if (cand[k] != POSSIBLE) continue;

            board[i][j] = k;
            bool result = dfs(i, j, remained - 1);
            if (result) return true;
        }

        board[i][j] = 0;
        return false;
    }

    pair<int, int> findNextEmpty(int _i, int _j) {
        for (int i = _i; i < 9; ++i)
            for (int j = _j; j < 9; ++j)
                if (board[i][j] == 0) return make_pair(i, j);
        return findNextEmpty(0, 0);
    }

private:
    int getBoxNum(int i, int j) {
        return i/3*3 + j/3;
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

    sdk.dfs();
    sdk.printBoard();

    return 0;
}
