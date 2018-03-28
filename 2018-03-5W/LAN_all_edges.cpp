#include <vector>
#include <algorithm>
#include <utility>
#include <cmath>
#include <iostream>

using namespace std;
using Edge = pair<int, int>;
using Cost = double;

void readCoord(int N, vector<int>& coord) {
    for (int n = 0; n < N; ++n)
        scanf("%d", &coord[n]);
}

double square(int x) {
    return x*x;
}

double distance(const vector<int>& x, const vector<int>& y, int i, int j) {
    return sqrt(square(x[i] - x[j]) + square(y[i] - y[j]));
}

class QuickUnion {
    vector<int> id, sz;

public:
    QuickUnion(int N) : id(N), sz(N, 1) {
        for (int n = 0; n < N; ++n) {
            id[n] = n;
        }
    }

    int size(int p) {
        return sz[p];
    }

    int find(int p) {
        while (p != id[p])
            p = id[p];
        return p;
    }

    bool connected(int p, int q) {
        return find(p) == find(q);
    }

    bool connected(Edge e) {
        return connected(e.first, e.second);
    }

    bool spanned(int p) {
        return sz[find(p)] == id.size();
    }

    bool spanned(Edge e) {
        return spanned(e.first);
    }

    bool unite(int p, int q) {
        int i = find(p);
        int j = find(q);

        if (i == j) return false;

        if (sz[i] >= sz[j]) {
            id[j] = i;
            sz[i] += sz[j];
        } else {
            id[i] = j;
            sz[j] += sz[i];
        }
        return true;
    }

    bool unite(Edge e) {
        return unite(e.first, e.second);
    }
};

int main() {
    int C;
    scanf("%d", &C);

    for (int c = 0; c < C; ++c) {
        int N, M;
        scanf("%d %d", &N, &M);

        vector<int> coordX(N), coordY(N);
        readCoord(N, coordX);
        readCoord(N, coordY);

        auto qu = QuickUnion(N);
        for (int m = 0; m < M; ++m) {
            int a, b;
            scanf("%d %d", &a, &b);
            qu.unite(a, b);
        }

        vector<pair<Cost, Edge> > cand;
        for (int i = 0; i < N-1; ++i) {
            for (int j = i+1; j < N; ++j) {
                double cost = distance(coordX, coordY, i, j);
                Edge   edge = make_pair(i, j);
                cand.push_back(make_pair(cost, edge));
            }
        }

        sort(cand.begin(), cand.end());

        int connectedEdges = M;
        double totalDist = 0;
        for (pair<Cost, Edge> p : cand) {
            double cost = p.first;
            Edge   edge = p.second;

            cout << "EDGE: " << edge.first << ", " << edge.second << endl;

            if (qu.connected(edge)) continue;

            qu.unite(edge);

            int root = qu.find(edge.first);
            cout << "ROOT: " << root << " (size: " << qu.size(root) << ")" << endl;
            ++connectedEdges;
            totalDist += cost;

            if (qu.spanned(edge)) break;
        }

        printf("%f", totalDist);

    }
}