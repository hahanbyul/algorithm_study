#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <utility>
#include <climits>

using namespace std;

int N, M, X;
vector<vector<pair<int, int> > > normalRoad, reversedRoad;

void dijkstra(vector<int>& distances, const vector<vector<pair<int, int> > >& road) {
    priority_queue<pair<int, int> > pq;

    distances[X] = 0;
    pq.push(make_pair(0, X));

    while (!pq.empty()) {
        pair<int,int> p = pq.top();
        int dist_so_far = p.first;
        int here = p.second;
        pq.pop();

        if (distances[here] > dist_so_far) continue;

        for (int i = 0; i < road[here].size(); ++i) {
            pair<int, int> edge = road[here][i];
            int dist  = edge.first;
            int there = edge.second;

            if (distances[there] < dist_so_far + dist) {
                distances[there] = dist_so_far + dist;
                pq.push(make_pair(distances[there], there));
            }

        }
    }
}

int solve() {
    vector<int> normalDist(N, INT_MIN);
    dijkstra(normalDist, reversedRoad);

    vector<int> reversedDist(N, INT_MIN);
    dijkstra(reversedDist, normalRoad);

    int ret = 0;
    for (int i = 1; i < N; ++i)
        ret = max(ret, -(normalDist[i] + reversedDist[i]));
    return ret;
}

int main() {
    cin >> N >> M >> X;
    N += 1;     // for array subscript

    for (int n = 0; n < N; ++n) {
        vector<pair<int, int> > edge;
        normalRoad.push_back(edge);
        reversedRoad.push_back(edge);
    }

    for (int m = 0; m < M; ++m) {
        int start, end, T;
        cin >> start >> end >> T;
        normalRoad[start].push_back(make_pair(-T, end));
        reversedRoad[end].push_back(make_pair(-T, start));
    }

    cout << solve() << '\n';

    return 0;
}
