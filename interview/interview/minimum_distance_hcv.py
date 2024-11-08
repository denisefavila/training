import heapq
from collections import defaultdict
from typing import List


def minimum_distance_hcv(
    num_stops: int,
    credit: List[int],
    num_roads: int,
    roads: List[List[int]],
    source: int,
    destination: int,
) -> int:
    if source == destination:
        return 0

    # Build graph as adjacency list
    graph = defaultdict(list)
    for u, v, dist in roads:
        graph[u].append((v, dist))
        graph[v].append((u, dist))

    # (current_distance, current_node, available_credits)
    queue = [(0, source, credit[source])]
    # Track the best (distance, credits) for each node
    visited = defaultdict(lambda: float("inf"))

    while queue:
        current_distance, current_node, available_credits = heapq.heappop(queue)

        if current_node == destination:
            return current_distance

        if visited[(current_node, available_credits)] <= current_distance:
            continue
        visited[(current_node, available_credits)] = current_distance

        for next_node, road_length in graph[current_node]:
            if available_credits >= road_length:
                new_distance = current_distance + road_length
                new_credits = available_credits - road_length + credit[next_node]

                if visited[(next_node, new_credits)] > new_distance:
                    heapq.heappush(queue, (new_distance, next_node, new_credits))

    return -1
