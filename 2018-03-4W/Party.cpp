#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <utility>
#include <climits>

using namespace std;

const int NO_ROAD = 0;

int N, M, X;
vector<vector<int> > road;

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
		int dist = p.first;
		int here = p.second;
		pq.pop();

		if (here == goal) {
			minDistance = -dist;
			break;
		}
		if (distances[here] > dist) continue;

		for (int there = 0; there < road[here].size(); ++there) {
			if (road[here][there] == NO_ROAD) continue;

			if (distances[there] < dist + road[here][there]) {
				distances[there] = dist + road[here][there];
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
		vector<int> edge(N, NO_ROAD);
		road.push_back(edge);
	}

	for (int m = 0; m < M; ++m) {
		int start, end, T;
		cin >> start >> end >> T;
		road[start-1][end-1] = -T;
	}

	cout << solve() << '\n';

    return 0;
}
