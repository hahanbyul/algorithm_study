#include <iostream>
#include <vector>
using namespace std;

string board[9];
int zeroNum = 0;
int zeroInRow[9] = {};
int zeroInCol[9] = {};
int zeroInBox[9] = {};

int rowPos[9], colPos[9];

vector<bool> possible[9][9];
int possibleLength[9][9];

int getBoxNum(int i, int j) {
    return i/3*3 + j/3;
}

void decreaseCnt(int i, int j) {
    --zeroNum;
    --zeroInRow[i];
    --zeroInCol[j];
    --zeroInBox[getBoxNum(i, j)];
}

void printChar(char ch) {
    if (ch == '0') cout << "\033[1;31m" << ch << "\033[0m";
    else           cout << ch;
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

int sumRow(int row) {
    int ret = 0;
    for (int i = 0; i < 9; ++i)
        ret += board[row][i];
    return ret;
}

int sumCol(int col) {
    int ret = 0;
    for (int i = 0; i < 9; ++i)
        ret += board[i][col];
    return ret;
}

int sumBox(int b) {
    int ret = 0;
    for (int i = rowPos[b]; i < rowPos[b] + 3; ++i)
        for (int j = colPos[b]; j < colPos[b] + 3; ++j)
            ret += board[i][j];
    return ret;
}

bool fillCol(int);
bool fillBox(int);
bool fillRow(int row) {
    if (zeroInRow[row] != 1) return false;

    for (int i = 0; i < 9; ++i) {
        if (board[row][i] == '0') {
            board[row][i] = 45 - sumRow(row);
            decreaseCnt(row, i);

            fillCol(i);
            fillBox(getBoxNum(row, i));
            break;
        }
    }
    return true;
}

bool fillCol(int col) {
    if (zeroInCol[col] != 1) return false;

    for (int i = 0; i < 9; ++i) {
        if (board[i][col] == '0') {
            board[i][col] = 45 - sumCol(col);
            decreaseCnt(i, col);

            fillRow(i);
            fillBox(getBoxNum(i, col));
            break;
        }
    }
    return true;
}

bool fillBox(int box) {
    if (zeroInBox[box] != 1) return false;

    for (int i = rowPos[box]; i < rowPos[box] + 3; ++i) {
        for (int j = colPos[box]; j < colPos[box] + 3; ++j) {
            if (board[i][j] == '0') {
                board[i][j] = 45 - sumBox(box);
                decreaseCnt(i, j);

                fillRow(i);
                fillCol(j);
                break;
            }
        }
    }
    return true;
}

int toNumber(char ch) {
    return ch - '0';
}

void checkRow(int i, vector<bool>& cand) {
    for (int n = 0; n < 9; ++n)
        cand[toNumber(board[i][n])] = false;
}

void checkCol(int i, vector<bool>& cand) {
    for (int n = 0; n < 9; ++n)
        cand[toNumber(board[n][i])] = false;
}

void checkBox(int box, vector<bool>& cand) {
    for (int i = rowPos[box]; i < rowPos[box] + 3; ++i)
        for (int j = colPos[box]; j < colPos[box] + 3; ++j)
            cand[toNumber(board[i][j])] = false;
}

void printCand(vector<bool>& cand) {
    for (int n = 1; n <= 9; ++n)
        if (cand[n]) cout << n << " ";
}

void check(int i, int j) {
    vector<bool>& cand = possible[i][j];
    checkRow(i, cand);
    checkCol(j, cand);
    checkBox(getBoxNum(i, j), cand);
}

int getCandLength(int i, int j) {
    int ret = 0;
    for (int k = 1; k < 10; ++k)
        ret += possible[i][j][k];
    return ret;
}

void printRowCand(int row) {
    for (int col = 0; col < 9; ++col) {
        if (board[row][col] == '0') {
            printf("(%d, %d): ", row, col);
            printCand(possible[row][col]);
            printf("(%d)\n", possibleLength[row][col]);
        }
    }
}

void printColCand(int col) {
    for (int row = 0; row < 9; ++row) {
        if (board[row][col] == '0') {
            printf("(%d, %d): ", row, col);
            printCand(possible[row][col]);
            printf("(%d)\n", possibleLength[row][col]);
        }
    }
}

void printBoxCand(int box) {
    for (int i = rowPos[box]; i < rowPos[box] + 3; ++i) {
        for (int j = colPos[box]; j < colPos[box] + 3; ++j) {
            if (board[i][j] == '0') {
                printf("(%d, %d): ", i, j);
                printCand(possible[i][j]);
                printf("(%d)\n", possibleLength[i][j]);
            }
        }
    }
}

void fill(int i, int j) {
    if (board[i][j] != '0' || possibleLength[i][j] != 1) return;
    int k;
    for (k = 1; k <= 9; ++k)
        if (possible[i][j][k])
            break;

    board[i][j] = '0' + k;
    --possibleLength[i][j];

    mark(i, j, board[i][j]);

}

void mark(int i, int j, char ch) {
    for (int n = 0; n < 9; ++n) {
        if (possible[i][n][toNumber(ch)]) {
            possible[i][n][toNumber(ch)] = false;
            --possibleLength[i][n];
        }

        if (possible[n][j][toNumber(ch)]) {
            possible[n][j][toNumber(ch)] = false;
            --possibleLength[n][j];
        }
    }

    int box = getBoxNum(i, j);
    for (int r = rowPos[box]; r < rowPos[box] + 3; ++r) {
        for (int c = colPos[box]; c < colPos[box] + 3; ++c) {
            if (possible[r][c][toNumber(ch)]) {
                possible[r][c][toNumber(ch)] = false;
                --possibleLength[r][c];
            }
        }
    }
}

void restore(int i, int j) {
    for (int n = 0; n < 9; ++n) {
        if (possible[i][n][toNumber(board[i][j])]) {
            possible[i][n][toNumber(board[i][j])] = false;
            --possibleLength[i][n];
        }

        if (possible[n][j][toNumber(board[i][j])]) {
            possible[n][j][toNumber(board[i][j])] = false;
            --possibleLength[n][j];
        }
    }

    int box = getBoxNum(i, j);
    for (int r = rowPos[box]; r < rowPos[box] + 3; ++r) {
        for (int c = colPos[box]; c < colPos[box] + 3; ++c) {
            if (possible[r][c][toNumber(board[i][j])]) {
                possible[r][c][toNumber(board[i][j])] = false;
                --possibleLength[r][c];
            }
        }
    }
}

int main() {
    // for test input
    for (int i = 0; i < 9; ++i)
        cin >> board[i];

    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            if (board[i][j] == '0') {
                ++zeroInRow[i];
                ++zeroInCol[j];
                ++zeroInBox[getBoxNum(i, j)];
                ++zeroNum;
            }
            possible[i][j] = vector<bool>(10, true);
        }
    }

    for (int i = 0; i < 9; ++i) {
        rowPos[i] = i / 3 * 3;
        colPos[i] = i % 3 * 3;
    }

    /*
    for (int i = 0; i < 9; ++i)
        fillRow(i);
    for (int i = 0; i < 9; ++i)
        fillCol(i);
    for (int i = 0; i < 9; ++i)
        fillBox(i);
    */

    cout << endl;
    printBoard();
    cout << zeroNum << endl;

    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            if (board[i][j] == '0') {
                check(i, j);
                possibleLength[i][j] = getCandLength(i, j);
            }
        }
    }


    fill(4, 5);

    cout << endl;

    printBoard();
}
