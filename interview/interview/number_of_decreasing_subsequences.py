from typing import List


def get_number_of_decreasing_subsequences(nums: List[int]):
    """

    Given an int array nums of length n. Split it into strictly decreasing subsequences.
    Output the min number of subsequences you can get by splitting.

    Example 1:

    Input: [5, 2, 4, 3, 1, 6]
    Output: 3

    Example 2:
    Input: [2, 9, 12, 13, 4, 7, 6, 5, 10]
    Output: 4

    Example 3:
    Input: [1, 1, 1]
    Output: 3

    """
    if nums is None or len(nums) == 0:
        return 0

    subsequences = []

    for num in nums:
        if not subsequences:
            subsequences.append(num)
        else:
            index = -1
            start, end = 0, len(subsequences) - 1

            while start <= end:
                mid = (start + end) // 2
                if subsequences[mid] > num:
                    index = mid
                    end = mid - 1
                else:
                    start = mid + 1

            if index != -1:
                subsequences[index] = num
            else:
                subsequences.append(num)

    return len(subsequences)
