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

unsigned long long possibleStart[2];
unsigned long long possibleGoal[2];

const int RED = 0;
const int BLACK = 1;

void addEdge(int u, int v, int i) {
    --u, --v;

    adj[u].push_back(v);
    adj[v].push_back(u);

    if (u > v) { swap(u, v); }
    edges[u].push_back(make_pair(v, i));
}

int findEdge(int u, int v) {
    --u, --v;

    if (u > v) { swap(u, v); }
    for (int i = 0; i < edges[u].size(); ++i) {
        if (edges[u][i].first == v) {
            return edges[u][i].second;
        }
    }
    return -1;
}

void dfs(int u, int height, unsigned long long array[2]) {
    visited[u] = true;
    ++array[height % 2];

    for (int i = 0; i < adj[u].size(); ++i) {
        int there = adj[u][i];
        if (!visited[there]) {
            dfs(there, height + 1, array);
        }
    }
}

unsigned long long solve(int u, int v, int color) {
    int edgeIndex = findEdge(u, v);
    if (u > v) { swap(u, v); }

    if (cache[color][edgeIndex] != -1) {
        cout << "cached!" << endl;
        return cache[color][edgeIndex];
    }

    --u, --v;
    visited = vector<bool>(N, false);
    visited[u] = true;
    possibleGoal[0] = 0, possibleGoal[1] = 0;
    dfs(v, 1, possibleGoal);

    visited[u] = false;
    possibleStart[0] = 0, possibleStart[1] = 0;
    dfs(u, 0, possibleStart);

    cache[RED][edgeIndex]   = possibleStart[RED] * possibleGoal[RED] + possibleStart[BLACK] * possibleGoal[BLACK];
    cache[BLACK][edgeIndex] = possibleStart[RED] * possibleGoal[BLACK] + possibleStart[BLACK] * possibleGoal[RED];

    return cache[color][edgeIndex];
}

int main() {
    N = 6, M = 3;

    adj = vector<vector<int> >(N);
    edges = vector<vector<pair<int, int> > >(N-1);
    cache[0] = vector<unsigned long long>(N-1, -1);
    cache[1] = vector<unsigned long long>(N-1, -1);

    addEdge(2, 4, 0);
    addEdge(2, 5, 1);
    addEdge(2, 6, 2);
    addEdge(1, 2, 3);
    addEdge(3, 1, 4);

    cout << solve(1, 3, 0) << endl;    
    cout << solve(1, 3, 1) << endl;    
    cout << solve(2, 1, 0) << endl;    

    return 0;
}