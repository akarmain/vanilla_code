#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

vector<int> sieve(int limit) {
  vector<int> primes;
  if (limit < 2)
    return primes;
  vector<bool> is_prime(limit + 1, true);
  is_prime[0] = is_prime[1] = false;
  for (int p = 2; p * 1LL * p <= limit; ++p) {
    if (is_prime[p]) {
      for (long long q = 1LL * p * p; q <= limit; q += p)
        is_prime[(int)q] = false;
    }
  }
  for (int i = 2; i <= limit; ++i)
    if (is_prime[i])
      primes.push_back(i);
  return primes;
}

int main() {
  long long n;
  cout << "Enter n:\n";
  if (!(cin >> n))
    return 0;

  if (n == 0) {
    cout << "Factorization is undefined for n = 0\n";
    return 0;
  }

  cout << "Prime factors (p : multiplicity):\n";
  if (n < 0) {
    cout << "-1 : 1\n";
    n = -n;
  }

  if (n == 1) {
    cout << "(none)  // n = 1 не имеет простых множителей\n";
    return 0;
  }
  long long limit = floor(sqrt((long double)n));
  vector<int> primes = sieve((int)limit);
  vector<pair<long long, int>> factors;
  for (int p : primes) {
    if (1LL * p * p > n)
      break;
    if (n % p == 0) {
      int k = 0;
      while (n % p == 0) {
        n /= p;
        ++k;
      }
      factors.push_back({p, k});
    }
  }
  if (n > 1) {
    factors.push_back({n, 1});
  }
  if (factors.empty()) {
    cout << "(none)\n";
  } else {
    for (auto &fk : factors) {
      cout << fk.first << " : " << fk.second << "\n";
    }
  }
  return 0;
}
