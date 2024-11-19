from heapq import heappop, heappush


def dijkstra(graph, start):
    """
    Finds the shortest path from a starting node to all other nodes in a weighted graph.
    """
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    queue = [(0, start)]

    while queue:
        current_distance, current_node = heappop(queue)

        for next_node, weight in graph[current_node].items():
            next_distance = current_distance + weight
            if next_distance < distances[next_node]:
                distances[next_node] = next_distance
                heappush(queue, (next_distance, next_node))

    return distances
