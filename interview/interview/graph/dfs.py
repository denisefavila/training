def dfs_stack(graph):
    # Initialization
    time = 0
    stack = []  # Stack for DFS
    color = {}  # Dictionary to store the color of each vertex
    distances = {}  # Dictionary to store discovery times
    finish_times = {}  # Dictionary to store finish times
    predecessors = {}  # Dictionary to store predecessors

    # Initialize each vertex
    for node in graph:
        color[node] = "WHITE"
        predecessors[node] = None

    # Start DFS for every white vertex in the graph
    for node in graph:
        if color[node] == "WHITE":
            stack.append(node)
            while stack:  # While stack is non-empty
                current_node = stack[-1]  # Look at the top vertex without popping it

                if color[current_node] == "WHITE":  # If it's not visited yet
                    time += 1
                    distances[current_node] = (
                        time  # Set the discovery time for the vertex
                    )
                    color[current_node] = "GRAY"  # Mark as discovered (in process)

                    # Visit all unvisited neighbors of current_node
                    pushed = False
                    for neighbor in graph[current_node]:
                        if color[neighbor] == "WHITE":
                            color[neighbor] = (
                                "GRAY"  # Mark neighbor as discovered (in process)
                            )
                            predecessors[neighbor] = current_node  # Set the predecessor
                            stack.append(neighbor)  # Push the neighbor onto the stack
                            pushed = True

                    if (
                        not pushed
                    ):  # If no neighbors were pushed, we finished exploring the current_node
                        time += 1
                        finish_times[current_node] = (
                            time  # Set the finish time for the vertex
                        )
                        color[current_node] = "BLACK"  # Mark as fully processed
                        stack.pop()  # Pop the vertex from the stack
                else:
                    # If the top vertex is fully processed, pop it
                    stack.pop()

    return distances, predecessors
