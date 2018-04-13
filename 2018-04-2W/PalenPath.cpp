#include <iostream>
#include <vector>
#include <string>
using namespace std;

int N;
const int LEFT  = 1;
const int RIGHT = -1;
char board[500][500];

struct Path {
    string key;
    int count;

    Path(string _key) : key(_key), count(1) {}
    void inc() { ++count; }
    bool operator== (const Path& p) const { return key == p.key; }
    bool operator<  (const Path& p) const { return key < p.key;  }
    bool operator<= (const Path& p) const { return key <= p.key; }
};

vector<Path> leftPath[500], rightPath[500];

void pathMapInc(int i, int direction, const string& path) {
    vector<Path>* pathMap;
    if (direction == LEFT)           pathMap = &leftPath[i];
    else /*if (direction == RIGHT)*/ pathMap = &rightPath[i];

    if (direction == LEFT) {
        vector<Path>::iterator it = find(pathMap->begin(), pathMap->end(), path);
        if (it == pathMap->end()) pathMap->push_back(Path(path));
        else                      it->inc();
    }
    else {
        vector<Path>::iterator it = find(leftPath[i].begin(), leftPath[i].end(), path);
        if (it == leftPath[i].end()) return;

        it = find(pathMap->begin(), pathMap->end(), path);
        if (it == pathMap->end()) pathMap->push_back(Path(path));
        else                      it->inc();
    }
}

void computePath(int i, int j, int direction, string& path, int count) {
    if (count == N-1) {
        pathMapInc(i,             direction, path);
        pathMapInc(i + direction, direction, path);
        return;
    }

    path[count] = board[i][j + direction];
    computePath(i, j + direction, direction, path, count + 1);

    path[count] = board[i + direction][j];
    computePath(i + direction, j, direction, path, count + 1);
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

        string topLeft;
        topLeft.resize(N-1);
        topLeft[0] = board[0][0];
        computePath(0, 0, LEFT, topLeft, 1);

        string bottomRight;
        bottomRight.resize(N-1);
        bottomRight[0] = board[N-1][N-1];
        computePath(N-1, N-1, RIGHT, bottomRight, 1);


        int numOfCases = 0;
        for (int i = 0; i < N; ++i) {
            cout << "i: " << i << endl;
            sort(leftPath[i].begin(),  leftPath[i].end());
            sort(rightPath[i].begin(), rightPath[i].end());

            cout << "leftPath[i]: ";
            for (auto p : leftPath[i]) cout << p.key << "(" << p.count << "), ";
            cout << endl;

            cout << "rightPath[i]: ";
            for (auto p : rightPath[i]) cout << p.key << "(" << p.count << "), ";
            cout << endl;

            vector<Path>::const_iterator leftIt  = leftPath[i].begin();
            vector<Path>::const_iterator rightIt = rightPath[i].begin();

            while (leftIt != leftPath[i].end() && rightIt != rightPath[i].end()) {
                cout << "left: " << leftIt->key << "(" << leftIt->count << ")";
                cout << ", right: " << rightIt->key << "(" << rightIt->count << ")" << endl;
                if (*leftIt == *rightIt)     numOfCases += (*leftIt++).count * (*rightIt++).count;
                else if (*leftIt < *rightIt) while (++leftIt != leftPath[i].end()   && *leftIt < *rightIt);
                else                         while (++rightIt != rightPath[i].end() && *rightIt < *leftIt);
            }
            cout << "answer: " << numOfCases << endl;

        }
        printf("#%d %d\n", t, numOfCases);
    }
}