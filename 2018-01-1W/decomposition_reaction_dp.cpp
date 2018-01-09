#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


class DecomReaction {
    public:
        int N, M;

        vector<int>* tree;
        vector<int>* tree_old;
        int* subtree_count;

        int** min_cut_with_root, ** min_cut_without_root;

        static const int root = 0;
        static const int INFINITY = 150;

        void readInput() {
            scanf("%d %d", &N, &M);
            tree_old = new vector<int>[N];
            tree     = new vector<int>[N];

            int v, w;
            for (int i = 0; i < N-1; i++) {
                scanf("%d %d", &v, &w);
                tree_old[v-1].push_back(w-1);
                tree_old[w-1].push_back(v-1);
            }
        }

        int solve() {
            subtree_count = new int[N];
            bool* visited = new bool[N];
            countSubtree(root, visited);
            delete[] tree_old;
            delete[] visited;

            min_cut_with_root = new int*[N];
            min_cut_without_root = new int*[N];

            for (int i = 0; i < N; i++) {
                min_cut_with_root[i]    = new int[N];
                min_cut_without_root[i] = new int[N];

                for (int j = 0; j < N; j++) {
                    min_cut_with_root[i][j]    = INFINITY;
                    min_cut_without_root[i][j] = INFINITY;
                }
            }

            int answer = min(solve_with_root(root, M, -1), solve_without_root(root, M, -1));
            cout << answer << endl;
            return answer;
        }

        ~DecomReaction() {
            delete[] tree;
            delete[] subtree_count;

            for (int i = 0; i < N; i++) {
                delete[] min_cut_with_root[i];
                delete[] min_cut_without_root[i];
            }

            delete[] min_cut_with_root;
            delete[] min_cut_without_root;
        }

        void printCache(vector<int>* cache) {
            for (int n = 0; n < N; n++) {
                cout << "node " << n << ": ";
                printVector(cache[n]);
            }
        }

        void printVector(vector<int> children) {
            for (vector<int>::iterator child = children.begin(); child != children.end(); child++) {
                cout << " " << *child;
            }
            cout << endl;
        }

    private:
        int countSubtree(int node, bool* visited) {
            vector<int> children = tree_old[node];
            vector<int>* children_new = &tree[node];

            visited[node] = true;

            subtree_count[node] = 1;
            for (vector<int>::iterator child = children.begin(); child != children.end(); child++) {
                if (visited[*child]) continue;

                subtree_count[node] += countSubtree(*child, visited);
                children_new->push_back(*child);
            }

            return subtree_count[node];
        }

        int solve_with_root(int node, int cut, int parent) {
            if (min_cut_with_root[node][cut] != INFINITY)
                return min_cut_with_root[node][cut];

            vector<int> children = tree[node];
            if (cut == 0) {
                min_cut_with_root[node][cut] = 1;
                return 1;
            }
            if (cut == 1) {
                min_cut_with_root[node][cut] = children.size()-1;
                return min_cut_with_root[node][cut];
            }

            int count = subtree_count[node];
            if (count < cut) {
                return INFINITY;
            }
            if (count == cut) {
                min_cut_with_root[node][cut] = 0;
                return 0;
            }

            solve_all_combination(0, cut-1, 0, 0, node, cut, parent);
            return min_cut_with_root[node][cut];
        }

        void solve_all_combination(int start, int goal, int progress, int answer, int node, int cut, int parent) {
            vector<int> children = tree[node];
            if (children[start] == parent) {
                if (start == children.size()-1) return;
                else solve_all_combination(start+1, goal, progress, answer, node, cut, parent);
            }
            if (start == children.size()-1) {
                int old_answer = min_cut_with_root[node][cut];
                int new_answer = answer + solve_with_root(children[start], goal - progress, node);
                min_cut_with_root[node][cut] = min(old_answer, new_answer);
                return;
            }

            for (int step = 0; step <= subtree_count[children[start]]; step++) {
                if (progress + step > goal) continue;

                int delta = solve_with_root(children[start], step, node);
                solve_all_combination(start+1, goal, progress + step, answer + delta, node, cut, parent);
            }

        }

        int solve_without_root(int node, int cut, int parent) {
            if (min_cut_without_root[node][cut] != INFINITY)
                return min_cut_without_root[node][cut];

            int count = subtree_count[node];
            if (count <= cut) {
                return INFINITY;
            }

            int ret = INFINITY;
            vector<int> children = tree[node];
            for (vector<int>::iterator child = children.begin(); child != children.end(); child++) {
                if (*child == parent) continue;
                ret = min(ret, 1 + solve_with_root(*child, cut, node));
                ret = min(ret, solve_without_root(*child, cut, node));
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
