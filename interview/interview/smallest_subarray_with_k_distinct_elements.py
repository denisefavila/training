from collections import defaultdict
from typing import List


def smallest_subarray_with_k_distinct(arr: List[int], k: int) -> List[int]:
    """
    [1, 2, 2, 3, 1, 3 ]
    *
    counter = {}
    min_subarray = []

    """
    # Write your code here.

    left, right = 0, 0
    counter = defaultdict(int)

    min_subarray = []
    min_length = float("inf")

    while right < len(arr):
        current_num = arr[right]
        counter[current_num] += 1

        while len(counter) == k:
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_subarray = [left, right]

            to_remove_num = arr[left]
            counter[to_remove_num] -= 1
            if counter[to_remove_num] == 0:
                del counter[arr[left]]
            left -= 1

        right += 1

    return min_subarray if min_subarray else []
