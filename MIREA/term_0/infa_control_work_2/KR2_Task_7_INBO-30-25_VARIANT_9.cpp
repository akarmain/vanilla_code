// Group: INBO-30-25
// Student: Кармаев Андрей Александрович

#include <iostream>
#include <vector>
using namespace std;

static int *find_first(int *a, int n, int x) {
  for (int i = 0; i < n; ++i)
    if (a[i] == x)
      return &a[i];
  return nullptr;
}

int main() {
  int n;
  cout << "Enter array size:\n";
  if (!(cin >> n) || n <= 0)
    return 0;

  vector<int> a(n);
  cout << "Enter " << n << " integers:\n";
  for (int i = 0; i < n; ++i)
    cin >> a[i];

  int x;
  cout << "Enter value to find:\n";
  cin >> x;

  int *p = find_first(a.data(), n, x);
  if (p) {
    cout << "Found at index " << (p - a.data()) << ": " << *p << '\n';
  } else {
    cout << "Not found\n";
  }
  return 0;
}
