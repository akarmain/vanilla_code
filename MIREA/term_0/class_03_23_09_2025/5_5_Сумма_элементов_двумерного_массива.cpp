#include <iostream>
using namespace std;

int main() {
  int len_arr_a, len_arr_b, sum_arr, cin_i;

  cout << "Enter count elements of arrey nober one (N)\n";
  cin >> len_arr_a;
  cout << "Enter count elements of arrey nober two (M)\n";
  cin >> len_arr_b;
  cout << "Enter elements of arrey\n";

  short arr[len_arr_a][len_arr_b];
  for (int i = 0; i < len_arr_a + len_arr_a; i++) {
    cin >> cin_i;
    sum_arr += cin_i;
  }
  cout << "Sum: " << sum_arr;
}
