#include <vector>
#include <climits>
#include <iostream>
#include <cmath>

using namespace std;

vector<int> bricks;

struct Score {
    int diff;
    int myScore;
    int yourScore;

    Score(int _myScore, int _yourScore) : diff(-abs(_myScore - _yourScore)), 
                                          myScore(_myScore), 
                                          yourScore(_yourScore) {}

    bool operator< (const Score& _score) const {
        if (diff == _score.diff) return myScore < _score.myScore;
        return diff < _score.diff;
    }

    Score& operator+ (const Score& _score) {
        diff      += _score.diff;
        myScore   += _score.myScore;
        yourScore += _score.yourScore;
        return *this;
    }
};

int sum(int start, int num) {
    int ret = 0;
    for (int i = 0; i < num; ++i) {
        ret += bricks[start + i];
    }
    return ret;
}

Score getScore(int start, int myRange, int yourRange) {
    int myScore   = sum(start, myRange);
    int yourScore = sum(start + myRange, yourRange);
    return Score(myScore, yourScore);
}

Score solve(int start) {
    cout << "START: " << start << endl;
    if (start >= bricks.size())   return Score(0, 0);
    if (start >= bricks.size()-3) return Score(sum(start, bricks.size() - start), 0);

    int maxRange = min((int)bricks.size() - start, 6);
    cout << "MAX_RNG: " << maxRange << endl;

    Score ret = Score(-1e9, 0);
    for (int range = 2; range <= maxRange; ++range) {
        cout << "RANGE: " << range << endl;
        int myRange   = min(range-1, 3);
        int yourRange = range - myRange;

        auto score = getScore(start, myRange, yourRange);
        cout << "SCORE: " << score.myScore << endl;
        ret = max(ret, score + solve(start + range));
        cout << "ret: diff -> " << ret.diff << " score -> " << ret.myScore << " yours -> " << ret.yourScore << endl;
    }
    return ret;
}

int main() {
    int T;
    scanf("%d", &T);

    for (int t = 0; t < T; ++t) {
        int N;
        scanf("%d", &N);

        bricks = vector<int>(N);
        for (int n = 0; n < N; ++n) {
            scanf("%d", &bricks[n]);
        }
        auto answer = solve(0);
        printf("%d\n", answer.myScore);
        printf("%d\n", answer.yourScore);
    }
}