#include <iostream>
#include <vector>
using namespace std;

int main() {
  int n;
  cout << "Enter the size of the array:";
  cin >> n;

  vector<int> arr(n);
  cout << "Enter the array elements:\n";
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }

  // Новый массив без нулей
  vector<int> result;
  for (int x : arr) {
    if (x != 0)
      result.push_back(x);
  }

  cout << "An array without zeros:\n";
  if (result.empty()) {
    cout << "All the elements were zeros, the array is empty.\n";
  } else {
    for (int x : result)
      cout << x << " ";
    cout << "\n";
  }

  return 0;
}
