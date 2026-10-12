#include <iostream>
#include <sstream>
#include <string>
using namespace std;

string solve(string s) {
  string w, r = "";
  stringstream ss(s);
  while (ss >> w)
    r = w + (r == "" ? "" : " " + r);
  return r;
}

int main() {
  string s;
  getline(cin, s);
  cout << solve(s);
}
