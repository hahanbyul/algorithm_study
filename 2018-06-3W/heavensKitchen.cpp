#include <vector>
#include <cstdio>
#include <algorithm>
using namespace std;

int N;

const int POSITIVE = 0;
const int NEGATIVE = 1;

struct Team {
    vector<int> maxVal;
    vector<int> startIdx, endIdx;

    Team() {
        maxVal.reserve(N);
        startIdx.reserve(N);
    }

    void update(int current, int sign, const vector<int>& values) {
        int curMax = 0;

        int sum = sign * values[current];
        curMax = max(curMax, sum);

        for (int i = current + 1; i < startIdx[current + 1]; ++i) {
            sum += sign * values[i];
            
            if (curMax <= sum) {
                curMax = sum;
            }
        }

        int nextMax = maxVal[current + 1];
        if (nextMax > curMax && sum < 0) {
            maxVal[current]   = nextMax;
            startIdx[current] = startIdx[current + 1];
        }
        else {
            maxVal[current]   = max(curMax, sum + nextMax);
            startIdx[current] = current;
        }

        // printf("%d: %d (%d)\n", current, maxVal[current], startIdx[current]);
    }
};

int main() {
    // freopen("input.hk", "r", stdin);

    scanf("%d", &N);
    vector<int> values(N), valuesReverse(N);

    for (int n = 0; n < N; ++n) {
        scanf("%d", &values[n]);
        valuesReverse[N-1-n] = values[n];
    }

    Team team1[2];
    team1[POSITIVE].maxVal[N-1]   = valuesReverse[N-1];
    team1[POSITIVE].startIdx[N-1] = N-1;

    team1[NEGATIVE].maxVal[N-1]   = -valuesReverse[N-1];
    team1[NEGATIVE].startIdx[N-1] = N-1;

    // printf("team1, POSITIVE\n");
    for (int i = N-2; i >= 1; --i) {
        team1[POSITIVE].update(i, +1, valuesReverse);
    }

    // printf("team1, NEGATIVE\n");
    for (int i = N-2; i >= 1; --i) {
        team1[NEGATIVE].update(i, -1, valuesReverse);
    }

    Team team2[2];
    team2[POSITIVE].maxVal[N-1]   = values[N-1];
    team2[POSITIVE].startIdx[N-1] = N-1;

    team2[NEGATIVE].maxVal[N-1]   = -values[N-1];
    team2[NEGATIVE].startIdx[N-1] = N-1;

    // printf("team2, POSITIVE\n");
    for (int i = N-2; i >= 1; --i) {
        team2[POSITIVE].update(i, +1, values);
    }
    // printf("team2, NEGATIVE\n");
    for (int i = N-2; i >= 1; --i) {
        team2[NEGATIVE].update(i, -1, values);
    }

    reverse(team1[POSITIVE].maxVal.begin(), team1[POSITIVE].maxVal.end());
    reverse(team1[NEGATIVE].maxVal.begin(), team1[NEGATIVE].maxVal.end());

    long long answer = -1000000;
    for (int i = 0; i <= N-2; ++i) {
        long long ret;
        ret = team1[POSITIVE].maxVal[i];
        ret *= team2[POSITIVE].maxVal[i+1];
        answer = max(answer, ret);

        ret = team1[NEGATIVE].maxVal[i];
        ret *= team2[NEGATIVE].maxVal[i+1];
        answer = max(answer, ret);
    }

    printf("%lld\n", answer);

    return 0;
}
