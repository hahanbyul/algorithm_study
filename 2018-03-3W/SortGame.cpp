#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <memory>
#include <tuple>
#include <map>
#include <algorithm>

using std::sort;
using std::cin;
using std::cout;
using std::string;
using std::vector;
using std::set;
using std::map;
using std::queue;
using std::tuple;
using std::make_tuple;
using std::get;
using std::pair;

using sint = typename vector<int>::size_type;
const int MAX_NUM = 8;

void printVector(const vector<int>&);

class SortGame {
public:
	SortGame();
	void readInput();
	int solve();

private:
	int C, N;
	vector<int> initialSeq;
	map<vector<int>, int> cache;
	queue<tuple<vector<int>, int>> q;

	bool isSorted(const vector<int>&);
	vector<int> reverseSeq(const vector<int>&, int, int);
	void insertNext(const vector<int>, int);
	bool isVisited(const vector<int>&);

	vector<int> arithmaticSeq(int);
	void doCaching(int);
	vector<int> normalize(const vector<int>& v);
	int solve(const vector<int>& v);
};

SortGame::SortGame() {
	doCaching(MAX_NUM);
}

void SortGame::readInput() {
	initialSeq.clear();

	cin >> N;

	for (int i = 0; i < N; ++i) {
		int element;
		cin >> element;
		initialSeq.push_back(element);
	}
}

bool SortGame::isSorted(const vector<int>& vec) {
	for (vector<int>::size_type i = 1; i <= vec.size(); ++i)
		if (i != vec[i-1]) return false;

	return true;
}

vector<int> SortGame::arithmaticSeq(int n) {
	vector<int> v;
	for (int i = 0; i < n; ++i)
		v.push_back(i);

	return v;
}

void SortGame::doCaching(int n) {
	vector<int> seq = arithmaticSeq(n);
	q.push(make_tuple(seq, 0));
	cache.insert(make_pair(seq, 0));

	int count = 1;
	while (q.size() > 0) {
		auto tp = q.front();
		q.pop();

		const vector<int> v = get<0>(tp);
		int min_count = get<1>(tp);

		// printVector(v);
		// cout << "->" << min_count << "->" << count++ << '\n';

		insertNext(v, min_count);
	}
}

vector<int> SortGame::reverseSeq(const vector<int>& v, int start, int end) {
	vector<int> reversed(v);

	int mid = (end - start) / 2;
	for (int i = 0; i <= mid; ++i) {
		int temp = reversed[start + i];
		reversed[start + i] = reversed[end - i];
		reversed[end - i] = temp;
	}

	return reversed;
}

bool SortGame::isVisited(const vector<int>& v) {
	return cache.count(v) == 1;
}

void SortGame::insertNext(const vector<int> v, int count) {
	for (sint i = 0; i < v.size() - 1; ++i) {
		for (sint j = i + 1; j < v.size(); ++j) {
			auto s = reverseSeq(v, i, j);

			if (!isVisited(s)) {
				q.push(make_tuple(s, count + 1));
				cache.insert(make_pair(s, count + 1));
			}
		}
	}
} 

vector<int> SortGame::normalize(const vector<int>& v) {
	vector<pair<int, int>> paired_v;
	for (sint i = 0; i < v.size(); ++i) {
		pair<int, int> p(v[i], i);
		paired_v.push_back(p);
	}

	sort(paired_v.begin(), paired_v.end(), [](const pair<int, int> & a, const pair<int, int>& b) { return a.first < b.first; });

	vector<int> normed_v(v);
	for (int i = 0; i < v.size(); ++i)
		normed_v[paired_v[i].second] = i;
	

	for (int i = normed_v.size(); i < MAX_NUM; ++i)
		normed_v.push_back(i);

	return normed_v;
}

int SortGame::solve() {
	return solve(initialSeq);
}

int SortGame::solve(const vector<int>& v) {
	// printVector(normalize(v));
	return cache[normalize(v)];
}

void printVector(const vector<int>& V) {
	for (int v : V)
		cout << v << " ";
	// cout << '\n';
}

int main() {
	auto sg = new SortGame();
	int C;
	cin >> C;
	for (int c = 0; c < C; ++c) {
		sg->readInput();
		cout << sg->solve() << '\n';
	}

    return 0;
}


