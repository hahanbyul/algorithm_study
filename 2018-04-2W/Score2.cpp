#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool totalScore[10000 + 1];
vector<int>  eachScore;

void solve(int goal, int start, int sum) {
    if (totalScore[goal]) {
        cout << "cached! (" << goal << ")\n";
        return;
    }

    for (int i = start; i < eachScore.size(); ++i) {
        int nextSum = sum + eachScore[i];
        if (nextSum >  goal) continue;
        else {

            totalScore[nextSum] = true;
            cout << "saved: " << nextSum << endl;
            solve(goal, i + 1, nextSum);
            if (totalScore[goal]) return;
        }
    }
}

int main() {
    /*
    int T;
    scanf("%d", &T);

    int t = 0;
    while (++t <= T) {
        */
        eachScore.clear();

        int N;
        scanf("%d", &N);

        eachScore  = vector<int>(N);
        int MAX_SCORE = 0;
        for (int n = 0; n < N; ++n) {
            scanf("%d", &eachScore[n]);
            MAX_SCORE += eachScore[n];
        }

        sort(eachScore.begin(), eachScore.end(), greater<int>());

        totalScore[0] = true;
        totalScore[MAX_SCORE] = true;

        int goal = MAX_SCORE;
        while (--goal > 0) {
            cout << "goal: " << goal << endl;
            solve(goal, 0, 0);
        }

        int numOfCases = 0;
        for (int i = 0; i <= MAX_SCORE; ++i)
            numOfCases += totalScore[i];

        printf("%d\n", numOfCases);
        // printf("#%d %d\n", t, numOfCases);
    // }

    return 0;
}