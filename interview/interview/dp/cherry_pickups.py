from functools import lru_cache
from typing import List


def cherry_pickups(grid: List[List[int]]) -> int:
    """
    https://leetcode.com/problems/cherry-pickup/description/

    You are given an n x n grid representing a field of cherries,
    each cell is one of three possible integers.

    0 means the cell is empty, so you can pass through,
    1 means the cell contains a cherry that you can pick up and pass through, or
    -1 means the cell contains a thorn that blocks your way.
    Return the maximum number of cherries you can collect by following
        the rules below:

    Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving
    right or down through valid path cells (cells with value 0 or 1).
    After reaching (n - 1, n - 1), returning to (0, 0) by moving left
    or up through valid path cells.
    When passing through a path cell containing a cherry, you pick it up,
    and the cell becomes an empty cell 0.
    If there is no valid path between (0, 0) and (n - 1, n - 1),
    then no cherries can be collected.

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
