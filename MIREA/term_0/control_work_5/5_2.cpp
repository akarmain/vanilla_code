#include <iostream>
#include <sstream>
#include <string>
using namespace std;

string solve(string s) {
  string w, best = "";
  stringstream ss(s);
  while (ss >> w)
    if (w.size() > best.size())
      best = w;
  return best;
}

int main() {
  string s;
  getline(cin, s);
  cout << solve(s);
}
