from collections import deque
from typing import List


def walls_and_gates(rooms: List[List[int]]) -> None:
    def get_next_positions(i, j):
        """Helper function to get valid neighboring positions."""
        next_positions = []
        movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for di, dj in movements:
            next_i, next_j = i + di, j + dj
            if 0 <= next_i < len(rooms) and 0 <= next_j < len(rooms[0]):
                next_positions.append((next_i, next_j))
        return next_positions

    m = len(rooms)
    n = len(rooms[0])

    queue = deque()
    for i in range(m):
        for j in range(n):
            if rooms[i][j] == 0:
                queue.append((i, j, 0))

    visited = set((i, j) for i, j, _ in queue)

    while queue:
        # process by level
        for _ in range(len(queue)):
            while queue:
                current_i, current_j, current_zeros = queue.popleft()

                rooms[current_i][current_j] = min(
                    rooms[current_i][current_j], current_zeros
                )

                next_positions = get_next_positions(current_i, current_j)
                for next_i, next_j in next_positions:
                    if (next_i, next_j) not in visited:
                        visited.add((next_i, next_j))

                        if rooms[next_i][next_j] != -1:
                            queue.append([next_i, next_j, current_zeros + 1])


def walls_and_gates2(rooms: List[List[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    You are given an m x n grid rooms initialized with these three possible values.

    -1 A wall or an obstacle.
    0 A gate.
    INF Infinity means an empty room.
        We use the value 231 - 1 = 2147483647 to represent INF as you may
        assume that the distance to a gate is less than 2147483647.

    Fill each empty room with the distance to its nearest gate.
    If it is impossible to reach a gate, it should be filled with INF.



    """

    def get_next_positions(i, j):
        next_positions = []
        movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for di, dj in movements:
            next_i, next_j = i + di, j + dj
            if 0 <= next_i < len(rooms) and 0 <= next_j < len(rooms[0]):
                next_positions.append((next_i, next_j))
        return next_positions

    m = len(rooms)
    n = len(rooms[0])

    for i in range(m):
        for j in range(n):
            # Its a gate
            if rooms[i][j] == 0:
                queue = deque([(i, j, 0)])  # (i, j, current_distance)
                visited = {i, j}

                while queue:
                    current_i, current_j, current_zeros = queue.popleft()

                    rooms[current_i][current_j] = min(
                        rooms[current_i][current_j], current_zeros
                    )

                    next_positions = get_next_positions(current_i, current_j)
                    for next_i, next_j in next_positions:
                        if (next_i, next_j) not in visited:
                            visited.add((next_i, next_j))

                            if rooms[next_i][next_j] != -1:
                                queue.append([next_i, next_j, current_zeros + 1])
