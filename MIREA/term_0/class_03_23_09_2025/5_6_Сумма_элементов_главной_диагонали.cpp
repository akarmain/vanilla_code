#include <iostream>
using namespace std;

int main() {
  cout << "Enter N\n";
  int len_arr, sum_arr = 0;
  cin >> len_arr;
  short arr[len_arr][len_arr];
  for (int i = 0; i < len_arr; i++) {
    for (int j = 0; j < len_arr; j++) {
      if (i == j) {
        sum_arr += arr[i][i];
      }
      cout << arr[i][j] << " ";
    }
    cout << endl;
  }
  cout << "Sum arr: " << sum_arr << endl;
}
