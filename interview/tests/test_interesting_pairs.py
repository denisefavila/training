from interview.interview.interesting_pairs import interesting_pairs


def test_case_1():
    arr = [1, 4, -1, 2]
    target = 4
    assert interesting_pairs(arr, target) == 2


# Test case 2
def test_case_2():
    arr = [1, 3, 2, 0]
    target = 2
    assert interesting_pairs(arr, target) == 1


# Test case 3
def test_case_3():
    arr = [1, 3, 2, 0]
    target = 3
    assert interesting_pairs(arr, target) == 0


# Test case 4: Edge case with no pairs
def test_case_4():
    arr = [1, 2, 3]
    target = 100
    assert interesting_pairs(arr, target) == 0


# Test case 5: All elements are the same
def test_case_5():
    arr = [2, 2, 2, 2]
    target = 4
    assert interesting_pairs(arr, target) == 6


# Test case 6: Single element array
def test_case_6():
    arr = [5]
    target = 5
    assert interesting_pairs(arr, target) == 0


# Test case 7: Large input with random values
def test_case_7():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    target = 10
    assert interesting_pairs(arr, target) == 4
