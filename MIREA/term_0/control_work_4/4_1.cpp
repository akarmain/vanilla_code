#include <iostream>
#include <vector>
using namespace std;

vector<int> bubble_sorting(vector<int> arr, int n) {
  bool swapped;
  do {
    swapped = false;
    for (int i = 0; i < n - 1; i++) {
      if (arr[i] > arr[i + 1]) {
        swap(arr[i], arr[i + 1]);
        swapped = true;
      }
    }
    n--;
  } while (swapped);
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

  arr = bubble_sorting(arr, len_arr);

  cout << "Sorted massive: " << endl;
  for (size_t i = 0; i < arr.size(); i++) {
    cout << arr[i] << " ";
  }
  return 0;
}
