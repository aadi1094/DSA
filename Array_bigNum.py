def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0], find_max(arr[1:]))

# Example usage
array = [5, 9, 3, 1, 7]
max_element = find_max(array)
print("The biggest element in the array is:", max_element)

# Find the index of the biggest element in the array
max_index = array.index(max_element)
print("The index of the biggest element in the array is:", max_index)