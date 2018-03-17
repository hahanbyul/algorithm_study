#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <memory>
#include <tuple>

using std::cin;
using std::cout;
using std::string;
using std::vector;
using std::set;
using std::queue;
using std::tuple;
using std::make_tuple;
using std::get;

using sint = typename vector<int>::size_type;

void printVector(const vector<int>&);

class SortGame {
public:
	SortGame();
	void readInput();
	bool isSorted(const vector<int>&);
	vector<int> reverseSeq(const vector<int>&, int, int);
	int bfs();
	void insertNext(const vector<int>, int);
	bool isVisited(const vector<int>&);

private:
	int C, N;
	vector<int> initialSeq;
	set<vector<int>> visited;
	queue<tuple<vector<int>, int>> q;

};

SortGame::SortGame() {
	initialSeq.reserve(8);
}

void SortGame::readInput() {
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

int SortGame::bfs() {
	q.push(make_tuple(initialSeq, 0));
	visited.insert(initialSeq);

	while (q.size() > 0) {
		auto tp = q.front();
		const vector<int> v = get<0>(tp);
		// printVector(v);

		q.pop();

		int min_count = get<1>(tp);
		if (isSorted(v)) return min_count;
		insertNext(v, min_count);
	}
    return 0;
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
	return visited.find(v) != visited.end();
}

void SortGame::insertNext(const vector<int> v, int count) {
	for (sint i = 0; i < v.size() - 1; ++i) {
		for (sint j = i + 1; j < v.size(); ++j) {
			auto s = reverseSeq(v, i, j);

			if (!isVisited(s)) {
				q.push(make_tuple(s, count + 1));
				visited.insert(s);
			}
		}
	}
} 

void printVector(const vector<int>& V) {
	for (int v : V)
		cout << v << " ";
	cout << '\n';
}

int main() {
	int C;
	cin >> C;
	for (int c = 0; c < C; ++c) {
		auto sg = new SortGame();
		sg->readInput();
		cout << sg->bfs() << '\n';
	}

    return 0;
}
