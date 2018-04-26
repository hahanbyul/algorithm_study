// link:   https://www.acmicpc.net/problem/1865
// result: https://cl.ly/0D3O2D452r2S
#include <cstdio>
#include <vector>
#include <utility>
using std::vector;
using std::pair;
using std::make_pair;

#define INF 5000000

vector<pair<int, int> > adj[500];

bool hasNegativeCycle(const vector<int>& from) {
    int N = from.size();

    for (int i = 0; i < adj[0].size(); ++i) {
        vector<int> visited(N, false);
        visited[0] = true;

        int here = adj[0][i].first;
        while (here != 0) {
            if (visited[here]) { 
                return true;
            }

            visited[here] = true;
            here = from[here];
        }
    }

    return false;
}

int main() {
    int C;
    scanf("%d", &C);
    for (int c = 0; c < C; ++c) {
        int N, M, W;
        scanf("%d %d %d", &N, &M, &W);

        for (int n = 0; n < N; ++n) {
            adj[n].clear();
        }

        int S, E, T;

        // read road
        for (int m = 0; m < M; ++m) {
            scanf("%d %d %d", &S, &E, &T);
            adj[S-1].push_back(make_pair(E-1, T));
            adj[E-1].push_back(make_pair(S-1, T));
        }

        // read wormhole
        for (int w = 0; w < W; ++w) {
            scanf("%d %d %d", &S, &E, &T);
            adj[S-1].push_back(make_pair(E-1, -T));
        }

        // bellman ford
        vector<int> upper(N, INF);
        vector<int> from(N, -1);
        upper[0] = 0;
        bool updated;

        for (int iter = 0; iter < N; ++iter) {
            updated = false;
            for (int here = 0; here < N; ++here) {
                for (int i = 0; i < adj[here].size(); ++i) {
                    int there = adj[here][i].first;
                    int cost  = adj[here][i].second;

                    if (upper[there] > upper[here] + cost) {
                        upper[there] = upper[here] + cost;
                        from[there] = here;
                        updated = true;
                    }
                }
            }
            if (!updated) break;
        }

        if (adj[0].empty()) {                                // 0에서 경로가 없으면 (돌아오는 것이 불가능하면)
            printf("NO\n");
        }
        else if (upper[0] < 0) {                             // 이미 최단 거리가 (-)이면
            printf("YES\n");
        } 
        else if (updated && hasNegativeCycle(from)) {        // V번째 iteration에서 update됐으면 음수 cycle이 있는지 체크
            printf("YES\n");
        }
        else {
            printf("NO\n");
        }
    }

    return 0;
}

