#include <cstdio>
#include <vector>
using namespace std;

void printBits(size_t const size, void const * const ptr)
{
    unsigned char *b = (unsigned char*) ptr;
    unsigned char byte;
    int i, j;

    for (i=size-1;i>=0;i--)
    {
        for (j=7;j>=0;j--)
        {
            byte = (b[i] >> j) & 1;
            printf("%u", byte);
        }
    }
    puts("");
}

int main() {
    freopen("timeTable-input.txt", "r", stdin);

    int N;
    scanf("%d", &N);

    vector<unsigned long long> classes(N, 0);
    
    for (int n = 0; n < N; ++n) {
        int k;
        scanf("%d", &k);

        for (int i = 0; i < k; ++i) {
            unsigned long long t;
            scanf("%llu", &t);
            printf("%llu ", t);
            classes[n] |= 1ULL << (t-1);
        }
        printBits(sizeof(classes[n]), &classes[n]);
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

        printf("student: ");
        printBits(sizeof(student), &student);

        int classCount = 0;
        for (int n = 0; n < N; ++n) {
            printf("  class: ");
            printBits(sizeof(classes[n]), &classes[n]);

            if (classes[n] == (student & classes[n])) {
                ++classCount;
            }
        }

        printf("%d\n", classCount);

    }

    return 0;
}
