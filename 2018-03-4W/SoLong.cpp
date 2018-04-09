// https://algospot.com/judge/problem/read/SOLONG

#include <cstring>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

const int R = 26;
const int MAX_CHAR_LENGTH = 10;
const int NOT_AVAILABLE = -1;
int toNumber(char ch)   { return ch - 'A'; }
string toString(char ch) { 
    string s(1, ch + 'A');
    return s; 
}

const int SEARCH_MISS = 0;

struct Key {
    string word;
    int    freq;

    Key(string _word, int _freq): word(_word), freq(_freq) {}

    bool operator<(const Key& that) const {
        if (freq == that.freq) return strcmp(word.c_str(), that.word.c_str()) > 0;
        return freq < that.freq;
    }
};

class TrieNode {
    vector<TrieNode*> children;
    int terminal;
    int first;

public:
    TrieNode() : terminal(NOT_AVAILABLE), children(R, 0), first(NOT_AVAILABLE) {}

    void insert(const char* key, int id) {
        if (first == NOT_AVAILABLE) first = id;
        if (*key == 0) terminal = id;
        else {
            int next = toNumber(*key);
            if (children[next] == 0)  { children[next] = new TrieNode(); }
            children[next]->insert(key + 1, id);
        }
    }

    int find(const char* key) {
        // search hit or miss condition (when node exists)
        if (*key == 0) return terminal;

        // search miss condition
        int next = toNumber(*key);
        if (children[next] == 0) return NOT_AVAILABLE;

        return children[next]->find(key + 1);
    }

    int solve(vector<string> v) {

        int spacesNum = v.size()-1;
        int answer = spacesNum;

        for (vector<string>::const_iterator word = v.begin(); word != v.end(); ++word) {

            const char* wordPtr = (*word).c_str();
            int id = find(wordPtr);

            if (id == NOT_AVAILABLE) {
                answer += (*word).size();
                continue;
            }

            int ret = 1 + children[toNumber(*wordPtr)]->countStrokes(wordPtr, id); 
            answer += ret;
        }

        return answer;
    }

    int countStrokes(const char* wordPtr, int id) {

        char nextChar = *(wordPtr + 1);
        /* termination conditions */
        if (nextChar == 0) return 0;
        TrieNode* nextNode = children[toNumber(nextChar)];
        if (nextNode == 0) return strlen(wordPtr + 1);
        if (first == id)   return 1;    // tab is pressed

        return 1 + nextNode->countStrokes(wordPtr + 1, id);
    }

};

int main() {
    int C;
    scanf("%d", &C);

    for (int c = 0; c < C; ++c) {
        TrieNode tn;

        int N, M;
        scanf("%d %d", &N, &M);

        vector<Key> words;
        for (int n = 0; n < N; ++n) {
            char s[MAX_CHAR_LENGTH + 1];
            int freq;
            scanf("%s %d", s, &freq);

            Key key(s, freq);
            words.push_back(key);
        }
        

        sort(words.begin(), words.end());


        int id = 0;
        for (vector<Key>::reverse_iterator it = words.rbegin(); it != words.rend(); ++it) {
            tn.insert(it->word.c_str(), id++);
        }


        vector<string> line;
        for (int m = 0; m < M; ++m) {
            char ch[MAX_CHAR_LENGTH + 1];
            scanf("%s", ch);

            string s(ch);
            line.push_back(s);
        }

        printf("%d\n", tn.solve(line));
    }
}
