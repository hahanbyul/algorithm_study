#include <cstdio>
#include <vector>
using std::vector;

bool hasDuplicate(int num, vector<bool>& usedDigits) {
    while (num > 0) {
        int rem = num % 10;
        if (usedDigits[rem]) {
            return true;
        } else {
            usedDigits[rem] = true;
        }
        num /= 10;
    }

    return false;
}

int main() {
    int N;
    scanf("%d", &N);

    int MAX_A = N/2 < 100000 ? N/2 : 100000;
    for (int A = 1; A < MAX_A; ++A) {
        vector<bool> usedDigits(10, false);

        if (hasDuplicate(A, usedDigits)) {
            continue;
        }

        int B = N - A;
        if (!hasDuplicate(B, usedDigits)) {
            printf("%d + %d\n", A, B);
            return 1;
        }
    }

    printf("-1\n");
    return 0;
}
