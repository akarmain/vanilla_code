#include <iostream>
using namespace std;

void h(int n, char a, char b, char c) {
  if (n == 0)
    return;
  h(n - 1, a, c, b);
  cout << a << " " << c << "\n";
  h(n - 1, b, a, c);
}

int main() {
  int n;
  cin >> n;
  h(n, 'A', 'B', 'C');
}
