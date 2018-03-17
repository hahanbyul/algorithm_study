#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

using std::cin;
using std::cout;
using std::endl;
using std::min;
using std::max;
using std::string;
using std::map;
using std::pair;
using std::vector;

enum class OWNERSHIP{ MAP_HAS_BOTH, MAP_HAS_i, MAP_HAS_j, MAP_HAS_NEITHER };

const bool CONTRADICT = false;
const bool SUCCESS    = true;

class QuickUnion {
public:
	QuickUnion(int n): id(n), size(n, 1), enemy(n, -1), count(n) {
		for (int i = 0; i < n; ++i)
			id.push_back(i);
	}

    bool dis(int u, int v) {
        u = root(u);
        v = root(v);

        if (u == v) return CONTRADICT;

        int a = union_(u, enemy[v]);
        int b = union_(v, enemy[u]);

        enemy[a] = b;
        enemy[b] = a;

        return SUCCESS;
    }

    bool ack(int u, int v) {
        u = root(u);
        v = root(v);

        if (enemy[u] == v) return CONTRADICT;

        int a = union_(u, v);
        int b = union_(enemy[u], enemy[v]);

        enemy[a] = b;
        if (b != -1) enemy[b] = a;

        return SUCCESS;
    }

	int countMaxPartySize(int N) {
		int partySize = N;
		for (int i = 0; i < enemy.size(); ++i) {
            if (enemy[i] == -1) continue;
			partySize -= min(size[i], size[enemy[i]]);

            enemy[i] = -1;
            enemy[enemy[i]] = -1;
		}

		return partySize;
	}

private:
	vector<int> id;
	vector<int> size;
    int count;
    vector<int> enemy;

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

	int union_(int p, int q) {
        if (p == -1 || q == -1) return max(p, q);

		auto i = root(p);
		auto j = root(q);

        if (i == j) return i;

        count--;

		if (size[i] >= size[j]) {
			id[j] = i;
			size[i] += size[j];
			size[j] = 0;
            return i;
		}
		else {
			id[i] = j;
			size[j] += size[i];
			size[i] = 0;
            return j;
		}
	}

	/******************** Quick union 구현 끝 ********************/
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
		bool result;
		for (int i = 0; i < M; i++) {
			scanf("%3s", opinion);
			string s(opinion);
			scanf("%d %d", &a, &b);

            if (s == "DIS")   result = qu->dis(a, b);
            else  /* "ACK" */ result = qu->ack(a, b);

			if (result == CONTRADICT) {
				printf("CONTRADICTION AT %d\n", i + 1);
				break;
			}
		}
		if (result == SUCCESS) printf("MAX PARTY SIZE IS %d\n", qu->countMaxPartySize(N));
	}

    return 0;
}
