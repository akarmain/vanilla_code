#include <iostream>
#include <vector>
using namespace std;

struct Para {
  int index_left = -1;
  int index_right = -1;
};

Para get_index_para(vector<int> arr) {
  Para para;

  for (int i = 0; i < (int)arr.size() - 1; i++) {
    if (para.index_left != -1 and arr[i + 1] != arr[i]) {
      para.index_right = i;
      return para;
    } else if (para.index_left == -1 and arr[i] == arr[i + 1]) {
      para.index_left = i;
    }
  }
  para.index_right = (int)arr.size() - 1;
  return para;
}

int main() {
  cout << "Enter count of student\n";
  int len_arr, ans = 0;
  cin >> len_arr;
  vector<int> arr(len_arr);
  cout << "Enter students:\n";
  for (int i = 0; i < len_arr; i++) {
    cin >> arr[i];
  }

  while (true) {
    Para para = get_index_para(arr);
    if (para.index_left == -1) {
      break;
    }

    ans += para.index_right - para.index_left + 1;
    arr.erase(arr.begin() + para.index_left,
              arr.begin() + para.index_right + 1);
    len_arr -= ans;
  }

  cout << "ANS: " << ans;
  return 0;
}
