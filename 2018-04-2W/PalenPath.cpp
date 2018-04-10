#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

int N;
const int LEFT  = 1;
const int RIGHT = -1;
char board[500][500];
map<string, int> leftPath[500], rightPath[500];

void pathMapInc(int i, int direction, const string& path) {
    map<string, int>* pathMap;
    if (direction == LEFT)           pathMap = &leftPath[i];
    else /*if (direction == RIGHT)*/ pathMap = &rightPath[i];

    // if (pathMap->find(path) == pathMap->end()) (*pathMap)[path] = 0;
    ++(*pathMap)[path];
}

void computePath(int i, int j, int direction, string path) {
    if (path.size() == N-1) {
        pathMapInc(i,             direction, path);
        pathMapInc(i + direction, direction, path);
        return;
    }

    path.push_back(board[i][j + direction]);
    computePath(i, j + direction, direction, path);
    path.pop_back();

    path.push_back(board[i + direction][j]);
    computePath(i + direction, j, direction, path);
    path.pop_back();
}

int main() {
    int testCase;
    scanf("%d", &testCase);

    int t = 0;
    while (++t <= testCase) {
        scanf("%d", &N);

        for (int n = 0; n < N; ++n) {
            scanf("%s", board[n]);
            leftPath[n].clear();
            rightPath[n].clear();
        }

        string topLeft(1, board[0][0]);
        computePath(0, 0, LEFT, topLeft);

        string bottomRight(1, board[N-1][N-1]);
        computePath(N-1, N-1, RIGHT, bottomRight);

        int numOfCases = 0;
        for (int i = 0; i < N; ++i) {
            for (auto m : leftPath[i])  { 
                string path = m.first;
                int   count = m.second;
                numOfCases += rightPath[i][path] * count;
            }
        }
        printf("#%d %d\n", t, numOfCases);
    }
}