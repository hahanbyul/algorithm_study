#include <cstdio>
#include <algorithm>
using std::max;
using std::min;

int N, D;
int stone[100000];
long long cache[100000];

int main() {
    scanf("%d", &N);
    scanf("%d", &D);

    for (int i = 0; i < N; ++i) {
        scanf("%d", &stone[i]);
    }

    cache[N-1] = stone[N-1];

    long long globalMax = stone[N-1];
    int globalMaxIndex  = N-1;

    long long localMax = globalMax;
    int localMaxIndex  = globalMaxIndex;

    for (int start = N - 2; start >= 0; --start) {
        if (localMaxIndex - start > D) {
            localMax = cache[start + 1];
            localMaxIndex = start + 1;
            for (int i = start + 2; i <= min(start + D, N-1); ++i) {
                if (localMax < cache[i]) {
                    localMax = cache[i];
                    localMaxIndex = i;
                }
            }
        }

        cache[start] = (long long) stone[start] + max((long long)0, localMax);
        if (localMax <= cache[start]) {
            localMax = cache[start];
            localMaxIndex = start;
        }

        if (globalMax < cache[start]) {
            globalMax = cache[start];
            globalMaxIndex = start;
        }
    }

    printf("%lld\n", globalMax);
}