"""
Given two sorted arrays:
Array1 [0, 3, 4, 5]
Array2 [6, 7, 30]
return a single sorted array
"""


def merge_sorted_arrays(array1, array2):
    """
    step 1: if array 1 is empty return second array
            else if array 2 is empty return first array
    step 2 : declare two variables left and right that holds the current index of array1 and array2
            left index keep track of left array
            right index keeps track of right array
    step 3: declare a variable merged_sorted_array that holds the new sorted array
    step 4: while left index is less than array1 length or right index is less than array2 length
                if left index is equal to length of array 1
                   add the value at right index of array 2 to the merged_sorted_array
                   increment right index
                else if right index is equal to length of array 2
                    add value at left index of array 1 to the merged_sorted_array
                    increment left index
                else if array1[left] <= array2[right]:
                    add value at left index of array 1 to the merged_sorted_array
                    increment left index
                else:
                    add the value at right index of array 2 to the merged_sorted_array
                   increment right index
    """

    if not array1:
        print('return array 2')
        return array2
    elif not array2:
        print('return array 1')
        return array1

    left = 0
    right = 0
    merged_sorted_array = []
    left_length = len(array1)
    right_length = len(array2)

    while left < left_length or right < right_length:
        if left == left_length:
            merged_sorted_array.append(array2[right])
            right += 1
        elif right == right_length:
            merged_sorted_array.append(array1[left])
            left += 1
        elif array1[left] <= array2[right]:
            merged_sorted_array.append(array1[left])
            left += 1
        else:
            merged_sorted_array.append(array2[right])
            right += 1

    return merged_sorted_array


array1 = [1, 2, 3, 4, 11]
array2 = [2, 4, 6, 8, 10, 50]
print(array1)
print(array2)
print(merge_sorted_arrays(array1, []))
