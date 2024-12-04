from typing import List


def dutch_flag_partition(pivot_idx: int, arr: List[int]):
    """
    Rearrange arr such that all elements less than arr[pivot_idx]
    appears first, followed by elements equal to the pivot,
    followed by elements greater than pivot

    [0,1,2,0,2,1,1], pivot_idx = 3
    arr[3] = 0 -> [0,0,1,2,2,1,1]
    arr[2] = 2 -> [0,1,0,1,1,2,2], [0,0,1,1,1,2,2]
    """
    pivot_element = arr[pivot_idx]

    # Lower than pivot at the beginning
    last_left_idx = 0
    for idx in range(len(arr)):
        if arr[idx] < pivot_element:
            arr[last_left_idx], arr[idx] = arr[idx], arr[last_left_idx]
            last_left_idx += 1

    # Greater than pivot at the beginning
    last_right_idx = len(arr) - 1
    for idx in range(len(arr) - 1, -1, -1):
        if arr[idx] > pivot_element:
            arr[last_right_idx], arr[idx] = arr[idx], arr[last_right_idx]
            last_right_idx -= 1

    return
