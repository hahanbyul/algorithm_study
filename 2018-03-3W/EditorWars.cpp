i#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

using std::cin;
using std::cout;
using std::endl;
using std::min;
using std::string;
using std::map;
using std::pair;
using std::vector;

enum class OWNERSHIP{ MAP_HAS_BOTH, MAP_HAS_i, MAP_HAS_j, MAP_HAS_NEITHER };

const bool CONTRADICT = false;
const bool SUCCESS    = true;

class QuickUnion {
public:
	QuickUnion(int n) {
		id.reserve(n);
		size.reserve(n);

		for (int i = 0; i < n; i++) {
			id.push_back(i);
			size.push_back(1);
		}
	}

	bool mutualExclusiveUnion(string inputOpinion, int p, int q) {
		int i = root(p);
		int j = root(q);

		if (inputOpinion == "ACK") {
			if (connected(i, j))         return SUCCESS;
			if (isMutualExclusive(i, j)) return CONTRADICT;

			switch (checkOwnership(i, j)) {
			case OWNERSHIP::MAP_HAS_BOTH:
			{
				int i_pair = opposite(i);
				int j_pair = opposite(j);

				eraseFromDicts(j, j_pair);

				return mutualExclusiveUnion("ACK", i, j) && mutualExclusiveUnion("ACK", i_pair, j_pair);
			}

			case OWNERSHIP::MAP_HAS_NEITHER:
				union_(i, j);
				break;

			// map에 i, j 둘 중 하나만 있을 경우.
			case OWNERSHIP::MAP_HAS_i:
				union_(i, j);
				updateDictionary(i);
				break;

			case OWNERSHIP::MAP_HAS_j:
				union_(j, i);
				updateDictionary(j);
				break;
			}
		}
		else { // inputOpinion == "DIS"
			if (connected(i, j))         return CONTRADICT;
			if (isMutualExclusive(i, j)) return SUCCESS;

			switch (checkOwnership(i, j)) {
			case OWNERSHIP::MAP_HAS_BOTH:
			{
				int i_pair = opposite(i);
				int j_pair = opposite(j);

				eraseFromDicts(j, j_pair);

				return mutualExclusiveUnion("ACK", i, j_pair) && mutualExclusiveUnion("ACK", j, i_pair);
			}
			case OWNERSHIP::MAP_HAS_NEITHER:
				insertDicts(i, j);
				break;

				// map에 i, j 둘 중 하나만 있을 경우.
			case OWNERSHIP::MAP_HAS_i:
				return mutualExclusiveUnion("ACK", opposite(i), j);

			case OWNERSHIP::MAP_HAS_j:
				return mutualExclusiveUnion("ACK", opposite(j), i);
			}
		}

		return SUCCESS;
	}

	int countMaxPartySize(int N) {
		int partySize = N;
		map<int, int>::const_iterator it;
		for (it = dict.cbegin(); it != dict.cend(); ++it) {
			int firstSize  = size[it->first];
			int secondSize = size[it->second];
			partySize -= min(firstSize, secondSize);
		}
		return partySize;
	}

private:
	vector<int> id;
	vector<int> size;

	map<int, int> dict;
	map<int, int> dict_opposite;

	/********************* Quick union 구현 *********************/
	int root(int p) {
		int root = p;
		while (root != id[root])
			root = id[root];

		return root;
	}

	bool connected(int p, int q) {
		return root(p) == root(q);
	}

	void union_(int p, int q) {
		if (connected(p, q)) return;

		auto i = root(p);
		auto j = root(q);

		if (size[i] >= size[j]) {
			id[j] = i;
			size[i] += size[j];
			size[j] = 0;
		}
		else {
			id[i] = j;
			size[j] += size[i];
			size[i] = 0;
		}
	}
	/******************** Quick union 구현 끝 ********************/

	void insertDicts(int p, int q) {
		int i = root(p);
		int j = root(q);

		pair<int, int> pr(i, j);
		dict.insert(pr);

		pair<int, int> pr_(j, i);
		dict_opposite.insert(pr_);
	}

	void eraseFromDicts(int i, int j) {
		if (isInDictionary(dict, i) && dict[i] == j) {
			dict.erase(i);
			dict_opposite.erase(j);
		}
		if (isInDictionary(dict_opposite, i) && dict_opposite[i] == j) {
			dict_opposite.erase(i);
			dict.erase(j);
		}
	}

	void updateDictionary(int p) {
		if (p != root(p)) {
			updateDictionary(dict, p);
			updateDictionary(dict_opposite, p);
		}
	}

	void updateDictionary(const map<int, int>& dictionary, int p) {
		if (isInDictionary(dictionary, p)) {
			int p_pair = dictionary.at(p);
			eraseFromDicts(p, p_pair);
			insertDicts(root(p), p_pair);
		}
	}

	OWNERSHIP checkOwnership(int p, int q) {
		// 선행 조건: p, q가 대립쌍인 경우 걸러졌다고 생각한다
		if (isInAnyDicts(p) && isInAnyDicts(q))   return OWNERSHIP::MAP_HAS_BOTH;
		if (!isInAnyDicts(p) && !isInAnyDicts(q)) return OWNERSHIP::MAP_HAS_NEITHER;
		if (isInAnyDicts(p))					  return OWNERSHIP::MAP_HAS_i;
		if (isInAnyDicts(q))					  return OWNERSHIP::MAP_HAS_j;
	}

	bool isMutualExclusive(int p, int q) {
		int i = root(p);
		int j = root(q);

		if (isInAnyDicts(i)) return opposite(i) == j;
		else				 return false;
	}

	bool isInAnyDicts(int p) {
		return isInDictionary(dict, p) || isInDictionary(dict_opposite, p);
	}

	bool isInDictionary(const map<int, int>& dictionary, int p) {
		return dictionary.count(p) == 1;
	}

	int opposite(int i) {
		// 선행조건: dictionary 둘 중 하나에는 있다고 가정
		if (isInDictionary(dict, i))		  return dict[i];
		if (isInDictionary(dict_opposite, i)) return dict_opposite[i];
		return -1;
	}
};

int main() {
	int C;
	scanf("%d", &C);

	for (int c = 0; c < C; ++c) {
		int N, M;
		scanf("%d %d", &N, &M);
		auto qu = new QuickUnion(N);

		char opinion[4];
		int a, b;
		bool result = SUCCESS;
		int contradictNum = 0;
		for (int i = 0; i < M; i++) {
			scanf("%3s", opinion);
			scanf("%d %d", &a, &b);
			string s(opinion);

			if (result != CONTRADICT) result = qu->mutualExclusiveUnion(s, a, b);
			if (result == CONTRADICT && contradictNum == 0) contradictNum = i+1;
		}
		if (result == SUCCESS)    printf("MAX PARTY SIZE IS %d\n", qu->countMaxPartySize(N));
		if (result == CONTRADICT) printf("CONTRADICTION AT %d\n", contradictNum);
	}

    return 0;
}
