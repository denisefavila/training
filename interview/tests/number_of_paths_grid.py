from interview.interview.number_of_paths_grid import (
    unique_paths,
    unique_paths_with_obstacles,
)


def test_unique_paths_with_obstacles():
    # Test case where the grid is 1x1 and there is no obstacle
    assert unique_paths_with_obstacles([[0]]) == 1

    # Test case where the grid is 1x1 with an obstacle
    assert unique_paths_with_obstacles([[1]]) == 0

    # Test a 2x2 grid with no obstacles
    grid = [[0, 0], [0, 0]]
    assert unique_paths_with_obstacles(grid) == 2  # There are 2 paths

    # Test a 3x3 grid with no obstacles
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert unique_paths_with_obstacles(grid) == 6  # There are 6 paths

    # Test a 3x3 grid with obstacles
    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert unique_paths_with_obstacles(grid) == 2  # Only two paths available

    # Test a 3x3 grid where the path is blocked completely
    grid = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
    assert unique_paths_with_obstacles(grid) == 0  # No paths available

    # Test case where obstacles are only on one side (right)
    grid = [[0, 1, 0], [0, 1, 0], [0, 0, 0]]
    assert (
        unique_paths_with_obstacles(grid) == 1
    )  # Only one path from top-left to bottom-right

    # Test a 4x4 grid with obstacles scattered
    grid = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    assert unique_paths_with_obstacles(grid) == 3  # There are 3 possible paths

    # Test a large grid (5x5) with a few obstacles
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    assert unique_paths_with_obstacles(grid) == 8  # There are 8 possible paths


def test_unique_paths():
    # Test 1x1 grid
    assert unique_paths(1, 1) == 1

    # Test single row grid (1x5)
    assert unique_paths(1, 5) == 1

    # Test single column grid (5x1)
    assert unique_paths(5, 1) == 1

    # Test 2x2 grid
    assert (
        unique_paths(2, 2) == 2
    )  # Possible paths: (0,0) -> (0,1) -> (1,1) and (0,0) -> (1,0) -> (1,1)

    # Test 3x3 grid
    assert (
        unique_paths(3, 3) == 6
    )  # Paths: (0,0)->(0,1)->(0,2)->(1,2)->(2,2) and other combinations

    # Test 3x2 grid
    assert unique_paths(3, 2) == 3  # Paths: (0,0) -> (1,0) -> (2,0) -> (2,1) and others

    # Test larger grids
    assert unique_paths(7, 3) == 28
    assert unique_paths(3, 7) == 28

    # Test 10x10 grid for a larger number of paths
    assert unique_paths(10, 10) == 48620

    # Test edge case of a large grid (e.g., 15x15)
    assert unique_paths(15, 15) == 40116600
