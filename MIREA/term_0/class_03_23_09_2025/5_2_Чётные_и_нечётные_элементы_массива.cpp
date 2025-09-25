#include <iostream>
using namespace std;

int main() {
  int len_arr, count_even = 0, count_uneven = 0;
  cout << "Enter count elements of arrey\n";
  cin >> len_arr;
  int arr[len_arr];
  for (int i = 0; i < len_arr; i++) {
    cout << "enter the value of the element under the number " << i + 1 << endl;

    cin >> arr[i];
    if (arr[i] % 2 == 0) {
      count_even++;
    } else {
      count_uneven++;
    }
  }

  cout << endl << "Сount even: " << count_even << endl;
  cout << "Сount uneven: " << count_uneven << endl;
  return 0;
}
