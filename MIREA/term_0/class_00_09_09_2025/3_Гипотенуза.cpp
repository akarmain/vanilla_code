#include <iostream>
#include <string>
using namespace std;
#include <cmath>
// https://codelessons.dev/ru/pow-in-cplusplus/

int main() {
  int a, b;
  cout << "Enter two numbers (a, b): ";
  cin >> a >> b;
  cout << pow(pow(a, 2) + pow(b, 2), 0.5) << " ";
}
