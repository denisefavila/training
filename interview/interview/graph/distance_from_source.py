from collections import deque


def min_distance_from_source(graph, source):
    """
    # non directed graph

    graph_1 = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2],
    }"

    """

    distances = {node: float("inf") for node in graph}

    predecessors = {node: None for node in graph}

    distances[source] = 0

    queue = deque()
    visited = set()

    queue.append((source, 0))
    visited.add(source)

    while queue:
        current_node, current_path_size = queue.popleft()

        distances[current_node] = current_path_size

        next_nodes = graph[current_node]

        for next_node in next_nodes:
            if next_node not in visited:
                new_path_size = current_path_size + 1
                predecessors[next_node] = current_node
                queue.append((next_node, new_path_size))
                visited.add(next_node)

    return distances, predecessors
