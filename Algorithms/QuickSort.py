# Quick Sort

# Start with pivot point, which is first item
# Looks at next two items and sees whether they are greater or less than
# Seperates everything less than and everything greater than

# swaps
def swap(arr, idx1, idx2):
    temp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = temp

# pivot helper function
# places all less than values to the left of the pivot and all greater than values to the right of the pivot
def pivot(arr, pivot_idx, end_idx):
    swap_idx = pivot_idx

    for i in range(pivot_idx + 1, end_idx + 1):
        if arr[i] < arr[pivot_idx]:
            swap_idx += 1
            swap(arr, swap_idx, i)

    swap(arr, pivot_idx, swap_idx)
    # returns middle/pivot index
    return swap_idx

def quick_sort_helper(arr, left, right):
    if left < right:
        pivot_idx = pivot(arr, left, right)
        quick_sort_helper(arr, left, pivot_idx - 1)
        quick_sort_helper(arr, pivot_idx + 1, right)
    return arr

def quick_sort(arr):
    return quick_sort_helper(arr, 0, len(arr) - 1)

arr = [4, 6, 1, 7, 3, 2, 5]

print(quick_sort(arr))

# Pivot function has for loop
# O(n)
# Recursion is 0(log n)

# Time complexity for best and average case: 0(n log n)

# Pivot function runs on every single item (n times)
# Big O (for already sorted data, which is the worst case): O(n^2)
# Better to use insertion sort then