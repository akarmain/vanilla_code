#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

vector<int> fermat_factorization(int n) {
  vector<int> ans;
  while (n % 2 != 1) {
    ans.push_back(2);
    n /= 2;
  }
  if (n == 1) {
    return ans;
  }

  int a, b, b2;
  a = ceil(sqrt(n));
  b2 = a * a - n;
  while (pow((int)sqrt(b2), 2) != b2) {
    a += 1;
    b2 = a * a - n;
  }
  b = sqrt(b2);
  ans.push_back(a - b);
  ans.push_back(a + b);

  return ans;
}

int main() {
  int n;
  cout << "Enter N:\n";
  cin >> n;

  cout << "Ans: ";
  for (int x : fermat_factorization(n)) {
    cout << x << " ";
  }
  return 0;
}
