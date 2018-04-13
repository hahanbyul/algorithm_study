#include <iostream>
using namespace std;

enum Duration { DAY, MONTH, QUATER, YEAR };

int prices[4];
int use[12];
int minPriceForMonth[12];
int cache[12];

const int MAX_VAL = 9000;

int compareToQuaterPlan(int start) {
    if (start >= 12)        return 0;
    if (cache[start] != -1) return cache[start];

    int ret = MAX_VAL;
    int prevPrice = 0;
    for (int i = start; i < min(10, start + 3); ++i) {
        int priceByMonth  = minPriceForMonth[i] + minPriceForMonth[i+1] + minPriceForMonth[i+2];
        int priceBYQuater = prices[QUATER];
        int cand = prevPrice + min(priceByMonth, priceBYQuater) + compareToQuaterPlan(i + 3);
        ret = min(ret, cand);
        prevPrice += minPriceForMonth[i];
    }

    cache[start] = ret;
    return ret;
}

int main() {
    int T;
    scanf("%d", &T);

    int t = 0;
    while (++t <= T) {
        for (int i = 0; i < 4; ++i)
            scanf("%d", &prices[i]);

        for (int i = 0; i < 12; ++i) {
            scanf("%d", &use[i]);
            minPriceForMonth[i] = min(prices[DAY]*use[i], prices[MONTH]);
            // cache initialization
            cache[i] = -1;
        }

        cache[11] = minPriceForMonth[11];
        cache[10] = minPriceForMonth[10] + minPriceForMonth[11];
        int answer = min(prices[YEAR], compareToQuaterPlan(0));
        printf("#%d %d\n", t, answer);
    }
}