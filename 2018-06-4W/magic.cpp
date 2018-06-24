#include <cstdio>

int main(void) {
    freopen("magic_input.txt", "r", stdin);

	int test_case;
	int T;

    scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case) {
        long long N, K;
        scanf("%lld %lld", &N, &K);
        K += 1;

        long long answer = 1;
        for (int n = 2; n <= N; ++n) {
            answer += K;
            if (answer > n) {
                answer %= n;
            }
            if (answer == 0) {
                answer += n;
            }
        }

        printf("#%d %lld\n", test_case, answer);
	}

	return 0; //정상종료시 반드시 0을 리턴해야 합니다.
}
