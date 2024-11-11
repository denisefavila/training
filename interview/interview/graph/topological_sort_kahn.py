from collections import defaultdict, deque


def topological_sort(graph):
    """
    "A": ["B", "C"], "B": ["D"], "C": [], "D": ["E"], "E": []}
    {'B': 1, 'C': 1, 'D': 1, 'E': 1})
    """
    all_nodes = [node for node in graph]

    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    result = []
    queue = deque()
    for node in all_nodes:
        if in_degree[node] == 0:
            queue.append(node)

    while queue:
        current_node = queue.popleft()
        result.append(current_node)

        next_nodes = graph[current_node]
        for next_node in next_nodes:

            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                queue.append(next_node)

    if len(result) == len(all_nodes):
        return result

    else:
        return []
