#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<bool> totalScore;
vector<int>  eachScore;

void combination(int start, int remained, int sum) {
    // printf("start: %d, remained: %d, sum: %d\n", start, remained, sum);
    if (remained == 0) {
        totalScore[sum] = true;
        return;
    }

    for (int i = start; i <= eachScore.size() - remained; ++i)
        combination(i + 1, remained - 1, sum + eachScore[i]);
}

int main() {
    int T;
    scanf("%d", &T);

    int t = 0;
    while (++t <= T) {
        totalScore.clear();
        eachScore.clear();

        int N;
        scanf("%d", &N);

        totalScore = vector<bool>(N*100 + 1, false);
        eachScore  = vector<int>(N);

        for (int n = 0; n < N; ++n)
            scanf("%d", &eachScore[n]);


        sort(eachScore.begin(), eachScore.end());

        totalScore[0] = true;
        for (int r = 1; r <= N; ++r)
            combination(0, r, 0);

        int numOfCases = 0;
        for (int i = 0; i < totalScore.size(); ++i)
            numOfCases += totalScore[i];

        printf("#%d %d\n", t, numOfCases);
    }

    return 0;
}