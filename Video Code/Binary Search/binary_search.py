# binary search

def binary_search(arr, target):
  left = 0
  right = len(arr) - 1
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return -1

# main
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
target = 3
print(binary_search(list1, target))