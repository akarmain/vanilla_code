// Group: INBO-30-25
// Student: Кармаев Андрей Александрович

#include <iostream>
#include <vector>
using namespace std;

static double mean(const int *arr, int n) {
  if (n <= 0)
    return 0.0;
  long long s = 0;
  for (int i = 0; i < n; ++i)
    s += arr[i];
  return static_cast<double>(s) / n;
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

  cout << "Mean: " << mean(a.data(), n) << '\n';
  return 0;
}
