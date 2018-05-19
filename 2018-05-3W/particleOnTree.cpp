#include <vector>
#include <iostream>
using namespace std;

int N, M;
vector<vector<int> > adj;
vector<bool> visited;

unsigned int possibleStart[2];
unsigned int possibleGoal[2];

const int RED = 0;
const int BLACK = 1;

void addEdge(int u, int v) {
    --u, --v;
    adj[u].push_back(v);
    adj[v].push_back(u);
}

void dfs(int u, int height, unsigned int array[2]) {
    cout << u + 1 << " " << height << endl;
    visited[u] = true;
    ++array[height % 2];

    for (int i = 0; i < adj[u].size(); ++i) {
        int there = adj[u][i];
        if (!visited[there]) {
            dfs(there, height + 1, array);
        }
    }
}

unsigned int solve(int u, int v, int color) {
    --u, --v;
    visited = vector<bool>(N, false);
    visited[u] = true;
    possibleGoal[0] = 0, possibleGoal[1] = 0;
    dfs(v, 1, possibleGoal);
    cout << "=> " << possibleGoal[0] << " " << possibleGoal[1] << endl;

    visited[u] = false;
    possibleStart[0] = 0, possibleStart[1] = 0;
    dfs(u, 0, possibleStart);
    cout << "=> " << possibleStart[0] << " " << possibleStart[1] << endl;

    return color == RED? possibleStart[RED] * possibleGoal[RED] + possibleStart[BLACK] * possibleGoal[BLACK] :
                         possibleStart[RED] * possibleGoal[BLACK] + possibleStart[BLACK] * possibleGoal[RED];
}

int main() {
    N = 6;
    adj = vector<vector<int> >(N);
    addEdge(2, 4);
    addEdge(2, 5);
    addEdge(2, 6);
    addEdge(1, 2);
    addEdge(3, 1);

    cout << solve(1, 3, RED) << endl;
    cout << solve(1, 3, BLACK) << endl;
    cout << solve(2, 1, 1) << endl;
    return 0;
}