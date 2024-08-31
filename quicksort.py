def quicksort(arr: list[int], left: int, right: int) -> None:
  if left < right:
    partition_pos = partition(arr, left, right)
    quicksort(arr, left, partition_pos - 1)
    quicksort(arr, partition_pos + 1, right)


def partition(arr: list[int], left: int, right: int) -> int:
  i = left
  j = right
  pivot = arr[right]

  while i < j:

    while i < right and arr[i] < pivot:
      i += 1

    while j > left and arr[j] >= pivot:
      j -= 1

    if i < j:
      arr[i], arr[j] = arr[j], arr[i]

  arr[i], arr[right] = arr[right], arr[i]

  return i


arr = [1, 3, 6, 10, 7, 5, 15, 13, 2, 5, 4]
quicksort(arr, 0, len(arr) - 1)
print(arr)
