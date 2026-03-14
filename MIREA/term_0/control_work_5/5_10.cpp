#include <iostream>
using namespace std;

void qs(int a[], int l, int r) {
  int i = l, j = r, p = a[(l + r) / 2];
  while (i <= j) {
    while (a[i] < p)
      i++;
    while (a[j] > p)
      j--;
    if (i <= j)
      swap(a[i++], a[j--]);
  }
  if (l < j)
    qs(a, l, j);
  if (i < r)
    qs(a, i, r);
}

int main() {
  int n;
  cin >> n;
  int a[n];
  for (int i = 0; i < n; i++)
    cin >> a[i];
  qs(a, 0, n - 1);
  for (int i = 0; i < n; i++)
    cout << a[i] << " ";
}
