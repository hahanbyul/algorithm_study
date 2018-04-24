#include <vector>
using std::vector;

int N, M;
int numOfChildren[500], numOfParent[500];
vector<int> forwardEdge[500];

int countChildren(int curNode, vector<bool>& visited) {
    // printf("curNode: %d\n", curNode + 1);
    int ret = 1;
    for (int nextNode : forwardEdge[curNode]) {
        if (!visited[nextNode]) {
            visited[nextNode] = true;
            int cnt = countChildren(nextNode, visited);
            // printf("next: %d (%d)\n", nextNode + 1, cnt);
            ret += cnt;
        }
    }

    // printf("%d: %d\n", curNode + 1, ret);
    return ret;
}

int main() {
    scanf("%d %d", &N, &M);

    int a, b;
    for (int m = 0; m < M; ++m) {
        scanf("%d %d", &a, &b);
        forwardEdge[b-1].push_back(a-1);
    }

    for (int n = 0; n < N; ++n) {
        vector<bool> visited(N, false);
        printf("%d\n", countChildren(n, visited) - 1);
    }

    return 0;
}
