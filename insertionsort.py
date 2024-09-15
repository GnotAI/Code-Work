def insertionSort(arr: list[int]) -> list[int]:
  """
    Insertion sort algorithm that performs sorting of lists through a predetermined set of procedures.

    # Procedures
    - It starts its operations from the second element in the list and checks its value with the element before it.
    - If its value is less than the element, then the values are swapped.
    - However, if the value is greater than the element, then nothing happens to the list.
    - Finally, we move to the next element in the list and repeat the procedures.
  """
  for i in range(1, len(arr)):
    while arr[i - 1] > arr[i] and i > 0:
      arr[i - 1], arr[i] = arr[i], arr[i - 1]
      i -= 1

  print(arr)


insertionSort([2,1,3,6,4,5])
