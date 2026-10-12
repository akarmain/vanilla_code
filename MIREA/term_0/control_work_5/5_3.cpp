#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<int> prefix(string p) {
  int m = p.size();
  vector<int> pi(m);
  for (int i = 1, j = 0; i < m; i++) {
    while (j > 0 && p[i] != p[j])
      j = pi[j - 1];
    if (p[i] == p[j])
      j++;
    pi[i] = j;
  }
  return pi;
}

vector<int> kmp(string s, string p) {
  vector<int> ans;
  vector<int> pi = prefix(p);
  int j = 0;
  for (int i = 0; i < s.size(); i++) {
    while (j > 0 && s[i] != p[j])
      j = pi[j - 1];
    if (s[i] == p[j])
      j++;
    if (j == p.size()) {
      ans.push_back(i - j + 1);
      j = pi[j - 1];
    }
  }
  return ans;
}

int main() {
  string s, p;
  cin >> s >> p;
  vector<int> pos = kmp(s, p);
  for (int x : pos)
    cout << x << " ";
}
