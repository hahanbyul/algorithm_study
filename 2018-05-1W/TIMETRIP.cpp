#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>
using std::vector;
using std::pair;
using std::make_pair;
using std::fill;

const int INF = 100000;
const bool REVERSED = true;

int G, W;
vector<pair<int, int> > adj[100];

void bellmanFord(vector<int>& upper, vector<int>& from, bool reversed=false) {
    bool updated;
    for (int iter = 0; iter < G - 1; ++iter) {
        updated = false;
        for (int here = 0; here < G; ++here) {
            for (int i = 0; i < adj[here].size(); ++i) {
                int there = adj[here][i].first;
                int cost  = adj[here][i].second;
                if (reversed) { cost = -cost; }

                if (upper[there] > upper[here] + cost) {
                    upper[there] = upper[here] + cost;
                    from[there] = here;
                    updated = true;
                }
            }
        }
        if (!updated) break;
    }
}


bool dfs(int here, int goal, vector<bool>& visited) {
    for (int i = 0; i < adj[here].size(); ++i) {
        int there = adj[here][i].first;
        if (there == goal) { return true; }

        if (!visited[there]) {
            visited[there] = true;
            bool arrived = dfs(there, goal, visited);
            if (arrived) return true;
        }
    }
    return false;
}

bool reachable(int start, int goal) {
    vector<bool> visited(G, false);
    visited[start] = true;
    return dfs(start, goal, visited);
}

bool isNegCycleReachable(const vector<int>& upper, const vector<int>& from, bool reversed=false) {
    // 추가 iteration
    for (int here = 0; here < G; ++here) {
        for (int i = 0; i < adj[here].size(); ++i) {
            int there = adj[here][i].first;
            int cost  = adj[here][i].second;
            if (reversed) { cost = -cost; }

            if (upper[there] > upper[here] + cost) {
                if (reachable(0, here) && reachable(here, 1)) {
                    return true;
                }
            }
        }
    }
    return false;
}

int main() {
    int C;
    scanf("%d", &C);

    for (int c = 0; c < C; ++c) {
        scanf("%d %d", &G, &W);

        for (int g = 0; g < G; ++g) {
            adj[g].clear();
        }

        int a, b, d;
        for (int w = 0; w < W; ++w) {
            scanf("%d %d %d", &a, &b, &d);
            adj[a].push_back(make_pair(b, d));
        }

        vector<int> upper(G, INF);
        vector<int> from(G, -1);
        upper[0] = 0;

        bellmanFord(upper, from);
        if (upper[1] == INF) {
            printf("UNREACHABLE\n");
            continue;
        }

        if (isNegCycleReachable(upper, from)) {
            printf("INFINITY ");
        }
        else {
            printf("%d ", upper[1]);
        }

        fill(upper.begin(), upper.end(), INF);
        fill(from.begin(),  from.end(),  -1);
        upper[0] = 0;

        bellmanFord(upper, from, REVERSED);
        if (isNegCycleReachable(upper, from, REVERSED)) {
            printf("INFINITY\n");
        }
        else {
            printf("%d\n", -upper[1]);
        }
    }

    return 0;
}