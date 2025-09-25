#include <iostream>
using namespace std;

int main() {
  int a, b;
  char symbol;
  cout << "Entaer A and B\n";
  cin >> a >> b;
  cout << "Entaer a symbol +, -, * or /\n";
  cin >> symbol;

  cout << "Result: ";
  if (symbol == '+') {
    cout << a + b;
  } else if (symbol == '-') {
    cout << a - b;
  } else if (symbol == '*') {
    cout << a * b;
  } else if (symbol == '/') {
    cout << a * 1.0 / b;
  } else {
    cout << "Errrror";
  }
  return 0;
}
