#include <iostream>
#include <string>
using namespace std;

string strip_leading_zeros_dec(const string &s) {
  size_t pos = s.find_first_not_of('0');
  if (pos == string::npos)
    return "0";
  return s.substr(pos);
}

string add_decimal_accelerated(string a, string b) {
  a = strip_leading_zeros_dec(a);
  b = strip_leading_zeros_dec(b);
  if (a == "0" && b == "0")
    return "0";
  if (a.size() < b.size())
    a = string(b.size() - a.size(), '0') + a;
  else if (b.size() < a.size())
    b = string(a.size() - b.size(), '0') + b;
  string x(a.rbegin(), a.rend());
  string y(b.rbegin(), b.rend());
  while (true) {
    int n = x.size();
    string sum(n, '0');
    string carry_raw(n + 1, '0');
    for (int i = 0; i < n; ++i) {
      int t = (x[i] - '0') + (y[i] - '0');
      sum[i] = char('0' + (t % 10));
      carry_raw[i + 1] = char('0' + (t / 10));
    }
    string new_y(n, '0');
    bool any = false;
    for (int i = 0; i < n; ++i) {
      new_y[i] = carry_raw[i];
      if (new_y[i] != '0')
        any = true;
    }
    if (carry_raw[n] != '0') {
      sum.push_back('0');
      new_y.push_back(carry_raw[n]);
      if (carry_raw[n] != '0')
        any = true;
    }
    x = sum;
    y = new_y;
    if (!any)

      break;
  }
  string res(x.rbegin(), x.rend());
  return strip_leading_zeros_dec(res);
}

int main() {
  string a, b;
  if (!(cin >> a >> b))
    return 0;
  cout << add_decimal_accelerated(a, b) << '\n';
  return 0;
}
