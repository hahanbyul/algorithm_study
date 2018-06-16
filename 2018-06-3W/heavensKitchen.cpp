#include <vector>
#include <cstdio>
#include <algorithm>
using namespace std;

int N;

struct Team {
    vector<int> maxVal;
    vector<int> startIdx, endIdx;

    Team() {
        maxVal.reserve(N);
        startIdx.reserve(N);
    }

    void update(int current, int sign, const vector<int>& values) {
        int nextMax = maxVal[current + 1];
        int curMax = 0;

        int sum = sign * values[current];
        curMax = max(curMax, sum);

        bool updated;
        for (int i = current + 1; i < startIdx[current + 1]; ++i) {
            updated = false;
            sum += sign * values[i];
            
            if (curMax <= sum) {
                curMax = sum;
                updated = true;
            }
        }

        if (updated) {
            maxVal[current]   = max(curMax, curMax + nextMax);
            startIdx[current] = current;
        }
        else {
            if (nextMax > curMax) {
                maxVal[current]   = nextMax;
                startIdx[current] = startIdx[current + 1];
            }
            else {
                maxVal[current]   = curMax;
                startIdx[current] = current;
            }
        }

        printf("%d: %d (%d)\n", current, maxVal[current], startIdx[current]);
    }
};

int main() {
    freopen("input.hk", "r", stdin);

    scanf("%d", &N);
    vector<int> values(N), valuesReverse(N);

    for (int n = 0; n < N; ++n) {
        scanf("%d", &values[n]);
        valuesReverse[N-1-n] = values[n];
    }

    Team team1;
    int sign = -1;

    team1.maxVal[N-1] = sign * valuesReverse[N-1];
    team1.startIdx[N-1] = N-1;

    for (int i = N-2; i >= 1; --i) {
        team1.update(i, sign, valuesReverse);
    }

    /*
    Team team2;
    int sign = +1;

    team2.maxVal[N-1] = sign * values[N-1];
    team2.startIdx[N-1] = N-1;

    for (int i = N-2; i >= 1; --i) {
        team2.update(i, sign, values);
    }
    */

    return 0;
}
