#include <vector>
#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

int N;
int pairSum[20][20] = {0};
int answer = 40000; // max value

bool startTeamMember[20] = {true};

int getLinkTeamScore() {
    vector<int> linkTeam;
    int sum = 0;
    for (int i = 0; i < N; ++i) {
        if (startTeamMember[i]) continue;

        for (auto prevMember : linkTeam)
            sum += pairSum[prevMember][i];
        linkTeam.push_back(i);
    }

    return sum;
}

int dfs(int start, int remained, int startTeamScore, vector<int>& startTeam) {
    if (remained == 0) {
        int linkTeamScore = getLinkTeamScore();
        answer = min(answer, abs(linkTeamScore - startTeamScore));
        return answer;
    }

    for (int i = start + 1; i <= N - remained; ++i) {
        int addedSum = 0;
        for (auto v : startTeam)
            addedSum += pairSum[v][i];

        startTeam.push_back(i);
        startTeamMember[i] = true;

        int ret = dfs(i, remained - 1, startTeamScore + addedSum, startTeam);
        if (ret == 0) return 0;

        startTeam.pop_back();
        startTeamMember[i] = false;
    }

    return answer;
}

int main() {
    scanf("%d", &N);

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            int ability;
            scanf("%d", &ability);
            pairSum[min(i, j)][max(i, j)] += ability; 
        }
    }

    vector<int> startTeam(1, 0);
    dfs(0, N/2 - 1, 0, startTeam);
    printf("%d", answer);

    return 0;
}