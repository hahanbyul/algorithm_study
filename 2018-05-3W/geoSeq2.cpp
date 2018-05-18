#include <cstdio>
#include <iostream>
using namespace std;

int a, r, n, mod;
int cache[36];

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

int powerOfr(int p=n, int index=0, int bias=-1) {
    printf("%d %d %d\n", p, index, bias);
    if (p == 2) {
        int answer = bias == -1? r + 1 : r*r + 1;
        printf("%d\n", answer);
        return answer % mod;
    }
    if (cache[index] != 0) {
        int answer =  bias == -1? cache[index] : cache[index] * (r - 1) + 2;
        printf("%d\n", answer);
        return answer % mod;
    }
    if (p % 2 == 0) {
        cache[index] = (powerOfr(p/2, index + 1, -1) * powerOfr(p/2, index + 1, +1)) % mod;
        printf("%d\n", cache[index]);
        return cache[index];
    }
    else {
        cache[index] = (r * powerOfr(p - 1, index + 1, -1) + 1) % mod;
        printf("%d\n", cache[index]);
        return cache[index];
    }
}

int solve() {
    return (a*powerOfr()) % mod;
}

int main() {
    // a = 3, r = 5, n = 2, mod = 10;
    a = 1, r = 2, n = 9, mod = 100;
    printf("%d\n", solve());
}