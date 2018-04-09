#include <vector>
#include <algorithm>
#include <string>
#include <iostream>

using namespace std;

const bool CONTRADICT = true;
const int  MAX_DIGITS = 10;

int main() {
    int testCase;
    scanf("%d", &testCase);

    for (int c = 0; c < testCase; ++c) {
        int numOfItems;
        scanf("%d", &numOfItems);

        vector<string> phoneBook(numOfItems);
        for (int i = 0; i < numOfItems; ++i) {
            char number[MAX_DIGITS+1];
            scanf("%s", number);

            string numberStr(number);
            phoneBook[i] = numberStr;
        }

        sort(phoneBook.begin(), phoneBook.end());

        bool result;
        for (int i = 0; i < phoneBook.size()-1; ++i) {
            string curNumber(phoneBook[i]);
            string nextNumber(phoneBook[i+1]);

            result = (nextNumber.compare(0, min(curNumber.size(), nextNumber.size()), curNumber) == 0);
            if (result == CONTRADICT) {
                printf("NO\n");
                break;
            }
        }
        if (result == !CONTRADICT) printf("YES\n");
    }
}