// https://algospot.com/judge/problem/read/SOLONG

#include <cstring>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

const int R = 26;
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
};

class TrieNode {
    vector<TrieNode*> children;
    int freq;

    public:
    TrieNode() : freq(0), children(R, 0) {}

    void insert(const char* key, int val) {
        if (*key == 0) freq = val;
        else {
            int next = toNumber(*key);
            if (children[next] == 0)  { children[next] = new TrieNode(); }
            children[next]->insert(key + 1, val);
        }
    }

    TrieNode* find(const char* key) {
        // search hit or miss condition (when node exists)
        if (*key == 0) return this;

        // search miss condition
        int next = toNumber(*key);
        if (children[next] == 0) return nullptr;

        return children[next]->find(key + 1);
    }

    vector<Key> keysWithPrefix(const char* prefix) {
        vector<Key> keys;
        TrieNode* prefixNode = find(prefix);
        if (prefixNode == 0) return keys;

        string prefixStr = string(prefix);
        prefixNode->collect(prefixStr, keys);

        return keys;
    }

    // should not be called if object is null
    void collect(string word, vector<Key>& queue) {
        if (freq != 0) {
            Key key(word, freq);
            queue.push_back(key);
        }

        for (char c = 0; c < R; ++c) {
            if (children[c] != 0) {
                children[c]->collect(word + toString(c), queue);
            }
        }
    }

    void printKeys(vector<Key>& keys) {
        for (vector<Key>::const_iterator key = keys.begin(); key != keys.end(); ++key)
            cout << key->word << ": " << key->freq << '\n';
    }

};

int main() {
    int C;
    scanf("%d", &C);

    for (int c = 0; c < C; ++c) {
        TrieNode tn;

        int N, M;
        scanf("%d %d", &N, &M);

        for (int n = 0; n < N; ++n) {
            char s[10];
            int freq;
            scanf("%s %d", s, &freq);
            tn.insert(s, freq);
        }

        vector<char*> line;
        for (int m = 0; m < M; ++m) {
            char s[10];
            scanf("%s", s);
            line.push_back(s);
        }
    }

    /*
    tn.insert("ABCD", 4);
    tn.insert("ABCDE", 3);

    vector<Key> keys = tn.keysWithPrefix("AB");
    tn.printKeys(keys);
    */
}
