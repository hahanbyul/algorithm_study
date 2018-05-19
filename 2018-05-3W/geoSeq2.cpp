/* link: https://www.acmicpc.net/problem/15712 */
#include <cstdio>

unsigned long long a, r, n, mod;
unsigned long long cache[100];

unsigned long long powerOfr(unsigned long long p=n, int index=0, int bias=-1) {
    if (p == 2) {
        unsigned long long answer = bias == -1? r + 1 : (r*r) % mod + 1;
        return answer % mod;
    }
    if (cache[index] != 0) {
        unsigned long long answer = (bias == -1)? cache[index] : ((cache[index] * (r - 1)) % mod + 2);
        return answer % mod;
    }
    if (p % 2 == 0) {
        cache[index] = (powerOfr(p/2, index + 1, -1) * powerOfr(p/2, index + 1, +1)) % mod;
        return cache[index];
    }
    else {
        cache[index] = ((r * powerOfr(p - 1, index + 1, -1)) % mod + 1) % mod;
        return cache[index];
    }
}

unsigned long long solve() {
    return (n == 1 || r % mod == 0 || a % mod == 0)? a % mod : ((a % mod) * powerOfr()) % mod;
}

int main() {
    scanf("%lld %lld %lld %lld", &a, &r, &n, &mod);
    printf("%lld\n", solve());
}