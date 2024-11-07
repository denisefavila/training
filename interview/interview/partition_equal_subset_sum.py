from functools import lru_cache


def can_partition(nums):
    """
    TopDown -> Recursion + Memoization
    nums = [1,5,11,5]
    total_sum = 22, target_sum = total_sum // 2, if odd -> False

    validPartition(current_sum=0)

    """

    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False

    target_sum = total_sum // 2

    n = len(nums) - 1

    @lru_cache(None)
    def valid_partition(idx, remaining_sum):
        if remaining_sum == 0:
            return True

        if remaining_sum < 0 or idx == 0:
            return False

        current_number = nums[idx]
        add_current_number_to_set = valid_partition(
            idx - 1, remaining_sum - current_number
        )
        dont_add_current_number_to_set = valid_partition(idx - 1, remaining_sum)

        return add_current_number_to_set or dont_add_current_number_to_set

    return valid_partition(n, target_sum)


def can_partition_up(nums):
    """
    TopDown -> Recursion + Memoization
    nums = [1,5,11,5]
    total_sum = 22, target_sum = total_sum // 2, if odd -> False

    validPartition(current_sum=0)

    """

    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False

    target_sum = total_sum // 2

    @lru_cache(None)
    def valid_partition(idx, current_sum):
        if current_sum == target_sum:
            return True if current_sum == target_sum else 0

        if current_sum > target_sum:
            return False

        if idx >= len(nums):
            return False

        current_number = nums[idx]
        add_current_number_to_set = valid_partition(
            idx + 1, current_sum + current_number
        )
        dont_add_current_number_to_set = valid_partition(idx + 1, current_sum)

        return add_current_number_to_set or dont_add_current_number_to_set

    return valid_partition(0, 0)
