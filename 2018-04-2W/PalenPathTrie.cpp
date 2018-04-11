#include <iostream>
#include <vector>
#include <string>
using namespace std;

const int R = 26;
const int SEARCH_MISS = 0;

int toNumber(char ch) { return ch - 'a'; }

struct TrieNode {
    int count;
    vector<TrieNode*> children;

    TrieNode() : count(0), children(R, 0) {}
    void insert(const char* path) {
        TrieNode*& currentNode = children[toNumber(*path)];
        if (currentNode == 0) currentNode = new TrieNode();

        if (*(path+1) == 0) {
            ++(currentNode->count);
            return;
        }

        currentNode->insert(++path);
    }

    int find(const char* path) {
        TrieNode* currentNode = children[toNumber(*path)];
        if (currentNode == 0) { return SEARCH_MISS;        }
        if (*(path+1) == 0)   { return currentNode->count; }

        return currentNode->find(++path);
    }
};

int main() {
    TrieNode root;

    string s = "abcd";
    root.insert(s.c_str());
    cout << root.find(s.c_str()) << endl;
    root.insert(s.c_str());
    cout << root.find(s.c_str()) << endl;

    string s2 = "abc";
    cout << root.find(s2.c_str()) << endl;
    return 0;
}