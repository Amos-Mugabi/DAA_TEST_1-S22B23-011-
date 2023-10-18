
# 1. Write the pseudocode and the actual code for the find_max() function in your preferred 
# programming language.

# The pseudocode.
# function find_max(arr):
#     max = arr[0]  // Initialize max to the first element of the array
#     for i from 1 to length(arr) - 1:  // Iterate over the array starting from the second element
#         if arr[i] > max:  // Compare the current element to max
#             max = arr[i]  // Update max if the current element is greater
#     return max  // Return the maximum element found in the array


def find_max(arr):
    max_element = arr[0]  # Initialize max to the first element of the array
    for i in range(1, len(arr)):  # Iterate over the array starting from the second element
        if arr[i] > max_element:  # Compare the current element to max
            max_element = arr[i]  # Update max if the current element is greater
    return max_element  # Return the maximum element found in the array

# Example usage
array = [3, 7, 1, 9, 5]
maximum_element = find_max(array)
print("Maximum element in the array is:", maximum_element)




# 2. Test the find_max() function with a variety of different arrays, including empty arrays, arrays 
# with a single element, and arrays with multiple elements.


def find_max(arr):
    if len(arr) == 0:
        return None  # Return None for empty arrays
    max_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
    return max_element



# Test with different arrays
arrays = [
    [],                    # Empty array
    [5],                   # Array with a single element
    [1, 2, 3, 4, 5],       # Array with ascending elements
    [5, 4, 3, 2, 1],       # Array with descending elements
    [3, 1, 7, 2, 8],       # Array with unsorted elements
    [-1, -5, -3, -2, -4]   # Array with negative elements
]

for array in arrays:
    max_element = find_max(array)
    if max_element is None:
        print("Maximum element in the empty array is None")
    else:
        print("Maximum element in the array", array, "is:", max_element)

