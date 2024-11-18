def interesting_pairs(arr, target):
    """

    Given an array of integers arr, an integer sumVal, the task is to pair the elements
    in the arr into interesting pairs. Find the number of interesting pairs in the array .
    An unordered pair (i,j) is defined to be
    interesting if | arr[i] - arr[j] | + | arr[i] + arr[j] | = sumVal (i.e,
    the sum of absolute difference and absolute sum at the values in respective indices
    is equal to sumVal). The goal is to find the number of interesting pairs in the array.

    arr = [1,4,-1,2] ---> [-1,1,2,4]

    | x -  y | + |x + y|

    case1: x >= 0 and y >= 0
        2x

    case1: x <= 0 and y <= 0
        2x



    """
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(arr[i] - arr[j]) + abs(arr[i] + arr[j]) == target:
                count += 1
    return count
