# Selection Sort

def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr) - 1):
      
    # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
              
    # Swap the found minimum element with the first element        
        if i != min_idx:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [4, 30, 6, 22, 1, 13]

print(selection_sort(arr))

# Time complexity = O(n^2)

# Space complexity = O(1)