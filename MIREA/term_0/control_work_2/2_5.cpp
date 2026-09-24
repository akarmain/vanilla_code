#include <iomanip>
#include <iostream>
#include <string>
using namespace std;

static string pad_left_zeros(const string &s, size_t n) {
  return (s.size() >= n) ? s : string(n - s.size(), '0') + s;
}

static int middle_square_next(int x) {
  long long sq = 1LL * x * x;
  string s = pad_left_zeros(to_string(sq), 10);
  string mid = s.substr(2, 5);
  return stoi(mid);
}

int main() {
  int seed;
  cout << "Enter 5-digit seed (00000..99999):\n";
  if (!(cin >> seed) || seed < 0 || seed > 99999) {
    cout << "Invalid seed\n";
    return 0;
  }

  cout << "Von Neumann sequence (10 terms):\n";
  int x = seed;
  for (int i = 1; i <= 10; ++i) {
    x = middle_square_next(x);
    cout << setw(5) << setfill('0') << x << (i == 10 ? '\n' : ' ');
    if (x == 0 && i < 10) {
      for (int j = i + 1; j <= 10; ++j)
        cout << "00000" << (j == 10 ? '\n' : ' ');
      break;
    }
  }
  return 0;
}
