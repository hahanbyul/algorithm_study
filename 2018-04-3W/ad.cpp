#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
using std::vector;
using std::min;
using std::cout;

#define endl "\n"

int main() {
    char text[1000000];
    // strcpy(text, "abcabcabc");
    // strcpy(text, "abcdef");
    // int N = strlen(text);

    int N;
    scanf("%d", &N);
    vector<int> pi(N, 0);

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

    for (auto m : pi) cout << m << " ";
    cout << endl;

    int start = N;
    int minJumpLength = N;
    while (--start + minJumpLength >= N && pi[start] > 0) {
        cout << "start: " << start << "\n";
        minJumpLength = min(minJumpLength, N - pi[start]);
        int jump = pi[start] - 1;
        int jumpLength = start - jump;
        if (jumpLength >= minJumpLength) continue;

        int nextJump = pi[jump] - 1;
        while (jump >= jumpLength && jump - nextJump == jumpLength) {
            cout << "jump: " << jump << ", nextJump: " << nextJump << "\n";
            jump = nextJump;
            if (pi[jump] == 0) break;
            nextJump = pi[jump] - 1;
        }

        int lastJump = jump;
        cout << "lastJump: " << lastJump << endl;
        if (lastJump < jumpLength) {
            int idx = N + (lastJump - jumpLength);
            cout << "idx: " << idx << ", text[idx]: " << text[idx] << ", text[lastJump]: " << text[lastJump] << endl;
            if (text[idx] == text[lastJump]) {
                minJumpLength = min(minJumpLength, jumpLength);
                printf("updated: %d\n", minJumpLength);
            }
        }

    }

    printf("%d", minJumpLength);

    return 0;
}