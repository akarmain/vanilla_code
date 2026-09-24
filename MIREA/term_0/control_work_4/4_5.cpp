#include <iostream>
#include <vector>
using namespace std;

vector<int> shell_sort(vector<int> arr, int n) {
  for (size_t gap = n / 2; gap > 0; gap /= 2) {
    for (size_t i = gap; i < n; i++) {
      int temp = arr[i];
      size_t j = i;
      while (j >= gap && arr[j - gap] > temp) {
        arr[j] = arr[j - gap];
        j -= gap;
      }
      arr[j] = temp;
    }
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

  arr = shell_sort(arr, len_arr);

  cout << "Sorted massive: " << endl;
  for (size_t i = 0; i < arr.size(); i++) {
    cout << arr[i] << " ";
  }
  return 0;
}
