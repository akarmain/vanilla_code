#include <iostream>
using namespace std;
#include <cstdlib>

int gcd_mod(int a, int b) {
  a = std::abs(a);
  b = std::abs(b);
  if (a == 0)
    return b;
  if (b == 0)
    return a;
  while (b != 0) {
    int r = a % b;
    a = b;
    b = r;
  }
  return a;
}

int main() {
  int a, b, c;
  cout << "Enter a, b, c:\n";
  if (!(cin >> a >> b >> c))
    return 0;
  int g = gcd_mod(gcd_mod(a, b), c);
  cout << "GCD: " << g << '\n';
}
