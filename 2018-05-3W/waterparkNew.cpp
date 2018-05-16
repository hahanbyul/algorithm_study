#include <cstdio>
#include <algorithm>
using std::max;
using std::min;

int N, D;
// int stone[100000];  // 동적할당 하는 것과 비교
long long cache[100000];

void print(int* array) {
    for (int i = 0; i < N; ++i) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

void print(long long *array) {
    for (int i = 0; i < N; ++i) {
        printf("%lld ", array[i]);
    }
    printf("\n");
}

struct Score {
    long long value;
    int index;
    int count;

    Score(long long _value, int _index, int _count=1) : value(_value), index(_index), count(_count) {}
    Score(const Score& s) { value = s.value, index = s.index; }
    bool operator<= (Score& s) { return value <= s.value; }
    long long getPosVal() { return value > 0 ? value : 0; }
};

int main() {
    /*
    N = 10;
    D = 2;
    int stone[] = {2, 7, -5, -4, 10, -5, -5, -5, 30, -10};
    */

    N = 3;
    D = 2;
    int stone[] = {-4, -2, -7};

    print((int*) stone);

    // Score globalMaxSum(stone[N-1], N-1);
    cache[N-1] = stone[N-1];
    for (int start = N - 2; start >= 0; --start) {
        long long localMax = 0;
        for (int i = start + 1; i <= min(start + D, N-1); ++i) {
            localMax = max(localMax, cache[i]);
        }
        cache[start] = stone[start] + localMax;
    }

    long long maxSum = -1000000000;
    for (int i = 0; i < N-1; ++i) {
        maxSum = max(maxSum, cache[i]);
    }

    print(cache);

    printf("%d\n", maxSum);
}