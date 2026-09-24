// Group: INBO-30-25
// Student: Кармаев Андрей Александрович

#include <iostream>
#include <vector>
using namespace std;

int main() {
  int n, m;
  cout << "Enter rows and cols:\n";
  if (!(cin >> n >> m) || n <= 0 || m <= 0)
    return 0;

  vector<vector<int>> a(n, vector<int>(m));
  cout << "Enter " << n * m << " integers (row by row):\n";
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < m; ++j)
      cin >> a[i][j];

  int cnt = 0;
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < m; ++j)
      if (a[i][j] % 2 == 0)
        ++cnt;

  cout << "Even elements count: " << cnt << '\n';
  return 0;
}
