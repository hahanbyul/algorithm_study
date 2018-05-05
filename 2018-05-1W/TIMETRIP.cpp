// link:   https://algospot.com/judge/problem/read/TIMETRIP
// result: https://cl.ly/2F0l2o460m2N

#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>
using std::vector;
using std::pair;
using std::make_pair;

const int INF = 200000;

int G, W;
vector<pair<int, int> > adj[100];

bool isNegCycleReachable(const vector<int>& upper, bool reversed=false) {
    // 추가 iteration
    for (int here = 0; here < G; ++here) {
        if (upper[here] == INF) { continue; }
        for (int i = 0; i < adj[here].size(); ++i) {
            int there = adj[here][i].first;
            int cost  = adj[here][i].second;
            if (reversed) { cost = -cost; }

            if (upper[there] > upper[here] + cost) {
                return true;
            }
        }
    }
    return false;
}

bool bellmanFord(bool reversed=false) {
    vector<int> upper(G, INF);
    upper[0] = 0;

    bool updated;
    for (int iter = 0; iter < G - 1; ++iter) {
        updated = false;
        for (int here = 0; here < G; ++here) {
            if (upper[here] == INF) { continue; }
            for (int i = 0; i < adj[here].size(); ++i) {
                int there = adj[here][i].first;
                int cost  = adj[here][i].second;
                if (reversed) { cost = -cost; }

                if (upper[there] > upper[here] + cost) {
                    upper[there] = upper[here] + cost;
                    updated = true;
                }
            }
        }
        if (!updated) break;
    }

    if (upper[1] == INF) {
        return false;
    }

    if (updated && isNegCycleReachable(upper, reversed)) {
        printf("INFINITY");
    }
    else {
        if (!reversed) printf("%d", upper[1]);
        else           printf("%d", -upper[1]);
    }
    return true;
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

        bool reachable = bellmanFord();
        if (!reachable) {
            printf("UNREACHABLE\n");
            continue;
        }

        printf(" ");
        bellmanFord(true);
        printf("\n");
    }

    return 0;
}