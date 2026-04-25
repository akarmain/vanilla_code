// Group: INBO-30-25
// Student: Кармаев Андрей Александрович

#include <cstdlib>
#include <ctime>
#include <iostream>
#include <vector>
using namespace std;

static void fill_random_and_print(vector<vector<int>> &a, int n, int m) {
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < m; ++j)
      a[i][j] = rand() % 100; // 0..99

  cout << "Matrix " << n << "x" << m << ":\n";
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      cout << a[i][j] << (j + 1 == m ? '\n' : ' ');
    }
  }
}

int main() {
  srand((unsigned)time(nullptr));
  int n, m;
  cout << "Enter rows and cols:\n";
  if (!(cin >> n >> m) || n <= 0 || m <= 0)
    return 0;

  vector<vector<int>> a(n, vector<int>(m));
  fill_random_and_print(a, n, m);
  return 0;
}
