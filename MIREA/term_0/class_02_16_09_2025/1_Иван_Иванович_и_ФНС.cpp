// Переборщил, нужно было по проще)

#include <cmath>
#include <iostream>
using namespace std;
int main() {
  cout << "Enter X and Y\n";
  double x, y, z;
  z = 0;
  cin >> x >> y;

  for (int n = 1; n <= pow(2, 8); ++n) {
    z = z + x * pow(n, 1.1);
    if (y < z) {
      cout << "Ivan Ivanovich will go to prison in " << n << " days";
      return 0;
    }
  }
  cout << "Ivan Ivanovich will not go to prison";
  return 0;
}
