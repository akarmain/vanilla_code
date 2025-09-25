#include <iostream>
#include <limits>
using namespace std;

int main() {
  int len_arr, value_i, max_i = numeric_limits<int>::min(),
                        min_i = numeric_limits<int>::max();
  cout << "Enter count elements of arrey\n";
  cin >> len_arr;
  for (int i = 0; i < len_arr; i++) {
    cout << "enter the value of the element under the number " << i + 1 << endl;
    cin >> value_i;
    if (value_i > max_i) {
      max_i = value_i;
    }
    if (value_i < min_i) {
      min_i = value_i;
    }
  }

  cout << endl << "Max even: " << max_i << endl;
  cout << "Min uneven: " << min_i << endl;
  return 0;
}
