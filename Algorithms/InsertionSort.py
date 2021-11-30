# Insertion Sort

# Start with the second item in the list
# Compare second item to the item before it
# Switch if it is less than the item before it
# Move to the next item and do so until you get to the end of the list

def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        temp = arr[i]
        # Move elements of arr[0..i-1], that are greater than temp, to one position ahead of their current position
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            arr[j] = temp
            j -= 1
    
    return arr

arr = [1, 12, 13, 5, 6]

print(insertion_sort(arr))

# Big O = O(n^2)

# Best case when sorted or almost sorted list
# Time complexity then becomes O(n)

# Space complexity = O(1)