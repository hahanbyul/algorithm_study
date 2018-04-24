#include <vector>
using std::vector;

int N, M;
int numOfChildren[500] = {}, numOfParent[500] = {};
bool visited[500];
vector<vector<int> > forwardEdge(500), backwardEdge(500);

int countChildren(int curNode, bool forward) {
    int* cache = forward? &numOfChildren[0] : &numOfParent[0];
    if (cache[curNode] != 0) return cache[curNode];

    // printf("curNode: %d\n", curNode + 1);
    int ret = 1;
    vector<vector<int> >& edge = forward? forwardEdge : backwardEdge;
    for (int nextNode : edge[curNode]) {
        if (!visited[nextNode]) {
            visited[nextNode] = true;
            int cnt = countChildren(nextNode, forward);
            // printf("next: %d (%d)\n", nextNode + 1, cnt);
            ret += cnt;
        }
    }

    // printf("%d: %d\n", curNode + 1, ret);
    cache[curNode] = ret;
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
        if (numOfChildren[n] == 0) {
            memset(visited, 0, N * sizeof(bool));
            countChildren(n, true);
        }
        if (numOfParent[n] == 0) {
            memset(visited, 0, N * sizeof(bool));
            countChildren(n, false);
        }
    }

    int totalStudent = 0;
    for (int n = 0; n < N; ++n) {
        // printf("%d: %d, %d\n", n, numOfChildren[n], numOfParent[n]);
        if (numOfChildren[n] + numOfParent[n] - 1 == N)
            ++totalStudent;
    }

    printf("%d", totalStudent);
    return 0;
}
