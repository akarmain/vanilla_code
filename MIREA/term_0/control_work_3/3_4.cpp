#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

string strip_leading_zeros(const string &s) {
  size_t pos = s.find_first_not_of('0');
  if (pos == string::npos)
    return "0";
  return s.substr(pos);
}

string multiply_school(const string &a, const string &b) {
  string x = strip_leading_zeros(a);
  string y = strip_leading_zeros(b);
  if (x == "0" || y == "0")
    return "0";
  int n = x.size();
  int m = y.size();
  vector<int> res(n + m, 0);
  for (int i = n - 1; i >= 0; --i) {
    int da = x[i] - '0';
    for (int j = m - 1; j >= 0; --j) {
      int db = y[j] - '0';
      res[n - 1 - i + m - 1 - j] += da * db;
    }
  }
  int carry = 0;
  for (size_t k = 0; k < res.size(); ++k) {
    int v = res[k] + carry;
    res[k] = v % 10;
    carry = v / 10;
  }
  while (carry) {
    res.push_back(carry % 10);
    carry /= 10;
  }
  while (res.size() > 1 && res.back() == 0)
    res.pop_back();
  string s;
  for (int i = (int)res.size() - 1; i >= 0; --i)
    s.push_back(char('0' + res[i]));
  return strip_leading_zeros(s);
}

int main() {
  string a, b;
  if (!(cin >> a >> b))
    return 0;
  cout << multiply_school(a, b) << '\n';
  return 0;
}
