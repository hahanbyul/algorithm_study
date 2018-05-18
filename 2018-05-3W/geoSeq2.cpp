#include <cstdio>
#include <iostream>
using namespace std;

int a, r, n, mod;
unsigned long long cache[36];

int toIndex(int x) {
    int index = 0;
    int start = n;

    while (start > x) {
        if (start % 2 == 0) {
            start /= 2;
        }
        else {
            start -= 1;
        }
        ++index;
    }
    return index;
}

unsigned long long powerOfr(int p=n, int index=0, int bias=-1) {
    printf("%d %d %d\n", p, index, bias);
    if (p == 2) {
        int answer = bias == -1? r + 1 : r*r + 1;
        printf("%d\n", answer);
        return answer;
    }
    if (cache[index] != 0) {
        unsigned long long answer =  bias == -1? cache[index] : cache[index] * (r - 1) + 2;
        printf("%lld\n", answer);
        return answer;
    }
    if (p % 2 == 0) {
        cache[index] = powerOfr(p/2, index + 1, -1) * powerOfr(p/2, index + 1, +1);
        printf("%lld\n", cache[index]);
        return cache[index];
    }
    else {
        cache[index] = r * powerOfr(p - 1, index + 1, -1) + 1;
        printf("%lld\n", cache[index]);
        return cache[index];
    }
}

int main() {
    n = 17, r = 4;
    int args;
    // while (1) {
    //     scanf("%d", &args);
    //     printf("%d\n", toIndex(args));
    // }
    printf("%lld\n", powerOfr());
}