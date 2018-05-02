#include <cstdio>
#include <string>
using namespace std;

int N;
char board[500][500];

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
        if (!isInBoard(y, x) || !hasOpposite(y, x, direction)) { 
            return 0; 
        }

        path[count-1] = board[y][x];
        return this;
    }

    bool hasOpposite(int y, int x, int direction) {
        int yMirror = yStart - (x - xStart);
        int xMirror = xStart - (y - yStart);

        if (board[yMirror][xMirror] == board[y][x]) { return true; }
        if (isInMirrorRange(yMirror+1, xMirror-1, direction) && board[yMirror+1][xMirror-1] == board[y][x]) {
            return true;
        }
        if (isInMirrorRange(yMirror-1, xMirror+1, direction) && board[yMirror-1][xMirror+1] == board[y][x]) {
            return true;
        }

        return false;
    }

    void back() {
        --count;
    }

    void print() {
        printf("%s\n", path.c_str());
    }
};

void dfs(Node* curNode, int y, int x, int direction) {
    if (curNode == 0) { return; }
    if (curNode->isGoal()) { // 종료 조건
        curNode->print();
        // TODO: map 카운트 증가
        return;
    }
    printf("%d %d\n", y, x);

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

    int numOfCases = 0;
    if (board[0][0] != board[N-1][N-1]) {
        printf("0\n");
        // continue;
    }

    while (true) {
        int i;
        scanf("%d", &i);
        Node start(i, N-1-i);
        dfs(&start, i, N-1-i, LEFT);
    }
}