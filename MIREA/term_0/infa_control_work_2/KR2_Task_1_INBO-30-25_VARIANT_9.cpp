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

  vector<int> b;
  b.reserve(n);
  for (int x : a)
    if (x != 0)
      b.push_back(x);

  cout << "Array without zeros:\n";
  for (int i = 0; i < (int)b.size(); ++i) {
    cout << b[i] << (i + 1 == (int)b.size() ? '\n' : ' ');
  }
  if (b.empty())
    cout << '\n';
  return 0;
}
