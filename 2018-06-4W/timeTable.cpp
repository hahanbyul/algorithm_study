#include <cstdio>
#include <vector>
using namespace std;

int main() {
    int N;
    scanf("%d", &N);

    vector<unsigned long long> classes(N, 0);
    
    for (int n = 0; n < N; ++n) {
        int k;
        scanf("%d", &k);

        for (int i = 0; i < k; ++i) {
            unsigned long long t;
            scanf("%llu", &t);
            classes[n] |= 1ULL << (t-1);
        }
    }

    int M;
    scanf("%d", &M);

    for (int m = 0; m < M; ++m) {
        int p;
        scanf("%d", &p);

        unsigned long long student = 0;
        for (int i = 0; i < p; ++i) {
            unsigned long long q;
            scanf("%llu", &q);

            student |= 1ULL << (q-1);
        }

        int classCount = 0;
        for (int n = 0; n < N; ++n) {
            if (classes[n] == (student & classes[n])) {
                ++classCount;
            }
        }

        printf("%d\n", classCount);

    }

    return 0;
}
