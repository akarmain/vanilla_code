#include <chrono>
#include <iostream>
#include <vector>
using namespace std;
using namespace std::chrono;

vector<int> bubble_sorting(vector<int> arr, size_t n) {
  bool swapped;
  do {
    swapped = false;
    for (size_t i = 0; i < n - 1; i++) {
      if (arr[i] > arr[i + 1]) {
        swap(arr[i], arr[i + 1]);
        swapped = true;
      }
    }
    n--;
  } while (swapped);
  return arr;
}

vector<int> shaker_sorting(vector<int> arr, size_t n) {
  size_t left = 0;
  size_t right = n - 1;

  while (left < right) {
    for (size_t i = left; i < right; i++) {
      if (arr[i] > arr[i + 1]) {
        swap(arr[i], arr[i + 1]);
      }
    }
    right--;

    for (size_t i = right; i > left; i--) {
      if (arr[i] < arr[i - 1]) {
        swap(arr[i], arr[i - 1]);
      }
    }
    left++;
  }

  return arr;
}

vector<int> insertion_sort(vector<int> arr, size_t n) {
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

vector<int> selection_sort(vector<int> arr, size_t n) {
  for (size_t i = 0; i < n - 1; i++) {
    size_t min_index = i;
    for (size_t j = i + 1; j < n; j++) {
      if (arr[j] < arr[min_index]) {
        min_index = j;
      }
    }
    if (min_index != i) {
      swap(arr[i], arr[min_index]);
    }
  }
  return arr;
}

vector<int> shell_sort(vector<int> arr, size_t n) {
  for (size_t gap = n / 2; gap > 0; gap /= 2) {
    for (size_t i = gap; i < n; i++) {
      int temp = arr[i];
      size_t j = i;
      while (j >= gap && arr[j - gap] > temp) {
        arr[j] = arr[j - gap];
        j -= gap;
      }
      arr[j] = temp;
    }
  }
  return arr;
}

vector<int> gnome_sort(vector<int> arr, size_t n) {
  size_t i = 1;

  while (i < n) {
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
  const size_t SMALL = 10;
  const size_t BIG = 50000;
  srand(0);
  vector<int> base_small(SMALL);
  vector<int> base_big(BIG);
  for (size_t i = 0; i < SMALL; i++) {
    base_small[i] = rand() % 1000;
  }
  for (size_t i = 0; i < BIG; i++) {
    base_big[i] = rand() % 100000;
  }

  auto measure =
      [](const string &name, vector<int> (*sort_func)(vector<int>, size_t),
         const vector<int> &base_small, const vector<int> &base_big) {
        vector<int> arr_small = base_small;
        vector<int> arr_big = base_big;

        auto start_small = high_resolution_clock::now();
        arr_small = sort_func(arr_small, arr_small.size());
        auto end_small = high_resolution_clock::now();

        auto start_big = high_resolution_clock::now();
        arr_big = sort_func(arr_big, arr_big.size());
        auto end_big = high_resolution_clock::now();

        auto dur_small =
            duration_cast<microseconds>(end_small - start_small).count();
        auto dur_big = duration_cast<microseconds>(end_big - start_big).count();

        cout << name << ":\n";
        cout << "  small (" << base_small.size() << "): " << dur_small
             << " microseconds\n";
        cout << "  big   (" << base_big.size() << "): " << dur_big
             << " microseconds\n\n";
      };

  cout << "Timing different sorting algorithms on the same arrays\n\n";

  measure("Bubble sort", bubble_sorting, base_small, base_big);
  measure("Shaker sort", shaker_sorting, base_small, base_big);
  measure("Insertion sort", insertion_sort, base_small, base_big);
  measure("Selection sort", selection_sort, base_small, base_big);
  measure("Shell sort", shell_sort, base_small, base_big);
  measure("Gnome sort", gnome_sort, base_small, base_big);

  return 0;
}
