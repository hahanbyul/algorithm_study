#define MAX_LENGTH 100

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

char text[MAX_LENGTH + 1], pattern[MAX_LENGTH + 1];
int patternLength, textLength;

// precondition: begin <= patternLength
int getNextWildcardCharIdx (int begin) {
    int end = begin;
    while (end < patternLength && (pattern[end] != '*' && pattern[end] != '?')) { ++end; }
    return end;
}

int getPatternMatchedLength (int patternBegin, int textBegin, int length) {
    for (int i = 0; i < length; ++i) {
        if (patternBegin + i > patternLength || textBegin + i > textLength) {
            return i - 1;
        }
        if (pattern[patternBegin + i] != text[textBegin + i]) {
            return i;
        }
    }
    return length;
}

bool find(int patternIdx, int textIdx) {
    const char patternChar = pattern[patternIdx];
    const char textChar    = text[textIdx];
    // printf("p: %c t: %c\n", patternChar, textChar);

    if      (patternChar == 0)   { return text[textIdx] == 0; }
    else if (patternChar == '?') { return find(patternIdx + 1, textIdx + 1); }
    else if (patternChar == '*') {
        int beginIdx = patternIdx;
        while (beginIdx <= patternLength && (pattern[beginIdx] == '*' || pattern[beginIdx] == '?')) { ++beginIdx; }
        // cout << "beginIdx: " << beginIdx << " " << pattern[beginIdx] << endl;
        int endIdx = getNextWildcardCharIdx(beginIdx);
        if (endIdx == patternLength) { return find(beginIdx, textLength - (patternLength - beginIdx)); }

        while (textIdx < textLength) {
            while (text[textIdx] != 0 && text[textIdx] != pattern[beginIdx]) { ++textIdx; }

            bool result = find(beginIdx, textIdx);
            if (result) return true;
            ++textIdx;
        }
        return false;
    }
    else {
        int nextWildCardIdx = getNextWildcardCharIdx(patternIdx);
        int length = nextWildCardIdx - patternIdx;
        int matchedLength = getPatternMatchedLength(patternIdx, textIdx, length);
        return matchedLength == length ? find(patternIdx + length, textIdx + length) : false;
    }
}

int main() {
    // test
    /*
    scanf("%s", &pattern);
    patternLength = strlen(pattern);

    while (true) {
        scanf("%s", &text);
        textLength = strlen(text);
        cout << find(0, 0) << endl;
    }
    */

    int T;
    scanf("%d", &T);

    while (--T >= 0) {
        scanf("%s", &pattern);
        patternLength = strlen(pattern);
        
        int N;
        scanf("%d", &N);

        vector<string> matched;
        for (int n = 0; n < N; ++n) {
            scanf("%s", &text);
            textLength = strlen(text);
            bool result = find(0, 0);
            if (result) matched.push_back(string(text));
        }

        sort(matched.begin(), matched.end());

        for (int i = 0; i < matched.size(); ++i) {
            printf("%s\n", matched[i].c_str());
        }

    }

    return 0;
}
