def get_or(intervals1, intervals2):
    """
    intervals1 = [(2, 4), (6, 8), (1, 3)] -> [(1, 3), (2, 4), (6, 8)]
    intervals2 = [(7, 9), (2, 5)] -> [(2, 5), (7, 9)]
    expected_union = [(1, 5), (6, 9)]

    # merge intervals

    """

    def add_interval(start, end):
        if not result or start > result[-1][1]:
            result.append((start, end))
        else:
            # merge
            last_start, last_end = result[-1]
            result[-1] = (last_start, max(last_end, end))

    intervals1.sort()
    intervals2.sort()

    result = []

    i, j = 0, 0
    while i < len(intervals1) and j < len(intervals2):
        start_1, end_1 = intervals1[i]
        start_2, end_2 = intervals2[j]
        if start_1 < start_2:
            add_interval(start_1, end_1)
            i += 1

        else:
            add_interval(start_2, end_2)
            j += 1

    while i < len(intervals1):
        current_start, current_end = intervals1[i]
        add_interval(current_start, current_end)
        i += 1

    while j < len(intervals2):
        current_start, current_end = intervals2[j]
        add_interval(current_start, current_end)
        j += 1

    return result


def get_and(intervals1, intervals2):
    """

    intervals1 = [(2, 4), (6, 8), (1, 3)] -> [(1, 3), (2, 4), (6, 8)]
    intervals2 = [(7, 9), (2, 5)] -> [(2, 5), (7, 9)]
    expected_intersection = ??

    """
    result = []
    i, j = 0, 0

    while i < len(intervals1) and j < len(intervals2):
        start_1, end_1 = intervals1[i]
        start_2, end_2 = intervals2[j]

        overlap_start = max(start_1, start_2)
        overlap_end = min(end_1, end_2)

        if overlap_start <= overlap_end:  # Valid intersection
            result.append([overlap_start, overlap_end])

        if end_1 < end_2:
            i += 1
        else:
            j += 1

    return result
