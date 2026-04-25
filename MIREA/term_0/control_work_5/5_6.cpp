#include <iostream>
using namespace std;

double f(double x) { return x * x - 2; }

double solve(double l, double r) {
  double m = (l + r) / 2;
  if (r - l < 0.000001)
    return m;
  if (f(m) == 0)
    return m;
  if (f(l) * f(m) < 0)
    return solve(l, m);
  return solve(m, r);
}

int main() { cout << solve(0, 2); }
