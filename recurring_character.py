"""
Given an array A[1, 2, 3, 3]
return the first recurring character
Example:
    Array A[1, 2, 2, 3] should return 2
    Array B[1, 2, 3, 4] should return None
"""


def return_first_recurring_character(array):
    hash_table = dict()

    for val in array:
        if hash_table.get(val):
            return val
        hash_table[val] = True

    return None


print(return_first_recurring_character([2, 5, 5, 2, 3]))
