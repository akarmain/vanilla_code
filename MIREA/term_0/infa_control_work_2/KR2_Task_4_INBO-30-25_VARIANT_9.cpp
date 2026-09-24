// Group: INBO-30-25
// Student: Кармаев Андрей Александрович

#include <iostream>
using namespace std;

int main() {
  int n;
  cout << "Enter matrix size n (square):\n";
  if (!(cin >> n) || n <= 0)
    return 0;

  int **a = new int *[n];
  for (int i = 0; i < n; ++i)
    a[i] = new int[n];

  cout << "Enter " << n * n << " integers (row by row):\n";
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < n; ++j)
      cin >> a[i][j];

  cout << "Elements below main diagonal (one per line):\n";
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < n; ++j)
      if (i > j)
        cout << a[i][j] << '\n';

  for (int i = 0; i < n; ++i)
    delete[] a[i];
  delete[] a;
  return 0;
}
