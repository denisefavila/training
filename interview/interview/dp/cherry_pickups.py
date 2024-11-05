from functools import lru_cache
from typing import List


def cherry_pickups(grid: List[List[int]]) -> int:
    """

    [1,1,-1]
    [1,-1,1]
    [-1,1,1]

    """
    m = len(grid)
    n = len(grid[0])

    @lru_cache(None)
    def explore(i: int, j: int, i2: int, j2: int):

        if i >= m or j >= n or i2 >= m or j2 >= n:
            return float("-inf")

        if grid[i][j] == -1 or grid[i2][j2] == -1:
            return float("-inf")

        if i == i2 and j == j2:
            current_cherry = grid[i][j]
        else:
            current_cherry = grid[i][j] + grid[i2][j2]

        if i == m - 1 and j == n - 1 and i2 == m - 1 and j2 == n - 1:
            return current_cherry

        explore_right_right = explore(i, j + 1, i2, j2 + 1)
        explore_down_down = explore(i + 1, j, i2 + 1, j2)
        explore_right_down = explore(i, j + 1, i2 + 1, j2)
        explore_down_right = explore(i + 1, j, i2, j2 + 1)

        return current_cherry + max(
            explore_right_right,
            explore_down_down,
            explore_right_down,
            explore_down_right,
        )

    result = explore(0, 0, 0, 0)

    return max(0, result)
