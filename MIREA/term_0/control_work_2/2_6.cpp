#include <iostream>
#include <vector>
using namespace std;

vector<int> primes_sundaram(int N) {
  vector<int> primes;
  if (N < 2)
    return primes;
  if (N >= 2)
    primes.push_back(2);

  int k = (N - 1) / 2;
  vector<bool> removed(k + 1, false);

  for (int i = 1; i <= k; ++i) {
    int j = i;
    long long idx = i + j + 2LL * i * j;
    while (idx <= k) {
      removed[(int)idx] = true;
      ++j;
      idx = i + j + 2LL * i * j;
    }
  }

  for (int n = 1; n <= k; ++n) {
    if (!removed[n]) {
      int p = 2 * n + 1;
      if (p <= N)
        primes.push_back(p);
    }
  }
  return primes;
}

int main() {
  int N;
  cout << "Enter N:\n";
  if (!(cin >> N))
    return 0;

  auto ps = primes_sundaram(N);
  cout << "Primes <= " << N << ":\n";
  for (size_t i = 0; i < ps.size(); ++i) {
    cout << ps[i] << (i + 1 == ps.size() ? '\n' : ' ');
  }
  return 0;
}
