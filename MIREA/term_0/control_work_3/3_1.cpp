#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

string strip_leading_zeros(const string &s) {
  size_t pos = s.find_first_not_of('0');
  if (pos == string::npos)
    return "0";
  return s.substr(pos);
}

int compare_strings_num(const string &a, const string &b) {
  string x = strip_leading_zeros(a);
  string y = strip_leading_zeros(b);
  if (x.size() < y.size())
    return -1;
  if (x.size() > y.size())
    return 1;
  if (x == y)
    return 0;
  return x < y ? -1 : 1;
}

string add_strings(const string &a, const string &b) {
  string x(a.rbegin(), a.rend());
  string y(b.rbegin(), b.rend());
  int n = max(x.size(), y.size());
  x.resize(n, '0');
  y.resize(n, '0');
  string res;
  int carry = 0;
  for (int i = 0; i < n; ++i) {
    int d = (x[i] - '0') + (y[i] - '0') + carry;
    res.push_back(char('0' + (d % 10)));
    carry = d / 10;
  }
  if (carry)
    res.push_back(char('0' + carry));
  while (res.size() > 1 && res.back() == '0')
    res.pop_back();
  reverse(res.begin(), res.end());
  return res;
}

string sub_strings_nonneg(const string &a, const string &b) {
  string x(a.rbegin(), a.rend());
  string y(b.rbegin(), b.rend());
  int n = max(x.size(), y.size());
  x.resize(n, '0');
  y.resize(n, '0');
  string res;
  int borrow = 0;
  for (int i = 0; i < n; ++i) {
    int d = (x[i] - '0') - (y[i] - '0') - borrow;
    if (d < 0) {
      d += 10;
      borrow = 1;
    } else
      borrow = 0;
    res.push_back(char('0' + d));
  }
  while (res.size() > 1 && res.back() == '0')
    res.pop_back();
  reverse(res.begin(), res.end());
  return strip_leading_zeros(res);
}

int main() {
  string a, b;
  if (!(cin >> a >> b))
    return 0;
  cout << add_strings(a, b) << '\n';
  int cmp = compare_strings_num(a, b);
  string bigger, smaller;
  if (cmp >= 0) {
    bigger = a;
    smaller = b;
  } else {
    bigger = b;
    smaller = a;
  }
  cout << sub_strings_nonneg(bigger, smaller) << '\n';
  return 0;
}
