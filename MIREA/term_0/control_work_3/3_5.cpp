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
    for (int j = m - 1; j >= 0; --j) {
      int p = (x[i] - '0') * (y[j] - '0');
      int pos1 = i + j;
      int pos2 = i + j + 1;
      int s = p + res[pos2];
      res[pos2] = s % 10;
      res[pos1] += s / 10;
    }
  }
  int i = 0;
  while (i < (int)res.size() - 1 && res[i] == 0)
    ++i;
  string out;
  for (; i < (int)res.size(); ++i)
    out.push_back(char('0' + res[i]));
  return out;
}

vector<int> to_vec(const string &s) {
  vector<int> v;
  v.reserve(s.size());
  for (int i = (int)s.size() - 1; i >= 0; --i)
    v.push_back(s[i] - '0');
  return v;
}

vector<int> add_vec(const vector<int> &a, const vector<int> &b) {
  size_t n = max(a.size(), b.size());
  vector<int> res;
  res.reserve(n + 1);
  int carry = 0;
  for (size_t i = 0; i < n; ++i) {
    int da = i < a.size() ? a[i] : 0;
    int db = i < b.size() ? b[i] : 0;
    int s = da + db + carry;
    res.push_back(s % 10);
    carry = s / 10;
  }
  if (carry)
    res.push_back(carry);
  return res;
}

vector<int> sub_vec(const vector<int> &a, const vector<int> &b) {
  vector<int> res;
  res.reserve(a.size());
  int borrow = 0;
  for (size_t i = 0; i < a.size(); ++i) {
    int da = a[i];
    int db = i < b.size() ? b[i] : 0;
    int d = da - db - borrow;
    if (d < 0) {
      d += 10;
      borrow = 1;
    } else {
      borrow = 0;
    }
    res.push_back(d);
  }
  while (res.size() > 1 && res.back() == 0)
    res.pop_back();
  return res;
}

vector<int> karatsuba_vec(vector<int> a, vector<int> b) {
  if (a.empty() || b.empty())
    return vector<int>(1, 0);
  if (a.size() < b.size())
    swap(a, b);
  int n = (int)a.size();
  if (n <= 32 || (int)b.size() <= 32) {
    vector<int> res(a.size() + b.size(), 0);
    for (int i = 0; i < (int)a.size(); ++i) {
      int carry = 0;
      for (int j = 0; j < (int)b.size(); ++j) {
        int s = res[i + j] + a[i] * b[j] + carry;
        res[i + j] = s % 10;
        carry = s / 10;
      }
      int k = i + (int)b.size();
      while (carry) {
        int s = res[k] + carry;
        res[k] = s % 10;
        carry = s / 10;
        ++k;
      }
    }
    while (res.size() > 1 && res.back() == 0)
      res.pop_back();
    return res;
  }
  if ((int)b.size() < n)
    b.resize(n, 0);
  int m = n / 2;
  vector<int> a0(a.begin(), a.begin() + m);
  vector<int> a1(a.begin() + m, a.end());
  vector<int> b0(b.begin(), b.begin() + m);
  vector<int> b1(b.begin() + m, b.end());
  vector<int> z0 = karatsuba_vec(a0, b0);
  vector<int> z2 = karatsuba_vec(a1, b1);
  vector<int> a_sum = add_vec(a0, a1);
  vector<int> b_sum = add_vec(b0, b1);
  vector<int> z1 = karatsuba_vec(a_sum, b_sum);
  vector<int> t = sub_vec(z1, z0);
  t = sub_vec(t, z2);
  vector<int> res(z2.size() + 2 * m + 5, 0);
  for (size_t i = 0; i < z0.size(); ++i)
    res[i] += z0[i];
  for (size_t i = 0; i < t.size(); ++i)
    res[i + m] += t[i];
  for (size_t i = 0; i < z2.size(); ++i)
    res[i + 2 * m] += z2[i];
  int carry = 0;
  for (size_t i = 0; i < res.size(); ++i) {
    int s = res[i] + carry;
    res[i] = s % 10;
    carry = s / 10;
  }
  while (carry) {
    res.push_back(carry % 10);
    carry /= 10;
  }
  while (res.size() > 1 && res.back() == 0)
    res.pop_back();
  return res;
}

string multiply_karatsuba(const string &a, const string &b) {
  string x = strip_leading_zeros(a);
  string y = strip_leading_zeros(b);
  if (x == "0" || y == "0")
    return "0";
  vector<int> vx = to_vec(x);
  vector<int> vy = to_vec(y);
  vector<int> v = karatsuba_vec(vx, vy);
  string res;
  res.reserve(v.size());
  for (int i = (int)v.size() - 1; i >= 0; --i)
    res.push_back(char('0' + v[i]));
  return strip_leading_zeros(res);
}

int main() {
  string a, b;
  if (!(cin >> a >> b))
    return 0;
  string prod1 = multiply_school(a, b);
  string prod2 = multiply_karatsuba(a, b);
  cout << prod1 << '\n';
  cout << prod2 << '\n';
  return 0;
}
