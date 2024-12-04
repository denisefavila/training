from typing import List


def three_keys_partition(arr: List[str]):
    """
    Keys take one of three values, reorder the array so that all objects with the same key
    appear together.
    The order of the subarray is not important
    ["A", "B", "C", "A", "B"]
        -> ["A","A", "B", "B", "C"] + variations
    """

    keys = list(set(arr))

