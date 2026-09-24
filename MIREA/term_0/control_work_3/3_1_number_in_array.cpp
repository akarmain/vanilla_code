#include <cstdlib>
#include <iostream>
using namespace std;

int main() {
  int n;
  cin >> n;

  short *number = new short[n];

  for (int i = 0; i < n; i++) {
    number[i] = rand() % 10;
  }

  for (int i = n - 1; i >= 0; i--) {
    cout << number[i];
  }

  delete[] number;
  return 0;
}
