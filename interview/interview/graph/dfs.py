def dfs(graph):
    def dfs_visit(node):
        nonlocal time
        time += 1

        distances[node] = time
        visited.add(node)

        for next_node in graph[node]:
            if next_node not in visited:
                predecessors[next_node] = node
                dfs_visit(next_node)
        time += 1
        finish_times[node] = time

    distances = {node: None for node in graph}
    finish_times = {node: None for node in graph}
    predecessors = {node: None for node in graph}

    visited = set()

    time = 0
    for node in graph:
        if node not in visited:
            dfs_visit(node)

    return distances, finish_times, predecessors
