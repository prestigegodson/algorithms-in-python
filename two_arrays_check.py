"""
Given two arrays:
A: [2,4,6,8]
B: [1,3,5,7,8]
write an algorithm that returns True,
if the arrays contains common element
e:g A[1,2,3], B[2,7,6] = TRUE
They both contain 2
"""

array_one = [1, 3, 5, 7, 2]
array_two = [2, 4, 6, 8]


def contains_common_element(array1, array2):
    """
    step 1: loop through array one and save each value
            in a set or dictionary.
    step 2: loop through array2 and check if each item
            in array 2 can be found in the set or dict
    """

    lookup_table = {v for v in array1}

    for v in array2:
        if v in lookup_table:
            return True

    return False


print(contains_common_element(array_one, array_two))