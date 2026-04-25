#include <iostream>
using namespace std;

int main() {
  long long A, B;
  if (!(cin >> A >> B))
    return 0;
  if (B == 0)
    return 0;
  long long left = 0;
  long long right = A;
  long long ans = 0;
  while (left <= right) {
    long long mid = left + (right - left) / 2;
    __int128 prod = (__int128)B * mid;
    if (prod <= A) {
      ans = mid;
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  long long q = ans;
  long long r = A - B * q;
  cout << q << " " << r << '\n';
  return 0;
}
