def detect_cycle(graph):
    def dfs_visit(node):
        nonlocal has_found_cycle

        if visited[node] == 1:  # Cycle detected
            has_found_cycle = True
            return

        visited[node] = 1

        for next_node in graph[node]:
            if visited[next_node] != 2:
                dfs_visit(next_node)

        visited[node] = 2

    nodes = [node for node in graph]

    visited = {node: 0 for node in nodes}  # 0: not visited, 1: visiting, 2: visited

    has_found_cycle = False

    for node in nodes:
        if visited[node] == 0:
            dfs_visit(node)
            if has_found_cycle:
                return True

    return False
