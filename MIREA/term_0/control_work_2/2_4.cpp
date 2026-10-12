#include <cstdint>
#include <iostream>
using namespace std;

static bool is_prime_small(int p) {
  if (p < 2)
    return false;
  if (p % 2 == 0)
    return p == 2;
  for (int d = 3; 1LL * d * d <= p; d += 2)
    if (p % d == 0)
      return false;
  return true;
}

static bool lucas_lehmer_u64(int p) {
  if (p == 2)
    return true;
  uint64_t M =
      (p == 63) ? (uint64_t)(~0ULL >> 1) * 2 + 1 : ((1ULL << p) - 1ULL);
  __uint128_t s = 4;
  for (int i = 0; i < p - 2; ++i) {
    s = (s * s - 2) % M;
  }
  return (uint64_t)s == 0;
}

int main() {
  int p;
  cout << "Enter p:\n";
  if (!(cin >> p))
    return 0;

  if (p < 2 || p > 63) {
    cout << "p must be in\n";
    return 0;
  }
  if (!is_prime_small(p)) {
    cout << "p is not prime -> M_p is composite\n";
    return 0;
  }
  bool ok = lucas_lehmer_u64(p);
  cout << "M_" << p << " = 2^" << p << " - 1 is "
       << (ok ? "PRIME" : "COMPOSITE") << " (Lucas-Lehmer)\n";
  return 0;
}
