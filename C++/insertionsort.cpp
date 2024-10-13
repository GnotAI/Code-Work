#include <iostream>
#include <algorithm> // For std::swap

void insertionSort(int* num, int size) {
  for (int i = 1; i < size; i++) {
    while (i > 0 && num[i - 1] > num[i]) {
      std::swap(num[i - 1], num[i]);
      i--;
    }
  }
}

int main() {
  int arr[] = {2, 1, 3, 5, 4, 6, 11, 50, 8, 10};
  int size = sizeof(arr) / sizeof(arr[0]);  // Calculate array size

  insertionSort(arr, size);

  // Print sorted array
  for (int item : arr) {
    std::cout << item << " ";
  }
  std::cout << std::endl;

  return 0;
}
