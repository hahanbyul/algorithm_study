#include <iostream>
using namespace std;

int board[9][9];
int zeroNum = 0;
int zeroInRow[9] = {};
int zeroInCol[9] = {};
int zeroInBox[9] = {};

int rowPos[9], colPos[9];

int getBoxNum(int i, int j) {
    return i/3*3 + j/3;
}

void decreaseCnt(int i, int j) {
    --zeroNum;
    --zeroInRow[i];
    --zeroInCol[j];
    --zeroInBox[getBoxNum(i, j)];
}

void printRow(int i) {
    for (int num : board[i])
        cout << num << " ";
    cout << "\n";
}

void printBoard() {
    for (int i = 0; i < 9; ++i)
        printRow(i);
}

void printCol(int c) {
    for (int i = 0; i < 9; ++i)
        cout << board[i][c] << "\n";
}

void printBox(int b) {
    for (int i = rowPos[b]; i < rowPos[b] + 3; ++i) {
        for (int j = colPos[b]; j < colPos[b] + 3; ++j)
            cout << board[i][j] << " ";
        cout << "\n";
    }
}

int sumRow(int row) {
    int ret = 0;
    for (int r : board[row])
        ret += r;
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
        if (board[row][i] == 0) {
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
        if (board[i][col] == 0) {
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
            if (board[i][j] == 0) {
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

int main() {
    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            scanf("%d", &board[i][j]);

            if (board[i][j] == 0) {
                ++zeroInRow[i];
                ++zeroInCol[j];
                ++zeroInBox[getBoxNum(i, j)];
                ++zeroNum;
            }
        }
    }

    for (int i = 0; i < 9; ++i) {
        rowPos[i] = i / 3 * 3;
        colPos[i] = i % 3 * 3;
    }

    for (int i = 0; i < 9; ++i)
        fillRow(i);
    for (int i = 0; i < 9; ++i)
        fillCol(i);
    for (int i = 0; i < 9; ++i)
        fillBox(i);

    cout << endl;
    printBoard();
    cout << zeroNum << endl;
}
