#include <iostream>
#include <vector>
using namespace std;

vector<int> insertion_sort_binary(vector<int> arr, size_t n) {
  for (size_t i = 1; i < n; i++) {
    int key = arr[i];
    size_t left = 0;
    size_t right = i;
    while (left < right) {
      size_t mid = left + (right - left) / 2;
      if (arr[mid] <= key) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }

    size_t pos = left;
    for (size_t j = i; j > pos; j--) {
      arr[j] = arr[j - 1];
    }

    arr[pos] = key;
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

  arr = insertion_sort_binary(arr, len_arr);

  cout << "Sorted massive: " << endl;
  for (size_t i = 0; i < arr.size(); i++) {
    cout << arr[i] << " ";
  }
  return 0;
}
