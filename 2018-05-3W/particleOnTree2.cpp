#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
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

    printf("(%d): 0 -> %lld, 1 -> %lld\n", parent + 1, children[0][parent], children[1][parent]);
}

void dfs(int parent, int prevStart[2]) {
    visited[parent] = true;

    for (int i = 0; i < adj[parent].size(); ++i) {
        int child = adj[parent][i];
        if (!visited[child]) {
            printf("edge: (%d %d), prevSum: (%d %d)\n", parent + 1, child + 1, prevStart[0], prevStart[1]);
            int edgeIndex = findEdge(parent, child);

            int start[2];
            start[0] = prevStart[1] + children[0][parent] - children[1][child];
            start[1] = prevStart[0] + children[1][parent] - children[0][child];
            printf("start: %d %d\n", start[0], start[1]);

            cache[RED][edgeIndex]   = children[0][child] * start[1] + children[1][child] * start[0];
            cache[BLACK][edgeIndex] = children[1][child] * start[1] + children[0][child] * start[0];
            printf("end: %d %d\n", children[0][child], children[1][child]);
            printf("cache: (%lld %lld)\n", cache[RED][edgeIndex], cache[BLACK][edgeIndex]);

            dfs(child, start);
        }
    }
}

unsigned long long solve(int u, int v, int color) {
    int edgeIndex = findEdge(u-1, v-1);
    printf("%lld\n", cache[color][edgeIndex]);
}

void init() {
    visited = vector<bool>(N, false);
    countChildren(0);

    visited = vector<bool>(N, false);
    int prevStart[2] = {0, 0};
    dfs(0, prevStart);
}

int main() {
    N = 6, M = 3;

    adj = vector<vector<int> >(N);
    edges = vector<vector<pair<int, int> > >(N-1);
    cache[0] = vector<unsigned long long>(N-1, -1);
    cache[1] = vector<unsigned long long>(N-1, -1);
    children[0] = vector<unsigned long long>(N, 0);
    children[1] = vector<unsigned long long>(N, 0);

    addEdge(2, 4, 0);
    addEdge(2, 5, 1);
    addEdge(2, 6, 2);
    addEdge(1, 2, 3);
    addEdge(3, 1, 4);

    init();

    solve(1, 3, 0);
    solve(1, 3, 1);
    solve(2, 1, 1);

    return 0;
}