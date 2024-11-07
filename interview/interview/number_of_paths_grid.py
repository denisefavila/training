from functools import lru_cache
from typing import List


def unique_paths_with_obstacles(grid: List[List[int]]):
    """
    [0, 0, 0, 0],
    [0, 1, 0, 0]
    [0, 1, 1, 0]
    [0, 0, 0, 0]

    TopDown approach -> recursion + memoization
    1. m = 1, n = 1
        => 1
    2. m = 2, n = 2
        [0,1]
        [0,0]
        => 1
    """
    m, n = len(grid), len(grid[0])

    @lru_cache(None)
    def num_unique_paths(i, j):
        # Get unique paths from (i, j)
        if i >= m or j >= n:
            return 0

        if grid[i][j] == 1:
            return 0

        if i == m - 1 and j == n - 1:
            return 1



        explore_right=num_unique_paths(i, j + 1)
        explore_down=num_unique_paths(i + 1, j)

        return explore_right + explore_down

    return num_unique_paths(0, 0)

def unique_paths(m, n):
    """
    TopDown approach -> recursion + memoization
    1. m = 1, n = 1
        => 1
    2. m = 2, n = 2
        [0,0]
        [0,0]
        => 2
    """

    @lru_cache(None)
    def num_unique_paths(i, j):
        # Get unique paths from (i, j)
        if i == m - 1 and j == n - 1:
            return 1

        if i >= m or j >= n:
            return 0

        explore_right = num_unique_paths(i, j + 1)
        explore_down = num_unique_paths(i + 1, j)

        return explore_right + explore_down

    return num_unique_paths(0, 0)
