#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;

void print_land(vector<vector<int> > land) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++)
            cout << land[i][j] << " ";
        cout << endl;
    }
}

void print_cache(int** cache, int N) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < 4; j++)
            cout << cache[i][j] << " ";
        cout << endl;
    }
}

int solve(int** cache, vector<vector<int> > land, int row_index, int prev_i) {
    // cout << "row: " << row_index << ", prev_i: " << prev_i << endl;
    // print_cache(cache, land.size());
    if (row_index >= land.size())
        return 0;

    if (row_index != 0 && cache[row_index-1][prev_i] != -1)
        return cache[row_index-1][prev_i];

    int ret = 0;
    for (int i = 0; i < 4; i++) {
        if (i == prev_i)
            continue;
        ret = max(ret, land[row_index][i] + solve(cache, land, row_index+1, i));
    }

    // cout << "ret: " << ret << endl;
    if (row_index != 0)
        cache[row_index-1][prev_i] = ret;
    return ret;
}

int** initialize_cache(int N) {
    int** cache = new int* [N];
    for (int i = 0; i < N; i++) {
        cache[i] = new int[4];
        for (int j = 0; j < 4; j++)
            cache[i][j] = -1;
    }
    return cache;
}

int solution(vector<vector<int> > land) {
    int N = land.size();
    int** cache = initialize_cache(N);

	int answer = solve(cache, land, 0, -1);
	return answer;
}


int main() {
    int problem[3][4] = {{1,2,3,5},{5,6,7,8},{4,3,2,1}};
    vector<vector<int> > land;
    for (int i = 0; i < 3; i++) {
        vector<int> row;
        for (int j = 0; j < 4; j++)
            row.push_back(problem[i][j]);
        land.push_back(row);
    }

    // print_land(land);

    cout << solution(land) << endl;
    // solution(land);

    return 0;
}
