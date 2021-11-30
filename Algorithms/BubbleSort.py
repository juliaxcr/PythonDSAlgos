# Bubble Sort

# Start with first item in list and compare to second item, take second item and compare to third item, etc... Switching when necessary.
# Do this process again until all items are sorted.

def bubble_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]

print(bubble_sort(arr))