#include <iostream>
using namespace std;
#include <cmath>

double f(double x) { return acos((1 - x * x) / (1 + x * x)) - x; }

int main() {
  double l, r, m;
  l = 2;
  r = 3;

  while (r - l > 0.00001) {
    m = (l + r) / 2;
    if (f(l) * f(m) <= 0) {
      r = m;
    } else {
      l = m;
    }
  }

  cout << (l + r) / 2;
}
