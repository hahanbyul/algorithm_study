#include <cstdio>
#include <string>
#include <algorithm>
#include <map>
using namespace std;

int N;
char board[500][500];

const int LEFT  = -1;
const int RIGHT = 1;

const int MAX = 1000000007;

class Node {
    const int yStart, xStart;
    const int direction;
    int count;
    string path;
    map<string, int> pathMap;

public:
    Node(int _y, int _x, int _direction) : yStart(_y), xStart(_x), direction(_direction), count(0) {
        path.reserve(N);
        path[0] = board[_y][_x];
        ++count;
    }

    bool isInBoard(int y, int x) {
        return (y >= 0 && y < N && x >= 0 && x < N);
    }

    bool isInMirrorRange(int y, int x) {
        if (direction == RIGHT) return (y <= yStart && x <= xStart);
        else                    return (y >= yStart && x >= xStart);
    }

    bool isGoal() {
        return count == N;
    }

    Node* go(int y, int x) {
        ++count;
        if (!isInBoard(y, x) || !hasOpposite(board[y][x])) {  // 끝에 도달하면 안에 안들어가도 됨
            return 0; 
        }

        path[count-1] = board[y][x];
        return this;
    }

    bool hasOpposite(char ch) {
        int dist = count - 1;

        int yDiff;
        if (direction == RIGHT) { yDiff = min(dist, yStart); }
        else                    { yDiff = min(dist, N - 1 - yStart); }

        int y = yStart - direction * yDiff;
        int x = xStart - direction * (dist - yDiff);
        while (isInMirrorRange(y, x)) {
            if (board[y][x] == ch) { return true; }

            y += direction;
            x -= direction;
        }

        return false;
    }

    void back() {
        --count;
    }

    void print(const int direction) {
        if (direction == LEFT) printf("%s (LEFT) \n", path.c_str());
        if (direction == RIGHT) printf("%s (RIGHT) \n", path.c_str());
    }

    void print() {
        printf("%s\n", path.c_str());
    }

    string getPath() {
        return path;
    }

    int getNext(int x) {
        return x + direction;
    }

    void updateMap() {
        ++pathMap[string(path.c_str())];
    }

    map<string, int>& getPathMap() {
        return pathMap;
    }
};

void dfs(Node* curNode, int y, int x) {
    if (curNode == 0) { return; }
    if (curNode->isGoal()) {
        curNode->updateMap();
        return;
    }

    int yNext = curNode->getNext(y);
    dfs(curNode->go(yNext, x), yNext, x);
    curNode->back();

    int xNext = curNode->getNext(x);
    dfs(curNode->go(y, xNext), y, xNext);
    curNode->back();
}

int main() {
    int testCase;
    scanf("%d", &testCase);

    int t = 0;
    while (++t <= testCase) {
        scanf("%d", &N);

        for (int n = 0; n < N; ++n)
            scanf("%s", board[n]);

        if (board[0][0] != board[N-1][N-1]) {
            printf("#%d 0\n", t);
            continue;
        }

        unsigned int numOfCases = 0;
        for (int i = 0; i < N; ++i) {
            Node rightStart(i, N-1-i, RIGHT);
            dfs(&rightStart, i, N-1-i);

            Node leftStart(i, N-1-i, LEFT);
            dfs(&leftStart, i, N-1-i);

            map<string, int>& leftPath  = leftStart.getPathMap();
            map<string, int>& rightPath = rightStart.getPathMap();
            for (map<string, int>::iterator it = leftPath.begin(); it != leftPath.end(); ++it) { 
                string path = it->first;
                int   count = it->second;
                // printf("%d) leftpath:  %s (%d %d)\n", i, path.c_str(), count, rightPath[path]);

                numOfCases += (rightPath[path] * count) % MAX;
                numOfCases %= MAX;
            }
        }

        printf("#%d %d\n", t, numOfCases);
    }
}