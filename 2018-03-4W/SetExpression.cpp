#include <iostream>
#include <vector>

using namespace std;

class QuickUnion {
    public:
        QuickUnion(int _N): N(_N), id(_N), size(_N, 1) {
            for (int n = 0; n < N; ++n)
                id[n] = n;
        }

        int find(int p) {
            while (p != id[p]) p = id[p];
            return p;
        }

        void connected(int p, int q) {
            if (find(p) == find(q)) cout << "YES\n";
            else                    cout << "NO\n";
        }

        void unite(int p, int q) {
            int i = find(p);
            int j = find(q);

            if (i == j) return;

            if (size[i] >= size[j]) {
                id[j] = i;
                size[i] += size[j];
            } 
            else {
                id[i] = j;
                size[j] += size[i];
            }
        }

    private:
        int N;
        vector<int> id, size;
};

int main() {
    int n, m;
    cin >> n >> m;
    QuickUnion qu(n+1);
    for (int i = 0; i < m; ++i) {
        int op, a, b;
        cin >> op >> a >> b;
        if (op == 0) qu.unite(a, b);
        else         qu.connected(a, b);
    }
}
