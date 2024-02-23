# linear search

def linear_search(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return -1
# main
list1 = [1, 2, 3, 4, 5]
target = 3
print(linear_search(list1, target))
