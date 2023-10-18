# 1. Implementation:
# • The swap function, which is used in the provided insertionSort function, is missing. 
# Implement the swap function to make the insertionSort function work correctly.


# def insertionSort(A, n):
#     for pos in range (1, n):
#         nextpos = pos
#         while nextpos > 0 and A[nextpos] < A[nextpos - 1]:
#             swap(A, nextpos, nextpos - 1)
#             nextpos = nextpos - 1
#     return A



def swap(arr, i, j):
    """Helper function to swap elements at positions i and j in the array."""
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def insertionSort(A, n):
    for pos in range(1, n):
        nextpos = pos
        while nextpos > 0 and A[nextpos] < A[nextpos - 1]:
            swap(A, nextpos, nextpos - 1)
            nextpos = nextpos - 1
    return A

# Example:
A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_array = insertionSort(A, len(A))
print(sorted_array)





# 3. Testing:
# • Create a list of unsorted integers.
# • Use the provided insertionSort function to sort this list.
# • Verify and explain if the list was sorted correctly.


unsorted_list = [9, 3, 6, 1, 8, 2, 7, 5, 4]


def insertionSort(A, n):
    for pos in range(1, n):
        nextpos = pos
        while nextpos > 0 and A[nextpos] < A[nextpos - 1]:
            swap(A, nextpos, nextpos - 1)
            nextpos = nextpos - 1
    return A

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

# Sorting the unsorted list using insertionSort function
sorted_list = insertionSort(unsorted_list, len(unsorted_list))

print("Unsorted List:", unsorted_list)
print("Sorted List:", sorted_list)


# Unsorted List: [9, 3, 6, 1, 8, 2, 7, 5, 4]
# Sorted List: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# The insertionSort function has correctly sorted the unsorted_list in ascending order.


