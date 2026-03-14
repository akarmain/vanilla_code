#include <iostream>
#include <vector>
using namespace std;

vector<bool> sieve_eratosthenes(int n) {
  // Обратное решето Эратосфена, оно работает
  vector<bool> ans(1, n);
  ans[0] = 1;
  ans[1] = 1;

  for (int i = 2; i < n; i++) {
    bool f = 1;
    for (int j = i; j < n; j += i) {
      if (f) {
        f = 0;
        continue;
      }
      ans[j] = 1;
      cout << j << " ";
    }
    cout << endl;
  }

  return ans;
}

int main() {
  cout << "Enter N: \n";
  int n;
  cin >> n;
  n++;
  cout << "Ans: \n";

  vector<bool> ans = sieve_eratosthenes(n);
  cout << endl;

  for (int i = 0; i < n; i++) {
    if (!ans[i]) {
      cout << i << " ";
    }
  }
  return 0;
}
