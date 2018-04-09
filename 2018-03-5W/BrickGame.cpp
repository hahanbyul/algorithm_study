#include <vector>
#include <climits>
#include <iostream>
#include <cmath>

using namespace std;

struct Score {
    unsigned long long myScore;
    unsigned long long yourScore;

    Score(unsigned long long _myScore, unsigned long long _yourScore) : myScore(_myScore), 
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

vector<unsigned long long> bricks;
vector<Score> cache;
const Score DEFAULT(0, 0);

unsigned long long sum(int start, int num) {
    int ret = 0;
    for (int i = 0; i < num; ++i) {
        ret += bricks[start + i];
    }
    return ret;
}

Score getScore(int start, int myRange, int yourRange) {
    unsigned long long myScore   = sum(start, myRange);
    unsigned long long yourScore = sum(start + myRange, yourRange);
    return Score(myScore, yourScore);
}

Score solve(int start) {
    if (start >= bricks.size())   return Score(0, 0);
    if (cache[start] != DEFAULT)  return cache[start];

    Score ret = DEFAULT;
    for (int i = 1; i <= 3; ++i) {
        for (int j = 1; j <= 3; ++j) {
            if (start + i + j > bricks.size()) break;
            auto optimalScore        = solve(start + i + j);
            auto anotherOptimalScore = solve(start + i);

            auto score = getScore(start, i, j);
            if (score.yourScore + optimalScore.yourScore == anotherOptimalScore.myScore)
                ret = max(ret, score + optimalScore);
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

        bricks.clear();
        bricks = vector<unsigned long long>(N);
        cache.clear();
        for (int n = 0; n < N; ++n) {
            scanf("%llu", &bricks[n]);
            cache.push_back(DEFAULT);
        }

        for (int i = 1; i <= 3; ++i) {
            int start = bricks.size() - i;
            cache[start] = Score(sum(start, i), 0);
        }

        auto answer = solve(0);
        printf("%llu\n", answer.myScore);
    }
}