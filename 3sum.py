"""
Given a sorted array A[-2, -1, -1, 0, 1, 2, 3],
and a sum = 0
return 3 pairs of numbers that when added will equal th sum
"""


def get_3_pairs(array, sum):
    left = 0
    right = len(array) - 1
    pairs = []

    dicts = set(val for val in array)

    while left < right:
        val = array[left] + array[right]
        sums = sum - val

        if sums in dicts:
            pairs.append([sums, array[left], array[right]])

        if array[left] < array[right]:
            left += 1
        else:
            right += 1

    return pairs


print(get_3_pairs([-2, -1, 0, 1, 2, 3], 2))
