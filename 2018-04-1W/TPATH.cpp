// online test: PASS (https://cl.ly/0S0Z1I3U1q3q)

#include <queue>
#include <vector>
#include <algorithm>
#include <climits>
#include <iostream>

using namespace std;

using Cost = int;
using Next = int;

int C, N, M;
vector<pair<int, int> > adj[2000];

int dijkstra(int baseline) {
    vector<int> dist(N, INT_MIN);
    priority_queue<pair<Cost, Next> > pq;

    for (int i = 0; i < adj[0].size(); ++i) {
        int there = adj[0][i].first;
        int cost  = baseline - adj[0][i].second;

        if (cost <= 0) {
            dist[there] = cost;
            pq.push(make_pair(dist[there], there));
        }
    }

    while (!pq.empty()) {
        pair<Cost, Next> popped = pq.top();
        pq.pop();

        Cost minCost = popped.first;
        Next here    = popped.second;

        // cout << "[pop] here: " << here << ", cost: " << minCost << endl;

        if (here == N-1) return -minCost;

        if (dist[here] > minCost) continue;

        for (int i = 0; i < adj[here].size(); ++i) {
            int there = adj[here][i].first;
            int cost  = baseline - adj[here][i].second;
            if (cost > 0) continue;

            int nextCost = min(minCost, cost);
            if (dist[there] < nextCost) {
                dist[there] = nextCost;
                // cout << "[add] there: " << there << ", cost: " << nextCost << endl;
                pq.push(make_pair(dist[there], there));
            }
        }
    }

    return -1;
}

int main() {
    scanf("%d", &C);

    for (int c = 0; c < C; ++c) {
        scanf("%d %d", &N, &M);

        vector<bool> velocity(1000 + 1, false);
        for (int m = 0; m < M; ++m) {
            int a, b, c;
            scanf("%d %d %d", &a, &b, &c);
            adj[a].push_back(make_pair(b, c));
            adj[b].push_back(make_pair(a, c));

            velocity[c] = true;
        }

        int answer = INT_MAX;
        for (int v = 0; v <= 1000; ++v) {
            if (velocity[v]) {
                int cost = dijkstra(v);
                if (cost != -1) answer = min(answer, cost);
            }
        }
        printf("%d\n", answer);

        /*
        while (1) {
            int input;
            scanf("%d", &input);
            printf("%d\n", dijkstra(input));
        }
        */

        for (int n = 0; n < N; ++n) {
            adj[n].clear();
        }

    }

    return 0;
}
