#include <iostream>
using namespace std;

int main() {
  cout << "Enter N (side of the square):\n";
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    for (int g = n - i - 1; g > 0; g--) {
      cout << "0 ";
    }
    cout << "1 ";
    for (int g = i; g > 0; g--) {
      cout << "2 ";
    }
    cout << endl;
  }

  return 0;
}
