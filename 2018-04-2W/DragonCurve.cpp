#include <iostream>
#include <string>
using namespace std;

unsigned long int genSize[50 + 1] = {2};

string basicStr    = "FX+YF+FX-YF+FX+YF-FX-YF+FX+YF+FX-YF-FX+YF-FX-YF";
string reversedStr = "FY-XF-FY+XF-FY-XF+FY+XF-FY-XF-FY+XF+FY-XF+FY+XF";

string getDragonCurve(int i, unsigned long int left, unsigned long int right, bool reversed) {
    cout << "i: " << i;
    cout << ", left: " << left;
    cout << ", right: " << right; 
    cout << ", mid: " << genSize[i-1];
    cout << ", reversed " << reversed << endl;
    if (right <= left) return "";

    if (right < genSize[4]) {
        if (!reversed) return string(basicStr.begin() + left, basicStr.begin() + right + 1);
        else {
            int reversedLeft  = genSize[4] - 1 - right;
            int reversedRight = genSize[4] - 1 - left;
            return string(reversedStr.rbegin() + reversedLeft, reversedStr.rbegin() + reversedRight + 1);
        }
    }

    unsigned long int mid = genSize[i-1];
    if (right < mid) return getDragonCurve(i-1, left, right, reversed);
    if (left  > mid) return getDragonCurve(i-1, 2*mid - right, 2*mid - left, !reversed);
    
    string divLeft  = getDragonCurve(i, left, mid-1, reversed);
    string divRight = getDragonCurve(i, mid+1, right, reversed);
    if (!reversed) return divLeft + "+" + divRight;
    else           return divRight + "-" + divLeft;
}

void printDragonCurve(int i, unsigned long int p, int l) {
    printf("%s\n", getDragonCurve(i, p-1, p+l-2, false).c_str());
}

string genDragonCurve(int n) {
    string start = "FX";
    int t = 0;
    while (++t <= n) {
        for (int i = 0; i < start.size(); ++i) {
            if (start[i] == 'X') {
                start.insert(i+1, "+YF");
                i += 3;
            }
            if (start[i] == 'Y') {
                start.insert(i, "FX-");
                i += 3;
            }
        }
    }

    return start;
}

string getDragonCurveSlow(int i, unsigned long int p, int l) {
    string answer = genDragonCurve(i);
    return string(answer.begin() + p - 1, answer.begin() + p + l - 1);
}

int main() {
    for (int i = 1; i <= 50; ++i) genSize[i] = genSize[i-1] * 2 + 1;

    int i;
    scanf("%d", &i);
    cout << "range: 1 ~ " << genSize[i] << endl;

    int p, l;
    scanf("%d %d", &p, &l);

    cout << getDragonCurveSlow(i, p, l) << endl;
    printDragonCurve(i, p, l);

    // printDragonCurve(6, 91, 5);
    /*
    printDragonCurve(0, 1, 2);
    printDragonCurve(1, 1, 5);
    printDragonCurve(2, 6, 5);
    printDragonCurve(5, 46, 10);
    printDragonCurve(42, 764853475, 30);
    */
}

