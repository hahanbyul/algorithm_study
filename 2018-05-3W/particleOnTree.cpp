#include <cstdio>
#include <vector>
using namespace std;

int N, M;
vector<vector<int> > adj;
vector<bool> visited;

unsigned long long possibleStart[2];
unsigned long long possibleGoal[2];

const int RED = 0;
const int BLACK = 1;

void addEdge(int u, int v) {
    --u, --v;
    adj[u].push_back(v);
    adj[v].push_back(u);
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
    --u, --v;
    visited = vector<bool>(N, false);
    visited[u] = true;
    possibleGoal[0] = 0, possibleGoal[1] = 0;
    dfs(v, 1, possibleGoal);

    visited[u] = false;
    possibleStart[0] = 0, possibleStart[1] = 0;
    dfs(u, 0, possibleStart);

    return color == RED? possibleStart[RED] * possibleGoal[RED] + possibleStart[BLACK] * possibleGoal[BLACK] :
                         possibleStart[RED] * possibleGoal[BLACK] + possibleStart[BLACK] * possibleGoal[RED];
}

int main() {
    scanf("%d %d", &N, &M);
    adj = vector<vector<int> >(N);

    for (int n = 0; n < N-1; ++n) {
        int u, v;
        scanf("%d %d", &u, &v);
        addEdge(u, v);
    }

    for (int m = 0; m < M; ++m) {
        int u, v, c;
        scanf("%d %d %d", &u, &v, &c);
        printf("%lld\n", solve(u, v, c));
    }

    return 0;
}