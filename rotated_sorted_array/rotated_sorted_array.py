arr = [14, 15, 16, 17, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def rotated_search(arr, key):
    left = 0
    right = len(arr) - 1
    while left <= right:
        middle = left + ((right - left)/2)
        if arr[middle] == key:
            return middle
        if arr[left] <= arr[middle]:
            if arr[left] <= key < arr[middle]:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if arr[middle] < key <= arr[right]:
                left = middle + 1
            else:
                right = middle - 1
    return -1

print rotated_search(arr, 11)


def find_pivot(arr):
    # This is the same problem as the above one, but in this you have to find
    # the minimum element index.
    left = 0
    right = len(arr) - 1
    while arr[left] > arr[right]:
        middle = left + ((right - left)/2)
        if arr[middle] > arr[right]:
            left = middle + 1
        else:
            right = middle
    return left

print find_pivot(arr)

