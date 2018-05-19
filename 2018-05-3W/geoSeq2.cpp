#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

unsigned long long a, r, n, mod;
unsigned long long cache[100];

unsigned long long powerOfr(unsigned long long p=n, int index=0, int bias=-1) {
    printf("%lld, %d, %d\n", p, bias, index);
    if (p == 2) {
        unsigned long long answer = bias == -1? r + 1 : (r*r) % mod + 1;
        cout << answer % mod << endl;
        return answer % mod;
    }
    if (cache[index] != 0) {
        unsigned long long answer = (bias == -1)? cache[index] : (cache[index] * (r - 1) + 2) % mod;
        cout << "cached!: " << cache[index] << " " << answer % mod << endl;
        return answer % mod;
    }
    if (p % 2 == 0) {
        cache[index] = (powerOfr(p/2, index + 1, -1) * powerOfr(p/2, index + 1, +1)) % mod;
        cout << cache[index] << endl;
        return cache[index];
    }
    else {
        cache[index] = ((r * powerOfr(p - 1, index + 1, -1)) % mod + 1) % mod;
        cout << cache[index] << endl;
        return cache[index];
    }
}

unsigned long long solve() {
    return n == 1? a : (a*powerOfr()) % mod;
}

unsigned long long solveBrute() {
    int term = a % mod;
    unsigned long long geoSum = term;

    for (int i = 1; i < n; ++i) {
        term *= r;
        term %= mod;

        geoSum += term;
        geoSum %= mod;
    }

    return geoSum;
}

int main() {
    // scanf("%lld %lld %lld %lld", &a, &r, &n, &mod);
    // srand(time(NULL));
    // a = rand() % 100;
    // r = rand() % 100;
    // n = rand() % 100;
    // mod = rand() % 100;
    a = 48, r = 28, n = 90, mod = 14;
    printf("%lld %lld %lld %lld\n", a, r, n, mod);

    a %= mod, r %= mod;
    printf("%lld %lld\n", solve(), solveBrute());
}