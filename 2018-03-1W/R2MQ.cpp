#include <iostream>
#include <vector>
using namespace std;

struct RMQ {
    int n;
    vector<int> rangeMin[2];
    vector<int> rangeMin_old;
    // const int INT_MAX = numeric_limits<int>::max();

    RMQ(const vector<int>& array) {
        n = array.size();
        rangeMin[0].resize(n*4);
        rangeMin[1].resize(n*4);
        init(array, 0, n-1, 1);
    }

    vector<int> init(const vector<int>& array, int left, int right, int node) {
        vector<int> answer;
        if (left == right) {
            rangeMin[0][node] = array[left];
            rangeMin[1][node] = array[left];

            answer.push_back(array[left]);
            answer.push_back(array[left]);

            return answer;
        }

        int mid = (left + right) / 2;
        vector<int> leftMin  = init(array, left,    mid,   node * 2);
        vector<int> rightMin = init(array, mid + 1, right, node * 2 + 1);
        vector<int> min_vals = min_top2(leftMin, rightMin);

        rangeMin[0][node] = min_vals[0];
        rangeMin[1][node] = min_vals[1];

        return min_vals;
    }

    vector<int> min_top2(vector<int> leftMin, vector<int> rightMin) {
        vector<int> answer;

        answer.push_back(min(leftMin[0], rightMin[0]));
        if (leftMin[0] <  rightMin[0]) answer.push_back(min(leftMin[1], rightMin[0]));
        if (leftMin[0] >= rightMin[0]) answer.push_back(min(leftMin[0], rightMin[1]));

        return answer;
    }

    /*
    int query(int left, int right, int node, int nodeLeft, int nodeRight) {
        if (left >  nodeRight || right <  nodeLeft)  return INT_MAX;
        if (left <= nodeLeft  && right >= nodeRight) return rangeMin[node];

        int mid = (nodeLeft + nodeRight) / 2;
        return min(query(left, right, node * 2, nodeLeft, mid),
                   query(left, right, node * 2 + 1, mid + 1, nodeRight));
    }

    int query(int left, int right) {
        return query(left, right, 1, 0, n-1);
    }
    */

};

int main() {
    int array[] = {0, 0, 1, 1, 1, 1, 2, 3, 3, 3, 4};
    vector<int> A (array, array + sizeof(array) / sizeof(array[0]));
    for (int i = 0; i < A.size(); i++)
        cout << A[i] << " ";
    cout << endl;

    RMQ rmq(A);
    // cout << rmq.query(1, 5) << endl;
}
