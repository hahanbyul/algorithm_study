#include <cstdio>
#include <algorithm>
using std::max;
using std::min;

int N, D;
int stone[100000];          // 동적할당 하는 것과 비교
long long cache[100000];

int main() {
    scanf("%d", &N);
    scanf("%d", &D);

    for (int i = 0; i < N; ++i) {
        scanf("%d", &stone[i]);
    }

    long long globalMax = stone[N-1];
    int globalMaxIndex  = N-1;
    cache[N-1] = stone[N-1];
    for (int start = N - 2; start >= 0; --start) {
        long long localMax = (globalMax > 0 && globalMaxIndex - start <= D)? globalMax : 0;
        if (localMax == 0 && globalMax > 0) {
            for (int i = start + 1; i <= min(start + D, N-1); ++i) {
                localMax = max(localMax, cache[i]);
            }
        }
        cache[start] = stone[start] + localMax;

        if (globalMax < cache[start]) {
            globalMax = cache[start];
            globalMaxIndex = start;
        }
    }

    printf("%lld\n", globalMax);
}