#include <iostream>
#include <algorithm>

int partition(int *arr, int left, int right);
void quicksort(int *arr, int left, int right);

int main() {
  int arr[] = {1, 3, 6, 10, 7, 5, 15, 13, 2, 5, 4};
  int size = sizeof(arr) / sizeof(arr[0]);
  quicksort(arr, 0, size);

  for (int item : arr) {
    std::cout << item << "  ";
  }
  std::cout << std::endl;
}


void quicksort(int *arr, int left, int right) {
  if (left < right) {
    int partition_pos = partition(arr, left, right);
    quicksort(arr, left, partition_pos - 1);
    quicksort(arr, partition_pos + 1, right);
  }
}

int partition(int *arr, int left, int right) {
  int i = left;
  int j = right;
  int pivot = arr[right];

  while (i < j) {
    while (i < right && arr[i] < pivot) {
      i += 1;
    }

    while (j > left && arr[j] >= pivot) {
      j -= 1;
    }

    if (i < j) {
      std::swap(arr[i], arr[j]);
      std::cout << "contents swapped" << std::endl
    }
  }

  std::swap(arr[i], arr[right]);
  // std::cout << "Pivot swapped" << std::endl;

  return i;
}
