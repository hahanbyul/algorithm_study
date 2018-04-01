#include <vector>
#include <climits>
#include <iostream>
#include <cmath>

using namespace std;

struct Score {
    int myScore;
    int yourScore;

    Score(int _myScore, int _yourScore) : myScore(_myScore), 
                                          yourScore(_yourScore) {}

    bool operator< (const Score& _score) const {
        return myScore < _score.myScore;
    }

    Score& operator+ (const Score& _score) {
        myScore   += _score.myScore;
        yourScore += _score.yourScore;
        return *this;
    }

    bool operator== (const Score& _score) {
        return myScore == _score.myScore && yourScore == _score.yourScore;
    }

    bool operator!= (const Score& _score) {
        return !operator==(_score);
    }
};

vector<int> bricks;
vector<Score> cache;
const Score DEFAULT(-1, -1);

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
    // if (start >= bricks.size()-3) return Score(sum(start, bricks.size() - start), 0);
    if (cache[start] != DEFAULT) {
        cout << "CACHED: " << "(" << cache[start].myScore << ", " << cache[start].yourScore << ")" << endl;
        return cache[start];
    }


    Score ret = Score(-1e9, 0);
    for (int i = 1; i <= 3; ++i) {
        for (int j = 1; j <= 3; ++j) {
            if (start + i + j > bricks.size()) break;
            cout << "\nSTART: " << start;
            cout << ", i: " << i << ", j: " << j << endl;
            auto score = getScore(start, i, j);
            cout << "SCORE: " << score.myScore << endl;
            auto optimalScore        = solve(start + i + j);
            auto anotherOptimalScore = solve(start + i);

            cout << "Score (start + i + j) -> yourScore: " << score.yourScore + optimalScore.yourScore << endl;
            cout << "Score (start + i)     -> myScore:   " << anotherOptimalScore.myScore << endl;

            if (score.yourScore + optimalScore.yourScore == anotherOptimalScore.myScore) {
                ret = max(ret, score + optimalScore);
                cout << "updated!! ret: (" << ret.myScore << ", " << ret.yourScore << ")" << endl;
            }
        }
    }

    cache[start] = ret;
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
            cache.push_back(Score(-1, -1));
        }

        for (int i = 1; i <= 3; ++i) {
            int start = bricks.size() - i;
            cache[start] = Score(sum(start, i), 0);
        }
        auto answer = solve(0);
        printf("%d\n", answer.myScore);
        printf("%d\n", answer.yourScore);
    }
}