#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, M, X;
vector<vector<int>> road;

struct Pair {
	int dist, next;

	Pair(int _dist, int _next): dist(_dist), next(_next) {}

	int operator<(Pair p) {
		return dist < p.dist;
	}
};

void push_next(vector<Pair>& frontier, vector<bool>& visited, int start, int prev_dist) {
	for (int next = 0; next < N; ++next) {
		int dist = road[start][next];

		if (dist != 0 && !visited[next]) {
			Pair p(prev_dist + dist, next);
			frontier.push_back(p);
			push_heap(frontier.begin(), frontier.end());
		}
	}
	visited[start] = true;
}

int bfs(int start, int goal) {
	start -= 1;
	goal  -= 1;
	vector<bool> visited(N, false);

	vector<Pair> frontier;
	push_next(frontier, visited, start, 0);

	while (frontier.size() > 0) {
		Pair p = frontier.front();
		if (p.next == goal) return -p.dist;

		pop_heap(frontier.begin(), frontier.end());
		frontier.pop_back();

		push_next(frontier, visited, p.next, p.dist);
	}

	return 0;
}

int solve() {
	int ret = 0;
	for (int i = 1; i <= N; ++i) {
		if (i == X) continue;
		int answer = bfs(i, X) + bfs(X, i);
		if (answer > ret) ret = answer;
	}

	return ret;
}

int main() {
	cin >> N >> M >> X;

	for (int n = 0; n < N; ++n) {
		vector<int> to(N, 0);
		road.push_back(to);
	}

	for (int m = 0; m < M; ++m) {
		int start, end, T;
		cin >> start >> end >> T;
		road[start-1][end-1] = -T;
	}

	cout << solve() << '\n';

    return 0;
}
