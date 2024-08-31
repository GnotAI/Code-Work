def insertionSort(arr: list[int]) -> list[int]:
  for i in range(1, len(arr)):
    while arr[i - 1] > arr[i] and i > 0:
      arr[i - 1], arr[i] = arr[i], arr[i - 1]
      i -= 1

  print(arr)


insertionSort([2,1,3,6,4,5])
