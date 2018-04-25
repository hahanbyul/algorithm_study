// link:   https://www.acmicpc.net/problem/1305 
// result: https://cl.ly/0J16330f3N3D 

#include <cstdio>
#include <vector>
using std::vector;

int main() {
    int N;
    scanf("%d", &N);
    vector<int> pi(N, 0);

    char text[1000000];
    scanf("%s", text);

    int begin = 1;
    int matched = 0;
    while (begin + matched < N) {
        if (text[begin + matched] == text[matched]) {
            ++matched;
            pi[begin + matched - 1] = matched;
        }
        else {
            if (matched == 0) { ++begin; }
            else {
                begin += matched - pi[matched - 1];
                matched = pi[matched - 1];
            }
        }
    }

    int minLength = N - pi[N-1];
    printf("%d\n", minLength);

    return 0;
}