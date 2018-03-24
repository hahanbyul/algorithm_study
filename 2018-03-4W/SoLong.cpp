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

    bool operator<(const Key& that) const {
        if (freq == that.freq) return strcmp(word.c_str(), that.word.c_str()) > 0;
        return freq < that.freq;
    }
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
        TrieNode* prefixNode = find(prefix);
        return keysWithPrefix(prefixNode, prefix);
    }

    vector<Key> keysWithPrefix(TrieNode* prefixNode, const char* prefix) {
        vector<Key> keys;
        if (prefixNode == nullptr) return keys;

        string prefixStr = string(prefix);
        prefixNode->collect(prefixStr, keys);

        return keys;
    }

    // should not be called if object is null
    void collect(string word, vector<Key>& queue) {
        if (freq != 0) {
            Key key(word, freq);
            queue.push_back(key);
            push_heap(queue.begin(), queue.end());
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

    int solve(vector<string> v) {
        int spacesNum = v.size()-1;
        int answer = spacesNum;

        for (vector<string>::const_iterator word = v.begin(); word != v.end(); ++word)
            answer += solveForWord(*word);

        return answer;
    }

    int solveForWord(string word) {
        // cout << "word: " << word << endl;
        int stroke = 1;
        string prefix(1, word[0]);

        TrieNode* prefixNode = find(prefix.c_str());
        while (stroke <= word.size()) {
            // cout << "prefix: " << prefix << endl;
            vector<Key> keys = keysWithPrefix(prefixNode, prefix.c_str());
            if (keys.size() == 0) // not in dictionary
                return word.size(); 

            Key maxKey = keys.front();
            // cout << "max key: " << maxKey.word << endl;
            if (maxKey.word == word) {
                if (prefix != word) ++stroke; // tab
                break;
            }

            char nextChar = word[stroke];
            prefix += nextChar;
            prefixNode = prefixNode->children[toNumber(nextChar)];
            ++stroke;
        }

        // cout << word << "(" << stroke << ")" << endl;
        return stroke;
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

        vector<string> line;
        for (int m = 0; m < M; ++m) {
            char ch[10];
            scanf("%s", ch);

            string s(ch);
            line.push_back(s);
        }

        printf("%d\n", tn.solve(line));
    }
}
