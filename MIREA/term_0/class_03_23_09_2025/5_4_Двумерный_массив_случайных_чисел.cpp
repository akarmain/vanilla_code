#include <iostream>
using namespace std;

int main() {
  cout << "Enter count elements of arrey nober one (N)\n";
  int len_arr_a, len_arr_b;
  cin >> len_arr_a;
  cout << "Enter count elements of arrey nober two (M)\n";
  cin >> len_arr_b;
  short arr[len_arr_a][len_arr_b];
  for (int i = 0; i < len_arr_a; i++) {
    for (int j = 0; j < len_arr_b; j++) {
      cout << arr[i][j] << " ";
    }
    cout << endl;
  }
}
