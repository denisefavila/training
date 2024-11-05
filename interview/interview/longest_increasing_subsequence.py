from functools import lru_cache
from typing import List


def longest_increasing_subsequence(nums: List[int]) -> int:
    if not nums:
        return 0

    n = len(nums)

    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def longest_increasing_subsequence_memo(nums: List[int]) -> int:
    @lru_cache(None)
    def explore(idx):
        if idx >= len(nums):
            return 0

        max_length = 1
        for next_idx in range(idx + 1, len(nums)):
            if nums[next_idx] > nums[idx]:
                max_length = max(max_length, 1 + explore(next_idx))

        return max_length

    longest_increasing_length = 0
    for i in range(len(nums)):
        current_size = explore(i)
        longest_increasing_length = max(longest_increasing_length, current_size)

    return longest_increasing_length
