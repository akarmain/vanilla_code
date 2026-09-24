// Group: INBO-30-25
// Student: Кармаев Андрей Александрович

#include <iostream>
#include <vector>
using namespace std;

int main() {
  int n;
  cout << "Enter array size:\n";
  if (!(cin >> n) || n < 0)
    return 0;

  vector<int> a(n);
  cout << "Enter " << n << " integers:\n";
  for (int i = 0; i < n; ++i)
    cin >> a[i];

  cout << "Odd-index elements in reverse order:\n";
  bool first = true;
  for (int i = n - 1; i >= 0; --i) {
    if (i % 2 == 1) {
      if (!first)
        cout << ' ';
      cout << a[i];
      first = false;
    }
  }
  cout << '\n';
  return 0;
}
