#include <iostream>
#include <vector>
using namespace std;

vector<int> gnome_sort(vector<int> arr, int n) {
  size_t i = 1;

  while (i < (size_t)n) {
    if (i > 0 && arr[i] < arr[i - 1]) {
      int temp = arr[i];
      arr[i] = arr[i - 1];
      arr[i - 1] = temp;
      i--;
    } else {
      i++;
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

  arr = gnome_sort(arr, len_arr);

  cout << "Sorted massive: " << endl;
  for (size_t i = 0; i < arr.size(); i++) {
    cout << arr[i] << " ";
  }

  return 0;
}
