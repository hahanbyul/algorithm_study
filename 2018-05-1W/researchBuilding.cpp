// link: https://www.acmicpc.net/problem/14502

#include <cstdio>
#include <algorithm>
using namespace std;

#define MAX 8

int N, M, NM;
int area[MAX][MAX];

char emptyChar = 0;
char fillChar  = 3;

int zeroCount, maxZeroCount, maxSafety;

bool isValid(int row, int col) {
    return !(row < 0 || row >= N || col < 0 || col >= M) && (area[row][col] == emptyChar);
}

void dfs(int row, int col) {
    if (area[row][col] == 1) return;
    if (area[row][col] == emptyChar) {
        area[row][col] = fillChar;
        --zeroCount;
    }

    if (isValid(row-1, col)) dfs(row-1, col);
    if (isValid(row+1, col)) dfs(row+1, col);
    if (isValid(row, col-1)) dfs(row, col-1);
    if (isValid(row, col+1)) dfs(row, col+1);
}

void spread() {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (area[i][j] == 2) { 
                dfs(i, j);
                area[i][j] = 2;
            }
            if (zeroCount <= maxSafety) return;
        }
    }
}

void restore() {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (area[i][j] == emptyChar) {
                area[i][j] = fillChar;
            }
        }
    }
    swap(fillChar, emptyChar);
    zeroCount = maxZeroCount;
}

int main() {
    scanf("%d %d", &N, &M);
    NM = N*M;

    zeroCount = 0;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            scanf("%d", &area[i][j]);
            if (area[i][j] == 0) ++zeroCount;
        }
    }

    zeroCount -= 3;                 // for 3 walls
    maxZeroCount = zeroCount;

    for (int i = 0; i < NM-2; ++i) {
        int& area_i = area[i/M][i%M];
        if (area_i != emptyChar) continue;
        area_i  = 1;

        for (int j = i + 1; j < NM-1; ++j) {
            int& area_j = area[j/M][j%M];
            if (area_j != emptyChar) continue;
            area_j  = 1;

            for (int k = j + 1; k < NM; ++k) {
                int& area_k = area[k/M][k%M];
                if (area_k != emptyChar) continue;
                area_k = 1;

                spread();

                if (zeroCount > maxSafety) {
                    maxSafety = zeroCount;
                }

                area_k = emptyChar;
                restore();
            }
            
            area[j/M][j%M] = emptyChar;
        }

        area_i = emptyChar;
    }

    printf("%d\n", maxSafety);

    return 0;
}
