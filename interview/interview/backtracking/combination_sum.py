def combination_sum(arr, target):
    """
    [2, 3, 6, 7], 7
    """
    combinations = []

    def backtracking(idx, current_combination, current_combination_sum):
        if current_combination_sum == target:
            combinations.append(current_combination.copy())
            return

        if idx >= len(arr) or current_combination_sum > target:
            return

        current_number = arr[idx]

        # use current number
        current_combination.append(current_number)
        backtracking(idx, current_combination, current_combination_sum + current_number)
        current_combination.pop()

        # dont use current number
        backtracking(idx + 1, current_combination, current_combination_sum)

    backtracking(0, [], 0)
    return combinations
