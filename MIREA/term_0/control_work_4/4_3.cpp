#include <iostream>
#include <vector>
using namespace std;

vector<int> insertion_sort(vector<int> arr, int n) {
  for (size_t i = 1; i < n; i++) {
    int key = arr[i];
    size_t j = i;

    while (j > 0 && arr[j - 1] > key) {
      arr[j] = arr[j - 1];
      j--;
    }

    arr[j] = key;
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

  arr = insertion_sort(arr, len_arr);

  cout << "Sorted massive: " << endl;
  for (size_t i = 0; i < arr.size(); i++) {
    cout << arr[i] << " ";
  }
  return 0;
}
