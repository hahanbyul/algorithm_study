#include <iostream>
#include <vector>
#include <string>
using namespace std;

const int R = 26;
const int SEARCH_MISS = 0;
int N;
const int LEFT  = 1;
const int RIGHT = -1;
char board[500][500];

struct Path {
    string key;
    int count;

    Path(string _key, int _count) : key(_key), count(_count) {}
    bool operator== (const Path& p) const { return key == p.key; }
    bool operator<  (const Path& p) const { return key < p.key;  }
    bool operator<= (const Path& p) const { return key <= p.key; }
};

using Bag = vector<Path>;

int toNumber(char ch) { return ch - 'a'; }

struct TrieNode {
    int count;
    string finalPath;
    vector<TrieNode*> children;

    TrieNode() : count(0), children(R, 0) {}
    void insert(const char* path, const string& pathStr) {
        TrieNode*& currentNode = children[toNumber(*path)];
        if (currentNode == 0) currentNode = new TrieNode();

        if (*(path+1) == 0) {
            if (currentNode->count == 0) 
                currentNode->finalPath = pathStr;
            ++(currentNode->count);
            return;
        }

        currentNode->insert(++path, pathStr);
    }

    int find(const char* path) {
        TrieNode* currentNode = children[toNumber(*path)];
        if (currentNode == 0) { return SEARCH_MISS;        }
        if (*(path+1) == 0)   { return currentNode->count; }

        return currentNode->find(++path);
    }

    void clear() {
        for (auto child : children) {
            if (child != 0) child->clear();
            delete child;
        }
    }

    void collect(Bag& bag) {
        if (!finalPath.empty()) {
            bag.push_back(Path(finalPath, count));
            count = 0;
            return;
        } 

        for (auto child : children) {
            if (child != 0) child->collect(bag);
        }
    }
};

TrieNode leftPath[500], rightPath[500];
void pathMapInc(int i, int direction, const string& path) {
    TrieNode* pathMap;
    if (direction == LEFT)           pathMap = &leftPath[i];
    else /*if (direction == RIGHT)*/ pathMap = &rightPath[i];

    if (direction == RIGHT && leftPath[i].find(path.c_str()) == 0) return;

    pathMap->insert(path.c_str(), path);
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

        for (int n = 0; n < N; ++n)
            scanf("%s", board[n]);

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
            Bag leftBag, rightBag;
            leftPath[i].collect(leftBag);
            rightPath[i].collect(rightBag);

            /*
            cout << "left: ";
            for (auto b : leftBag) cout << b.first << "(" << b.second << "), ";
            cout << "\nright: ";
            for (auto b : rightBag) cout << b.first << "(" << b.second << "), ";
            */

            Bag::const_iterator leftIt  = leftBag.begin();
            Bag::const_iterator rightIt = rightBag.begin();

            while (leftIt != leftBag.end() && rightIt != rightBag.end()) {
                if (*leftIt == *rightIt)     numOfCases += (*leftIt++).count * (*rightIt++).count;
                else if (*leftIt < *rightIt) while (++leftIt != leftBag.end()   && *leftIt < *rightIt);
                else                         while (++rightIt != rightBag.end() && *rightIt < *leftIt);
            }
        }
        printf("#%d %d\n", t, numOfCases);

        /*
        for (int n = 0; n < N; ++n) {
            leftPath[n].clear();
            rightPath[n].clear();
        }
        */
    }
}