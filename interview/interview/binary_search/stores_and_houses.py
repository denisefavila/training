import bisect
from typing import List


def find_closest(value: int, nums: List[int]):
    """
    [1,2,5] ->

    """
    # find first greater or equal than
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    if left == 0:
        return nums[0]
    if left == len(nums):
        return nums[-1]

    left_store = nums[left - 1]
    right_store = nums[left]

    if abs(left_store - value) <= abs(right_store - value):
        return left_store
    else:
        return right_store


def find_closest_builtin(value: int, nums: List[int]):
    """
    [1,2,5] ->

    """
    # find first greater or equal than
    pos = bisect.bisect_left(nums, value)

    if pos == 0:
        return nums[0]
    if pos == len(nums):
        return nums[-1]

    left_store = nums[pos - 1]
    right_store = nums[pos]

    if abs(left_store - value) <= abs(right_store - value):
        return left_store
    else:
        return right_store


def get_closest_stores(houses: List[int], stores: List[int]):
    """
    You are given 2 arrays representing integer locations of stores and houses
    (each location in this problem is one-dimensional). For each house, find the store closest to it.
    Return an integer array result where result[i] should denote the location of the store closest
    to the i-th house. If many stores are equidistant from a particular house,
    choose the store with the smallest numerical location. Note that there may
    be multiple stores and houses at the same location.

    Input: houses = [5, 10, 17], stores = [1, 5, 20, 11, 16]
    Output: [5, 11, 16]

    Input: houses = [2, 4, 2], stores = [5, 1, 2, 3]
    Output: [2, 3, 2]

    Input: houses = [4, 8, 1, 1], stores = [5, 3, 1, 2, 6]
    Output: [3, 6, 1, 1]
    """

    if not stores:
        return []

    result = []

    stores.sort()
    for house in houses:
        current_store = find_closest(house, stores)
        result.append(current_store)
    return result
