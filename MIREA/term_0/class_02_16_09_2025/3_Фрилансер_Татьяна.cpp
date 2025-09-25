#include <iostream>
using namespace std;

int main() {
  cout << "Enter A and B\n";
  float a, b;
  cin >> a >> b;
  while (a > b) {
    if ((int)a % 2 == 0 and (a / 2 >= b)) {
      cout << ":2 " << "\n";
      a /= 2;
    } else {
      cout << "-1 " << "\n";
      a -= 1;
    }
  }
}
