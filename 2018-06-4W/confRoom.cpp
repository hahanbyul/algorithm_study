#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

struct Meeting {
    int tBegin, tEnd;
    Meeting(int _tStart, int _tEnd) : tBegin(_tStart), tEnd(_tEnd) {}
};

bool operator< (const Meeting& one, const Meeting& theOther) {
    if (one.tEnd == theOther.tEnd) {
        return one.tBegin < theOther.tBegin;
    }
    return one.tEnd < theOther.tEnd;
}

int main() {
    int N;
    scanf("%d", &N);
    vector<Meeting> meetings;
    meetings.reserve(N);

    for (int n = 0; n < N; ++n) {
        int tBegin, tEnd;
        scanf("%d %d", &tBegin, &tEnd);

        meetings.push_back(Meeting(tBegin, tEnd));
    }

    sort(meetings.begin(), meetings.end());

    int count = 0;
    int tEndPrev = 0;
    for (int n = 0; n < N; ++n) {
        if (meetings[n].tBegin >= tEndPrev) {
            ++count;
            tEndPrev = meetings[n].tEnd;
        }
    }

    printf("%d", count);

    return 0;
}
