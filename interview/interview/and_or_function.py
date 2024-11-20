def get_or(intervals1, intervals2):
    """
    intervals1 = [(2, 4), (6, 8), (1, 3)] -> [(1, 3), (2, 4), (6, 8)]
    intervals2 = [(7, 9), (2, 5)] -> [(2, 5), (7, 9)]
    expected_union = [(1, 5), (6, 9)]

    # merge intervals

    """
    intervals1.sort()
    intervals2.sort()

    result = []

    i, j = 0, 0
    while i < len(intervals1) and j < len(intervals2):
        start_1, end_1 = intervals1[i]
        start_2, end_2 = intervals2[j]
        if start_1 < start_2:
            current_start, current_end = start_1, end_1
            i += 1

        else:
            current_start, current_end = start_2, end_2
            j += 1

        if not result or current_start > result[-1][1]:
            result.append((current_start, current_end))
        else:
            # merge
            last_start, last_end = result[-1]
            result[-1] = (last_start, max(last_end, current_end))

    while i < len(intervals1):
        current_start, current_end = intervals1[i]
        if not result or current_start > result[-1][1]:
            result.append((current_start, current_end))
        else:
            # merge
            last_start, last_end = result[-1]
            result[-1] = (last_start, max(last_end, current_end))
        i += 1

    while j < len(intervals2):
        current_start, current_end = intervals2[j]
        if not result or current_start > result[-1][1]:
            result.append((current_start, current_end))
        else:
            # merge
            last_start, last_end = result[-1]
            result[-1] = (last_start, max(last_end, current_end))

        j += 1

    return result


def get_and(intervals1, intervals2):
    """

    intervals1 = [(2, 4), (6, 8), (1, 3)] -> [(1, 3), (2, 4), (6, 8)]
    intervals2 = [(7, 9), (2, 5)] -> [(2, 5), (7, 9)]
    expected_intersection = ??



    """
    ...
