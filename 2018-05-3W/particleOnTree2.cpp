#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int N, M;
vector<vector<int> > adj;
vector<bool> visited;
vector<vector<pair<int, int> > > edges;
vector<unsigned long long> cache[2];
vector<unsigned long long> children[2];

const int RED   = 0;
const int BLACK = 1;

void addEdge(int u, int v, int i) {
    --u, --v;

    adj[u].push_back(v);
    adj[v].push_back(u);

    if (u > v) { swap(u, v); }
    edges[u].push_back(make_pair(v, i));
}

int findEdge(int u, int v) {
    if (u > v) { swap(u, v); }
    for (int i = 0; i < edges[u].size(); ++i) {
        if (edges[u][i].first == v) {
            return edges[u][i].second;
        }
    }
    return -1;
}

void countChildren(int parent) {
    visited[parent] = true;
    children[0][parent] = 1;

    for (int i = 0; i < adj[parent].size(); ++i) {
        int child = adj[parent][i];
        if (!visited[child]) {
            countChildren(child);
            children[0][parent] += children[1][child];
            children[1][parent] += children[0][child];
        }
    }
}

void dfs(int parent, unsigned long long prevStart[2]) {
    visited[parent] = true;

    for (int i = 0; i < adj[parent].size(); ++i) {
        int child = adj[parent][i];
        if (!visited[child]) {
            int edgeIndex = findEdge(parent, child);

            unsigned long long start[2];
            start[0] = prevStart[1] + children[0][parent] - children[1][child];
            start[1] = prevStart[0] + children[1][parent] - children[0][child];

            cache[RED][edgeIndex]   = children[0][child] * start[1] + children[1][child] * start[0];
            cache[BLACK][edgeIndex] = children[1][child] * start[1] + children[0][child] * start[0];

            dfs(child, start);
        }
    }
}

void init() {
    visited = vector<bool>(N, false);
    countChildren(0);

    visited = vector<bool>(N, false);
    unsigned long long prevStart[2] = {0, 0};
    dfs(0, prevStart);
}

void solve(int u, int v, int color) {
    int edgeIndex = findEdge(u-1, v-1);
    printf("%lld\n", cache[color][edgeIndex]);
}

int main() {
    scanf("%d %d", &N, &M);

    adj = vector<vector<int> >(N);
    edges = vector<vector<pair<int, int> > >(N-1);

    cache[0] = vector<unsigned long long>(N-1, -1);
    cache[1] = vector<unsigned long long>(N-1, -1);

    children[0] = vector<unsigned long long>(N, 0);
    children[1] = vector<unsigned long long>(N, 0);

    for (int n = 0; n < N-1; ++n) {
        int u, v;
        scanf("%d %d", &u, &v);
        addEdge(u, v, n);
    }

    init();

    for (int m = 0; m < M; ++m) {
        int u, v, c;
        scanf("%d %d %d", &u, &v, &c);
        solve(u, v, c);
    }

    return 0;
}