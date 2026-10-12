#include <iostream>
using namespace std;

int main() {
  int a, b;
  cout << "Enter a & b:\n";
  cin >> a >> b;
  while (a != b) {
    if (a - b > 0) {
      a = a - b;
    } else {
      b = b - a;
    }
  }
  cout << "Ans: " << a;
}
