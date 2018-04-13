// online test: PASS - 400ms (https://cl.ly/3y462S1c3p1s)

#include <queue>
#include <vector>
#include <algorithm>
#include <climits>
#include <iostream>

using namespace std;

int C, N, M;

struct Edge {
    int start, end, cost;
    Edge(int a, int b, int c) : start(a), end(b), cost(c) {}
    bool operator< (const Edge& e) const { return cost < e.cost; }
};

class QuickUnion {
    vector<int> size, id;

public:
    QuickUnion(int n) : size(n, 1), id(n) {
        for (int i = 0; i < n; ++i)
            id[i] = i;
    }

    int find(int p) {
        while (p != id[p]) p = id[p];
        return p;
    }

    bool isConnected(Edge e) {
        return isConnected(e.start, e.end);
    }

    bool isConnected(int p, int q) {
        return find(p) == find(q);
    }

    void connect(Edge e) {
        connect(e.start, e.end);
    }

    void connect(int p, int q) {
        int i = find(p);
        int j = find(q);
        if (i == j) return;

        if (size[i] > size[j]) {
            id[j] = i;
            size[i] += size[j];
        } else {
            id[i] = j;
            size[j] += size[i];
        }
    }
};

int main() {
    scanf("%d", &C);

    for (int c = 0; c < C; ++c) {
        scanf("%d %d", &N, &M);
        vector<Edge> adj;

        vector<int> velocity(1000 + 1, 0);
        for (int m = 0; m < M; ++m) {
            int a, b, c;
            scanf("%d %d %d", &a, &b, &c);
            adj.push_back(Edge(a, b, c));
            ++velocity[c];
        }

        vector<int> velocityIndex;
        int index = 0;
        for (int i = 0; i <= 1000; ++i) {
            if (velocity[i] == 0)  continue;
            // if (index + N - 1 > M) break;

            velocityIndex.push_back(index);
            index += velocity[i];
        }

        sort(adj.begin(), adj.end());

        int ret = 1000;
        for (auto start : velocityIndex) {
            QuickUnion qu(N);

            int lowerBound = adj[start].cost;
            int upperBound = -1;

            // cout << "lowerBound: " << lowerBound << endl;

            while (start < M) {
                Edge e = adj[start];
                // cout << "edge: " << e.cost << "(" << e.start << ", " << e.end << ")\n";

                if (e.cost - lowerBound > ret) { break; }
                if (!qu.isConnected(e))        { qu.connect(e); }
                if (qu.isConnected(0, N-1))    { 
                    upperBound = e.cost;
                    break; 
                }

                ++start;
            }

            if (upperBound != -1) ret = min(ret, upperBound - lowerBound);
            // cout << "ret: " << ret << endl;
        }

        printf("%d\n", ret);
    }

    return 0;
}
