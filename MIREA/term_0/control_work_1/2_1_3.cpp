#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<int> nums = {-10, -10, -10, 1, 1, 1};
  int m, l = 0, r = nums.size();
  while (r - l > 1) {
    m = (l + r) / 2;
    if (nums[m] > -1) {
      r = m;
    } else {
      l = m;
    }
  }
  l++;
  r = nums.size() - r;
  cout << l << " " << r << endl;
  if (l == r) {
    cout << "Same";
  }
  if (l > r) {
    cout << " More negative numbers: " << l;
  } else {
    cout << " More positive numbers: " << r;
  }
  return 0;
}
