"""
Given an array A[5, 2, 2, 4, 3, 1, 4, 5, 2, 2]
and a sum = 10
return two elements in the array than when added,
can equal the sum
"""
pairs = [5, 2, 2, 4, 3, 1, 4, 5, 2, 2]
pair_sum = 10


def get_pair_with_sum_in_sorted_array(arr, sum):
    """
    Explain here
    """

    left = 0
    right = len(arr) - 1

    while left != right:
        s = arr[left] + arr[right]
        if s == sum:
            return [arr[left], arr[right]]
        elif s < sum:
            print('increasing left')
            left += 1
        else:
            print('decreasing right')
            right -= 1

    return []


def get_pair_with_sum_in_unsorted_array(arr, sum):

    compliments = dict()

    for value in arr:
        s = sum - value
        if compliments.get(s):
            return [value, s]
        else:
            compliments[value] = True

    return []


print(get_pair_with_sum_in_sorted_array(pairs, pair_sum))
print(get_pair_with_sum_in_unsorted_array(pairs, pair_sum))


