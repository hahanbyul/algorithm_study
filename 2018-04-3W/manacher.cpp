// link:   https://www.acmicpc.net/problem/13275
// result: https://cl.ly/1I143d211E2C
#include <cstdio>
#include <cstring>

char text[100000 + 1];

int manacher() {
    int N = strlen(text);
    N = 2*N + 1;
    int L[N];

    int i, iMirror;
    int diff;
    bool expand; 

    int C = 1;
    int R = 2;
    L[0] = 0;
    L[1] = 1;
    int maxLength = 1;

    for (i = 2; i < N; ++i) {
        iMirror = 2*C - i;
        diff = R - i;
        expand = false;

        if (diff > 0) {
            if      (L[iMirror] < diff)              { L[i] = L[iMirror]; }
            else if (L[iMirror] == diff && i == N-1) { L[i] = L[iMirror]; }
            else if (L[iMirror] == diff && i < N-1)  { 
                L[i] = L[iMirror];
                expand = true;
            }
            else if (L[iMirror] > diff) {
                L[i] = diff;
                expand = true;
            }
        } else {
            L[i] = 0;
            expand = true;
        }

        if (expand) {
            while (((i + L[i]) < N && (i - L[i]) > 0) && (((i + L[i] + 1) % 2 == 0) || (text[(i + L[i] + 1)/2] == text[(i - L[i] - 1)/2])))
                ++L[i];
        }

        if (R < i + L[i]) {
            C = i;
            R = i + L[i];
        }

        if (L[i] > maxLength) {
            maxLength = L[i];
        }
    }

    return maxLength;
}

int main() {
    scanf("%s", text);
    printf("%d", manacher());

    return 0;
}
