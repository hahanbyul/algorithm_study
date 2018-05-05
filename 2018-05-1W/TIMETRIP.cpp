#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>
using std::vector;
using std::pair;
using std::make_pair;
using std::fill;

const int INF = 200000;
const bool REVERSED = true;

int G, W;
vector<pair<int, int> > adj[100];
bool reachable[100][100];

void bellmanFord(vector<int>& upper, bool reversed=false) {
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
                    updated = true;
                }
            }
        }
        if (!updated) break;
    }
}

bool isNegCycleReachable(const vector<int>& upper, bool reversed=false) {
    // 추가 iteration
    for (int here = 0; here < G; ++here) {
        for (int i = 0; i < adj[here].size(); ++i) {
            int there = adj[here][i].first;
            int cost  = adj[here][i].second;
            if (reversed) { cost = -cost; }

            if (upper[there] > upper[here] + cost) {
                if (reachable[0][here] && reachable[here][1]) {
                    return true;
                }
            }
        }
    }
    return false;
}

void floyd() {
    for (int i = 0; i < G; ++i) {
        for (int j = 0; j < G; ++j) {
            reachable[i][j] = false;
        }
    }

    for (int here = 0; here < G; ++here) {
        for (int i = 0; i < adj[here].size(); ++i) {
            int there = adj[here][i].first;
            reachable[here][there] = true;
        }
    }

    for (int k = 0; k < G; ++k) {
        for (int i = 0; i < G; ++i) {
            for (int j = 0; j < G; ++j) {
                reachable[i][j] = reachable[i][j] || (reachable[i][k] && reachable[k][j]);
            }
        }
    }
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

        floyd();
        if (!reachable[0][1]) {
            printf("UNREACHABLE\n");
            continue;
        }

        vector<int> upper(G, INF);
        upper[0] = 0;

        bellmanFord(upper);
        if (isNegCycleReachable(upper)) {
            printf("INFINITY ");
        }
        else {
            printf("%d ", upper[1]);
        }

        fill(upper.begin(), upper.end(), INF);
        upper[0] = 0;

        bellmanFord(upper, REVERSED);
        if (isNegCycleReachable(upper, REVERSED)) {
            printf("INFINITY\n");
        }
        else {
            printf("%d\n", -upper[1]);
        }
    }

    return 0;
}