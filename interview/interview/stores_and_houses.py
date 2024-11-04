from typing import List


def find_closest(value: int, nums: List[int]):
    """
    [1,2,5] ->

    """
    # find first greater or equal than

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        current_store = nums[mid]
        if current_store == value:
            return current_store

        elif current_store > value:
            right = mid - 1

        else:
            left = mid + 1

    if right < 0:
        return nums[0]
    elif left >= len(nums):
        return nums[-1]
    else:
        if abs(nums[left] - value) < abs(nums[right] - value):
            return nums[left]
        else:
            return nums[right]


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
