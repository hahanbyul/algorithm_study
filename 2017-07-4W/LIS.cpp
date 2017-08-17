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
        int  MaxLength(int index);
        void PrintCache();
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
            ret = MaxLength(i);
            cache[i] = ret;
        }
        max_val = max(max_val, ret);
    }

    cout << max_val << endl;
    return max_val;
}

int LIS::MaxLength(int index) {
    if (cache[index] != -1)
        return cache[index];

    int ret = 1;
    for (int i = index+1; i < N; i++)
        if (seq[i] > seq[index])
            ret = max(ret, 1 + MaxLength(i));
    cache[index] = ret;
    return ret;
}

void LIS::PrintCache() {
    cout << "cache: ";
    for (int i = 0; i < N; i++)
        cout << cache[i] << ' ';
    cout << endl;
}
