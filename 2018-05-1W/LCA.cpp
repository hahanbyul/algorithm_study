#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using std::vector;
using std::swap;

#define MAX_HEIGHT 16
#define MAX_NODE   50000

vector<int> adj[MAX_NODE];
int depth[MAX_NODE];
int parent[MAX_NODE][MAX_HEIGHT + 1];

void dfs(int here) {
    for (int i = 0; i < adj[here].size(); ++i) {
        int there = adj[here][i];
        if (depth[there] == -1) {
            parent[there][0] = here;
            depth[there] = depth[here] + 1;
            dfs(there);
        }
    }
}

int findLCA(int u, int v) {
    if (depth[u] < depth[v]) swap(u, v);

    int diff = depth[u] - depth[v];
    for (int height = 0; diff > 0; ++height) {
        if (diff % 2 == 1) u = parent[u][height];
        diff /= 2;
    }

    if (u != v) {
        for (int height = MAX_HEIGHT; height >= 0; --height) {
            if (parent[u][height] != -1 && parent[u][height] != parent[v][height]) {
                u = parent[u][height];
                v = parent[v][height];
            }
        }
        u = parent[u][0];
    }

    return u;
}

int main() {
    int N;
    scanf("%d", &N);

    for (int n = 0; n < N-1; ++n) {
        int a, b;
        scanf("%d %d", &a, &b);
        --a, --b;

        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    memset(parent, -1, sizeof(parent));
    memset(depth, -1, N*sizeof(int));
    depth[0] = 0;
    dfs(0);

    for (int height = 0; height < MAX_HEIGHT; ++height) {
        for (int current = 1; current < N; ++current) {
            if (parent[current][height] != -1) {
                parent[current][height + 1] = parent[parent[current][height]][height];
            }
        }
    }

    int M;
    scanf("%d", &M);

    for (int m = 0; m < M; ++m) {
        int a, b;
        scanf("%d %d", &a, &b);
        --a, --b;
        printf("%d\n", findLCA(a, b) + 1);
    }

}
