#include <iostream>
#include <algorithm> // For std::swap

void insertionSort(int* num, int size) {
  for (int i = 1; i < size; i++) {
    int j = i;
    while (j > 0 && num[j - 1] > num[j]) {
      std::swap(num[j - 1], num[j]);
      j--;
    }
  }
}

int main() {
  int arr[] = {2, 1, 3, 5, 4, 6, 11, 50, 8, 10};
  int size = sizeof(arr) / sizeof(arr[0]);  // Calculate array size

  insertionSort(arr, size);

  // Print sorted array
  for (int i = 0; i < size; i++) {
    std::cout << arr[i] << " ";
  }
  std::cout << std::endl;

  return 0;
}
