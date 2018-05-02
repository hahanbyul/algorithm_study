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

    for (int A = 1; A < N; ++A) {
        vector<bool> usedDigits(10, false);

        if (hasDuplicate(A, usedDigits))
            continue;

        int B = N - A;
        if (A >= B) {
            printf("-1\n");
            break;
        }

        if (!hasDuplicate(B, usedDigits)) {
            printf("%d + %d\n", A, B);
            break;
        }
    }

    return 0;
}
