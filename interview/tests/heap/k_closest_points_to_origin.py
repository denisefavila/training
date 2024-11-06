from interview.interview.heap.k_closest_points_to_origin import \
    get_k_closest_points_to_origin


def test_k_closest():
    # Test case 1: Basic input with unique closest points
    points1 = [[1, 2], [2, 3], [3, 4], [4, 5]]
    k1 = 2
    expected1 = [[1, 2], [2, 3]]  # The 2 closest points to (0, 0)
    assert sorted(get_k_closest_points_to_origin(points1, k1)) == sorted(expected1)

    # Test case 2: Including points at the same distance from the origin
    points2 = [[1, 1], [1, -1], [-1, 1], [-1, -1], [2, 2]]
    k2 = 3
    expected2 = [[1, 1], [1, -1], [-1, 1]]  # Any combination of 3 closest points
    assert sorted(get_k_closest_points_to_origin(points2, k2)) == sorted(expected2)

    # Test case 3: When k equals the number of points
    points3 = [[3, 3], [5, -1], [-2, 4]]
    k3 = 3
    expected3 = [[3, 3], [5, -1], [-2, 4]]  # All points should be returned
    assert sorted(get_k_closest_points_to_origin(points3, k3)) == sorted(expected3)

    # Test case 4: Multiple points at the same distance from origin
    points4 = [[1, 2], [2, 1], [-1, -2], [-2, -1], [2, 2]]
    k4 = 2
    expected4 = [[1, 2], [2, 1]]  # Any two points at the same distance
    assert sorted(get_k_closest_points_to_origin(points4, k4)) == sorted(expected4)

    # Test case 5: Edge case with no points
    points5 = []
    k5 = 0
    expected5 = []  # No points to return
    assert get_k_closest_points_to_origin(points5, k5) == expected5

    # Test case 6: Edge case with negative coordinates
    points6 = [[-1, -1], [-2, -2], [1, 1], [2, 2]]
    k6 = 2
    expected6 = [[-1, -1], [1, 1]]  # Closest points with negative coordinates
    assert sorted(get_k_closest_points_to_origin(points6, k6)) == sorted(expected6)

    # Test case 7: Distance calculation check
    points7 = [[0, 3], [4, 0], [3, 4], [0, 0]]
    k7 = 1
    expected7 = [[0, 0]]  # The closest point to the origin
    assert sorted(get_k_closest_points_to_origin(points7, k7)) == sorted(expected7)

    # Test case 8: Points that are exactly on the axes
    points8 = [[0, 5], [5, 0], [-5, 0], [0, -5]]
    k8 = 2
    expected8 = [[0, 5], [5, 0]]  # Two closest points on the axes
    assert sorted(get_k_closest_points_to_origin(points8, k8)) == sorted(expected8)
