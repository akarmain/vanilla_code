#include <iostream>
using namespace std;

// Записываем формулу в сокращенном виде 0,7(2с-9к)-4(0,25с-к)
double f(double s, double k) { return 0.4 * s - 2.3 * k; }

int main() {
  cout << "Enter values for с and k: ";
  double с, k;
  cin >> с >> k;
  cout << "Answer " << f(с, k);
}
