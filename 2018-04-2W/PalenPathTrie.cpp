#include <iostream>
#include <vector>
#include <string>
using namespace std;

const int R = 26;
const int SEARCH_MISS = 0;

int toNumber(char ch) {
    return ch - 'a';
}

struct TrieNode {
    int count;
    vector<TrieNode*> children;

    TrieNode() : count(0), children(R, 0) {}
    void insert(const char* path) {
        TrieNode*& currentNode = children[toNumber(*path)];
        if (currentNode == 0) currentNode = new TrieNode();
        cout << "ch: " << *path << ", count: " << currentNode->count << endl;

        if (*(path+1) == 0) {
            ++(currentNode->count);
            cout << "count: " << currentNode->count << endl;
            return;
        }

        currentNode->insert(++path);
    }

    int find(const char* path) {
        // cout << "ch: " << *path << endl;
        TrieNode* currentNode = children[toNumber(*path)];
        cout << "ch: " << *path << endl; // << ", count: " << currentNode->count << endl;
        if (currentNode == 0) {
            cout << "MISS" << endl;
            return SEARCH_MISS;
        }
        if (*(path+1) == 0) {
            cout << "FOUND: " << currentNode->count << endl;
            return currentNode->count;
        }

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