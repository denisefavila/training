from collections import deque
from heapq import heappop, heappush


def broadcast_message(routers, source, destination, distance):
    """
    {
        0: [(1, 5), (2, 10)],
        1: [(0, 5), (3, 8)],
        2: [(0, 10), (3, 2)],
        3: [(1, 8), (2, 2)],
    }
    src = 0
    des = 3
    d = 10
    """

    # BFS with weight (Dikstra) from source to destination
    #   -> get the distance -> check if the distance if lower
    # than target distance

    queue = []
    distances = {node: float("inf") for node in routers}
    visited = set()

    # Start with the source node
    heappush(queue, (0, source))  # Push the source node with distance 0
    distances[source] = 0

    while queue:
        current_distance, current_node = heappop(queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        # Explore the neighbors
        for next_node, next_distance in routers.get(current_node, []):
            new_distance = current_distance + next_distance
            if new_distance < distances[next_node]:
                distances[next_node] = new_distance
                heappush(queue, (new_distance, next_node))

    return distances[destination] <= distance
