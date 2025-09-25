#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<int> nums = {5, 2, 6, 1};
  vector<int> counts;
  int count;
  for (long i = 0; i < (int)nums.size(); i++) {
    count = 0;
    for (long j = i; j < (int)nums.size(); j++) {
      if (nums[i] > nums[j]) {
        count++;
      }
    }
    counts.push_back(count);
  }

  for (auto &n : counts) {
    cout << n << "";
  }
  return 0;
}
