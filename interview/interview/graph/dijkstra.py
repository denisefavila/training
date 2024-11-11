from heapq import heappop, heappush


def dijkstra(graph, start):
    """
    Finds the shortest path from a starting node to all other nodes in a weighted graph.

    :param graph: A dictionary where keys are node names and values are dictionaries
                  of neighboring nodes with edge weights.
                  Example: {'A': {'B': 1, 'C': 4}, 'B': {'C': 2, 'D': 5}, ...}
    :param start: The starting node.
    :return: A dictionary where keys are nodes and values are the shortest path distance from start.
    """
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    queue = [(0, start)]
    finished = set()  # Track nodes for which we finalized the shortest path

    while queue:
        current_distance, current_node = heappop(queue)

        if current_node in finished:
            continue

        finished.add(current_node)

        if current_distance > distances[current_node]:
            continue

        for next_node, weight in graph[current_node].items():
            next_distance = current_distance + weight
            if next_distance < distances[next_node]:
                distances[next_node] = next_distance
                heappush(queue, (next_distance, next_node))

    return distances
