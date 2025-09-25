#include <iostream>
using namespace std;

int main() {
  cout << "Enter count elements of arrey\n";
  int len_arr, medium;
  medium = 0;
  cin >> len_arr;
  short arr[len_arr];
  for (int i = 0; i < len_arr; i++) {
    cout << arr[i] << " ";
    medium += arr[i];
  }
  cout << endl << "medium: " << medium / len_arr;
}
