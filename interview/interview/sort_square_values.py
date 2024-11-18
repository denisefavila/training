def sort_square_values(arr):
    """

    Given a sorted array with positive and negative values,
    sort them based on the square of its values.
    Also, print the squared values array.
    - Expected O(N) working code and interviewer made
        me run the code with sample tests and compare output
    [-7, -2, -1, -1, 1, 2, 2, 2, 3, 5]  # already sorted in a non decreasing order?

    [-1, -1, 1, -2, 2, 2, 2, 3, 5, -7]

    [49,4,1,1,1,4,4,4,9,25], left = 0, right = 8
    [0,0,0,0,0,0,0,0,0,49], left = 0, right = 7
    [0,0,0,0,0,0,0,0,25,49]


    """
