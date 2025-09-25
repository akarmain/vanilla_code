#include <iostream>
#include <vector>
using namespace std;

int n, m;
vector<vector<int>> arr;
void cet_count_of_mushroom(int r, int c) {
  int i = r - 1;
  int j = c - 1;

  if (arr[i][j] == -1)
    return;

  for (int di = -1; di <= 1; ++di) {
    for (int dj = -1; dj <= 1; ++dj) {
      if (di == 0 && dj == 0)
        continue;
      int ni = i + di, nj = j + dj;
      if (0 <= ni && ni < n && 0 <= nj && nj < m && arr[ni][nj] != -1) {
        arr[ni][nj] += 1;
      }
    }
  }
}

int main() {
  cin.tie(nullptr);
  cin >> n >> m;
  arr.assign(n, vector<int>(m, 0));

  int w;
  cin >> w;

  for (int g = 0; g < w; ++g) {
    int r, c;
    cin >> r >> c;
    if (r < 1 || r > n || c < 1 || c > m)
      continue;
    cet_count_of_mushroom(r, c);
    arr[r - 1][c - 1] = -1;
  }

  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      if (arr[i][j] == -1) {
        cout << '*' << " ";
      } else {
        cout << arr[i][j] << " ";
      }
    }
    cout << '\n';
  }
  return 0;
}
