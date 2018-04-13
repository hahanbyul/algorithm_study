#include <iostream>
#include <vector>
#include <string>
#include <stack>
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

struct Road {
    string str;
    int i, j;
    Road(string prevStr, int _i, int _j) : str(prevStr), i(_i), j(_j) { str.push_back(board[i][j]); }
    int size() { return str.size(); }
};

using Bag = vector<Path>;

int toNumber(char ch) { return ch - 'A'; }

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

void computePath(int start, int direction) {
    stack<Road> st;
    st.push(Road("", start, start));

    while (st.size() > 0) {
        Road curRoad = st.top();
        st.pop();

        int i = curRoad.i;
        int j = curRoad.j;

        if (curRoad.size() == N-1) {
            pathMapInc(i,             direction, curRoad.str);
            pathMapInc(i + direction, direction, curRoad.str);

            continue;
        }

        st.push(Road(curRoad.str, i, j+direction));
        st.push(Road(curRoad.str, i+direction, j));
    }
}

int main() {
    scanf("%d", &N);

    for (int n = 0; n < N; ++n)
        scanf("%s", board[n]);

    computePath(0,   LEFT);
    computePath(N-1, RIGHT);

    int numOfCases = 0;
    for (int i = 0; i < N; ++i) { 
        Bag leftBag, rightBag;
        leftPath[i].collect(leftBag);
        rightPath[i].collect(rightBag);

        Bag::const_iterator leftIt  = leftBag.begin();
        Bag::const_iterator rightIt = rightBag.begin();

        while (leftIt != leftBag.end() && rightIt != rightBag.end()) {
            if (*leftIt == *rightIt) {
                numOfCases += (*leftIt++).count * (*rightIt++).count;
                numOfCases %= 1000000007;
            }
            else if (*leftIt < *rightIt) while (++leftIt != leftBag.end()   && *leftIt < *rightIt);
            else                         while (++rightIt != rightBag.end() && *rightIt < *leftIt);
        }
    }
    printf("%d\n", numOfCases);
}