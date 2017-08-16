#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class LIS {
    private:
        int* seq;
        int N;
        int* cache;

    public:
        LIS(int N);
        ~LIS();
        void ReadSeq();
        int  Solve();
        int  MaxLength(int max_val, int index);
};

int main() {
    int C;
    cin >> C;
    for (int c = 0; c < C; c++) {
        int N;
        cin >> N;
        LIS* lis = new LIS(N);
        lis->ReadSeq();
        lis->Solve();
    }
    return 0;
}

LIS::LIS(int N_) {
    N = N_;
    seq = new int[N];
    cache = new int[N];
    for (int i = 0; i < N; i++)
        cache[i] = -1;
}

LIS::~LIS() {
    delete []cache;
}

void LIS::ReadSeq() {
    int num;
    for (int i = 0; i < N; i++) {
        cin >> num;
        seq[i] = num;
    }
}

int LIS::Solve() {
    int ret;
    int max_val = 0;

    for (int i = 0; i < N; i++) {
        ret = cache[i];
        if (ret == -1) {
            ret = MaxLength(0, i);
            cache[i] = ret;
        }
        max_val = max(max_val, ret);
    }

    /*
    cout << "cache: ";
    for (int i = 0; i < N; i++)
        cout << cache[i] << ' ';
    cout << endl;
    */

    cout << max_val << endl;
    return max_val;
}

int LIS::MaxLength(int max_val, int index) {
    // cout << "val: " << max_val << ", index: " << index << endl;
    if (cache[index] != -1)
        return cache[index];

    if (index >= N)
        return 0;

    if (seq[index] <= max_val)
        return MaxLength(max_val, index+1);
    else {
        int ret = 0;
        for (int i = index; i < N; i++)
            ret = max(ret, 1 + MaxLength(seq[index], i+1));
        // cout << "return: " << ret << endl;
        cache[index] = ret;
        return ret;
    }
}
