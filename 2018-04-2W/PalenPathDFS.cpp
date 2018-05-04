#include <cstdio>
#include <string>
#include <algorithm>
#include <map>
using namespace std;

int N;
char board[500][500];
map<string, int> pathLeft, pathRight;

const int LEFT  = -1;
const int RIGHT = 1;

class Node {
    const int yStart, xStart;
    int count;
    string path;

public:
    Node(int _y, int _x) : yStart(_y), xStart(_x), count(0) {
        path.reserve(N);
        path[0] = board[_y][_x];
        ++count;
    }

    bool isInBoard(int y, int x) {
        return (y >= 0 && y < N && x >= 0 && x < N);
    }

    bool isInMirrorRange(int y, int x, int direction) {
        if (direction == RIGHT) return isInBoard(y, x) && (y <= yStart && x <= xStart);
        else                    return isInBoard(y, x) && (y >= yStart && x >= xStart);
    }

    bool isGoal() {
        return count == N;
    }

    Node* go(int y, int x, int direction) {
        ++count;
        if (!isInBoard(y, x) || !hasOpposite(board[y][x], direction)) {  // 끝에 도달하면 안에 안들어가도 됨
            return 0; 
        }

        path[count-1] = board[y][x];
        return this;
    }

    bool hasOpposite(char ch, int direction) {
        int dist = count - 1;

        int yDiff;
        if (direction == RIGHT) { yDiff = min(dist, yStart); }
        else                    { yDiff = min(dist, N - 1 - yStart); }

        int y = yStart - direction * yDiff;
        int x = xStart - direction * (dist - yDiff);
        while (isInMirrorRange(y, x, direction)) {
            if (board[y][x] == ch) { return true; }

            y += direction;
            x -= direction;
        }

        return false;
    }

    void back() {
        --count;
    }

    void print() {
        printf("%s\n", path.c_str());
    }

    string getPath() {
        return path;
    }
};

void dfs(Node* curNode, int y, int x, int direction) {
    if (curNode == 0) { return; }
    if (curNode->isGoal()) { // 종료 조건
        // curNode->print();
        if (direction == RIGHT) ++pathRight[curNode->getPath()];
        else                    ++pathLeft[curNode->getPath()];
        return;
    }

    int yNext = y + direction;
    dfs(curNode->go(yNext, x, direction), yNext, x, direction);
    curNode->back();

    int xNext = x + direction;
    dfs(curNode->go(y, xNext, direction), y, xNext, direction);
    curNode->back();
}

int main() {
    scanf("%d", &N);

    for (int n = 0; n < N; ++n)
        scanf("%s", board[n]);

    if (board[0][0] != board[N-1][N-1]) {
        printf("0\n");
        // continue;
    }

    for (int i = 0; i < N; ++i) {
        Node rightStart(i, N-1-i);
        dfs(&rightStart, i, N-1-i, RIGHT);

        Node leftStart(i, N-1-i);
        dfs(&leftStart, i, N-1-i, LEFT);
    }

    int numOfCases = 0;

    /*
    while (true) {
        int i;
        scanf("%d", &i);
        Node start(i, N-1-i);
        dfs(&start, i, N-1-i, RIGHT);
    }
    */
}