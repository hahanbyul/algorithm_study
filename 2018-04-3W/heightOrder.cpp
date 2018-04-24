// link:   https://www.acmicpc.net/problem/2458
// result: https://cl.ly/0b031p26131A
#include <cstdio>
#include <cstring>
#include <vector>
using std::vector;

int N, M;
int numOfChildren[500] = {}, numOfParent[500] = {};
bool visited[500];
vector<vector<int> > forwardEdge(500), backwardEdge(500);

int countChildren(int curNode, bool forward) {
    int ret = 1;
    vector<vector<int> >& edge = forward? forwardEdge : backwardEdge;
    for (int nextNode : edge[curNode]) {
        if (!visited[nextNode]) {
            visited[nextNode] = true;
            int cnt = countChildren(nextNode, forward);
            ret += cnt;
        }
    }

    return ret;
}

int main() {
    scanf("%d %d", &N, &M);

    int a, b;
    for (int m = 0; m < M; ++m) {
        scanf("%d %d", &a, &b);
        forwardEdge[b-1].push_back(a-1);
        backwardEdge[a-1].push_back(b-1);
    }

    for (int n = 0; n < N; ++n) {
        memset(visited, 0, N * sizeof(bool));
        numOfChildren[n] = countChildren(n, true);

        memset(visited, 0, N * sizeof(bool));
        numOfParent[n] = countChildren(n, false);
    }

    int totalStudent = 0;
    for (int n = 0; n < N; ++n) {
        if (numOfChildren[n] + numOfParent[n] - 1 == N)
            ++totalStudent;
    }

    printf("%d", totalStudent);
    return 0;
}
