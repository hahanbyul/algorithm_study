#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


class DecomReaction {
    public:
        int N, M;
        bool** graph;

        vector<int>* tree;
        int* subtree_count;

        int** min_cut_with_root, ** min_cut_without_root;

        static const int root = 0;
        static const int INFINITY = 150;

        void readInput() {
            cin >> N >> M;
            graph = new bool*[N];
            for (int n = 0; n < N; n++)
                graph[n] = new bool[N];

            int v, w;
            for (int i = 0; i < N-1; i++) {
                cin >> v >> w;
                graph[v-1][w-1] = true;
                graph[w-1][v-1] = true;
            }
        }

        int solve() {
            constructTree();

            subtree_count = new int[N];
            countSubtree(root);

            min_cut_with_root = new int*[N];
            min_cut_without_root = new int*[N];

            for (int i = 0; i < N; i++) {
                min_cut_with_root[i] = new int[N];
                min_cut_without_root[i] = new int[N];

                for (int j = 0; j < N; j++) {
                    min_cut_with_root[i][j]    = INFINITY;
                    min_cut_without_root[i][j] = INFINITY;
                }
            }

            int answer = min(solve_with_root(root, M), solve_without_root(root, M));
            cout << answer << endl;
            return answer;
        }

    private:
        void constructTree() {
            tree = new vector<int>[N];
            bool* visited = new bool[N];
            addChild(root, visited);
        }

        void addChild(int node, bool* visited) {
            visited[node] = true;
            bool* children = graph[node];

            for (int child = 0; child < N; child++) {
                bool isChild = children[child];
                if (!isChild) continue;
                if (visited[child]) continue;

                tree[node].push_back(child);
                addChild(child, visited);
            }
        }

        int countSubtree(int node) {
            vector<int> children = tree[node];

            subtree_count[node] = 1;
            for (vector<int>::iterator child = children.begin(); child != children.end(); child++)
                subtree_count[node] += countSubtree(*child);

            return subtree_count[node];
        }

        int solve_with_root(int node, int cut) {
            if (min_cut_with_root[node][cut] != INFINITY)
                return min_cut_with_root[node][cut];

            vector<int> children = tree[node];
            if (cut == 0) {
                min_cut_with_root[node][cut] = 1;
                return 1;
            }
            if (cut == 1) {
                min_cut_with_root[node][cut] = children.size();
                return children.size();
            }

            int count = subtree_count[node];
            if (count < cut) {
                return INFINITY;
            }
            if (count == cut) {
                min_cut_with_root[node][cut] = 0;
                return 0;
            }

            solve_all_combination(0, cut-1, 0, 0, node, cut);
            return min_cut_with_root[node][cut];
        }

        void solve_all_combination(int start, int goal, int progress, int answer, int root, int cut) {
            vector<int> children = tree[root];
            if (start == children.size()-1) {
                int old_answer = min_cut_with_root[root][cut];
                int new_answer = answer + solve_with_root(children[start], goal - progress);
                min_cut_with_root[root][cut] = min(old_answer, new_answer);
                return;
            }

            for (int step = 0; step <= subtree_count[children[start]]; step++) {
                if (progress + step > goal) continue;

                int delta = solve_with_root(children[start], step);
                solve_all_combination(start+1, goal, progress + step, answer + delta, root, cut);
            }

        }

        int solve_without_root(int node, int cut) {
            if (min_cut_without_root[node][cut] != INFINITY)
                return min_cut_without_root[node][cut];

            int count = subtree_count[node];
            if (count <= cut) {
                return INFINITY;
            }

            int ret = INFINITY;
            vector<int> children = tree[node];
            for (vector<int>::iterator child = children.begin(); child != children.end(); child++) {
                ret = min(ret, 1 + solve_with_root(*child, cut));
                ret = min(ret, solve_without_root(*child, cut));
            }

            min_cut_without_root[node][cut] = ret;
            return ret;
        }
};

int main() {
    DecomReaction dr = DecomReaction();
    dr.readInput();
    dr.solve();
    return 0;
}
