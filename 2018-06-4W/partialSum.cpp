#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int N, M;
vector<unsigned long long> S;

const int SUM = 0;
// const int MODIFY = 1;

unsigned long long Sum(int left, int right, int node, int nodeLeft, int nodeRight) {
    if (right < nodeLeft || left > nodeRight)   { return 0;       }
    if (left <= nodeLeft && right >= nodeRight) { return S[node]; }

    int mid = (nodeLeft + nodeRight) / 2;
    unsigned long long leftSum  = Sum(left, right, node * 2, nodeLeft, mid);
    unsigned long long rightSum = Sum(left, right, node * 2 + 1, mid + 1, nodeRight);
    return leftSum + rightSum;
}

unsigned long long Sum(int i, int j) {
    int left  = min(i, j) - 1;
    int right = max(i, j) - 1;

    return Sum(left, right, 1, 0, N-1);
}

unsigned long long Modify(int i, int k, int node, int nodeLeft, int nodeRight) {
    if (i < nodeLeft || i > nodeRight) { return S[node]; };
    if (nodeLeft == nodeRight) {
        S[node] = k;
        return k;
    }

    int mid = (nodeLeft + nodeRight) / 2;
    unsigned long long result = Modify(i, k, node * 2, nodeLeft, mid) + Modify(i, k, node * 2 + 1, mid + 1, nodeRight);
    S[node] = result;
    return result;
}

unsigned long long Modify(int index, int value) {
    return Modify(index - 1, value, 1, 0, N-1);
}

int main() {
    scanf("%d %d", &N, &M);

    S = vector<unsigned long long>(4*N, 0);
    for (int m = 0; m < M; ++m) {
        int function;
        scanf("%d", &function);

        if (function == SUM) {
            int left, right;
            scanf("%d %d", &left, &right);
            unsigned long long result = Sum(left, right);
            printf("%llu\n", result);
        }
        else /* if (function == MODIFY) */ {
            int index, value;
            scanf("%d %d", &index, &value);
            Modify(index, value);
        }
        
    }
}
