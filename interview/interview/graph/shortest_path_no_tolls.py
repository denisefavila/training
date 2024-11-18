import heapq
from typing import Dict


def shortest_path_no_tolls(graph: Dict[str, tuple], start: str, end: str):
    """
    graph = {
        'A': [('B', 2, False), ('C', 4, True)],
        'B': [('A', 2, False), ('C', 1, False), ('D', 7, False)],
        'C': [('A', 4, True), ('B', 1, False), ('D', 3, False)],
        'D': [('B', 7, False), ('C', 3, False)]
    }

    """

    distances = {node: float("inf") for node in graph.keys()}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        for next_node, delta_distance, is_toll in graph[current_node]:
            next_distance = current_distance + delta_distance
            if next_distance < distances[next_node] and not is_toll:
                distances[next_node] = next_distance
                heapq.heappush(priority_queue, (next_distance, next_node))

    return distances[end] if end in distances and distances[end] != float("inf") else -1
