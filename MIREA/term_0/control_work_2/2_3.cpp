#include <cmath>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

static inline bool is_perfect_square(long long x) {
  if (x < 0)
    return false;
  long long r = (long long)floor(sqrt((long double)x) + 0.5L);
  return r * r == x;
}

vector<int> sieve(int limit) {
  vector<int> primes;
  if (limit < 2)
    return primes;
  vector<bool> is_prime(limit + 1, true);
  is_prime[0] = is_prime[1] = false;
  for (int p = 2; 1LL * p * p <= limit; ++p) {
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

bool is_prime_by_primes(long long n, const vector<int> &primes) {
  if (n < 2)
    return false;
  for (int p : primes) {
    long long pp = 1LL * p * p;
    if (pp > n)
      break;
    if (n % p == 0)
      return false;
  }
  return true;
}

void fermat_factor(long long n, const vector<int> &primes,
                   vector<long long> &out) {
  if (is_prime_by_primes(n, primes)) {
    out.push_back(n);
    return;
  }

  long long a = (long long)ceil(sqrt((long double)n));
  if (a * a < n)
    ++a;
  long long b2 = a * a - n;

  while (!is_perfect_square(b2)) {
    ++a;
    b2 = a * a - n;
  }

  long long b = (long long)llround(sqrt((long double)b2));
  long long x = a - b;
  long long y = a + b;

  if (x > 1 && (x % 2 == 1)) {
    if (is_prime_by_primes(x, primes))
      out.push_back(x);
    else
      fermat_factor(x, primes, out);
  } else if (x > 1) {
    long long t = x;
    for (int p : primes) {
      if (1LL * p * p > t)
        break;
      while (t % p == 0) {
        out.push_back(p);
        t /= p;
      }
    }
    if (t > 1)
      out.push_back(t);
  }

  if (y > 1 && (y % 2 == 1)) {
    if (is_prime_by_primes(y, primes))
      out.push_back(y);
    else
      fermat_factor(y, primes, out);
  } else if (y > 1) {
    long long t = y;
    for (int p : primes) {
      if (1LL * p * p > t)
        break;
      while (t % p == 0) {
        out.push_back(p);
        t /= p;
      }
    }
    if (t > 1)
      out.push_back(t);
  }
}

int main() {
  long long n0;
  cout << "Enter odd n:\n";
  if (!(cin >> n0))
    return 0;

  if (n0 == 0) {
    cout << "Factorization is undefined for n = 0\n";
    return 0;
  }
  if (n0 == 1 || n0 == -1) {
    cout << "No prime factors for |n| = 1\n";
    return 0;
  }

  bool neg = (n0 < 0);
  long long n = llabs(n0);

  if (n % 2 == 0) {
    cout << "Error: n must be odd by task condition.\n";
    return 0;
  }

  int limit = (int)floor(sqrt((long double)n));
  vector<int> primes = sieve(limit);

  vector<long long> raw_factors;
  if (neg) {
    cout << "-1 : 1\n";
  }

  if (n == 1) {
    return 0;
  }

  fermat_factor(n, primes, raw_factors);
  map<long long, int> mult;
  for (auto p : raw_factors)
    ++mult[p];
  cout << "Prime factors (p : multiplicity):\n";
  for (auto &kv : mult) {
    cout << kv.first << " : " << kv.second << "\n";
  }
  return 0;
}
