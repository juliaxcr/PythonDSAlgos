# Merge Sort

# Breaks down lists to seperate lists with single item, which is by definition sorted
# Creates new lists by merging and sorting lists.

# Merge is helper function
# Takes two sorted lists and combines them
def merge(arr1, arr2):
    combined = []
    i = j = 0
    # if either list becomes empty then we break out of while loop
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            combined.append(arr1[i])
            i += 1
        else:
            combined.append(arr2[j])
            j += 1
    while i < len(arr1):
        combined.append(arr1[i])
        i += 1
    while j < len(arr2):
        combined.append(arr2[j])
        j += 1

    return combined

# breaks list in half
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = int(len(arr)/2)
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))

print(merge_sort([1, 2, 6, 3, 2, 1, 7, 8, 8, 4, 3]))

# Space Complexity = O(n)

# Breaking apart is O(log n) - merge_sort function
# Putting back together O(n) - merge function
# Time Complexity = O(n log n)

# Less efficient than O(n), more efficient than O(n^2)