#include <iostream>
#include <vector>
using namespace std;

vector<int> shaker_sorting(vector<int> arr, int n) {
  size_t left = 0;
  size_t right = n - 1;

  while (left < right) {
    for (size_t i = left; i < right; i++) {
      if (arr[i] > arr[i + 1]) {
        swap(arr[i], arr[i + 1]);
      }
    }
    right--;

    for (size_t i = right; i > left; i--) {
      if (arr[i] < arr[i - 1]) {
        swap(arr[i], arr[i - 1]);
      }
    }
    left++;
  }

  return arr;
}

int main() {
  int len_arr;
  cout
      << "Enter the length of the array, and then the values of its elements\n";
  cin >> len_arr;

  vector<int> arr(len_arr);
  for (int i = 0; i < len_arr; i++) {
    cin >> arr[i];
  }

  arr = shaker_sorting(arr, len_arr);

  cout << "Sorted massive: " << endl;
  for (size_t i = 0; i < arr.size(); i++) {
    cout << arr[i] << " ";
  }
  return 0;
}
