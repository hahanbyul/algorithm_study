// problem: https://www.acmicpc.net/problem/1786 
// test result: https://cl.ly/3A2Q2t043542

#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    string T, P;
    getline(cin, T);
    getline(cin, P);

    int m = P.size();
    vector<int> pi(m, 0);
    int begin = 1, matched = 0;
    while (begin + matched < m) {
        if (P[begin + matched] == P[matched]) {
            ++matched;
            pi[begin + matched -1] = matched;
        }
        else {
            if (matched == 0) ++begin;
            else {
                begin += matched - pi[matched - 1];
                matched = pi[matched - 1];
            }
        }
    }

    int n = T.size();
    begin = 0, matched = 0;
    vector<int> position;
    while (begin + m - 1 < n) {
        if (matched < m && T[begin + matched] == P[matched]) {
            ++matched;
            if (matched == m) position.push_back(begin);
        }
        else {
            if (matched == 0) ++begin;
            else {
                begin += matched - pi[matched - 1];
                matched = pi[matched - 1];
            }
        }
    }

    printf("%lu\n", position.size());
    for (auto p : position) printf("%d ", p + 1);
    printf("\n");
}