#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <utility>
#include <climits>

using namespace std;

const int NO_ROAD = 0;

int N, M, X;
vector<vector<pair<int, int> > > road;

int dijkstra(int start, int goal) {
	start -= 1;
	goal  -= 1;

	vector<int> distances(N, INT_MIN);
	priority_queue<pair<int, int> > pq;
	int minDistance = 0;

	distances[start] = 0;
	pq.push(make_pair(0, start));

	while (!pq.empty()) {
		pair<int,int> p = pq.top();
		int dist_so_far = p.first;
		int here = p.second;
		pq.pop();

		if (here == goal) {
			minDistance = -dist_so_far;
			break;
		}
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

	return minDistance;
}

int solve() {
	int ret = 0;
	for (int i = 1; i <= N; ++i) {
		if (i == X) continue;

		int answer = dijkstra(i, X) + dijkstra(X, i);
		if (answer > ret) ret = answer;
	}

	return ret;
}

int main() {
	cin >> N >> M >> X;

	for (int n = 0; n < N; ++n) {
		vector<pair<int, int> > edge;
		road.push_back(edge);
	}

	for (int m = 0; m < M; ++m) {
		int start, end, T;
		cin >> start >> end >> T;
		road[start-1].push_back(make_pair(-T, end-1));
	}

	cout << solve() << '\n';

    return 0;
}
