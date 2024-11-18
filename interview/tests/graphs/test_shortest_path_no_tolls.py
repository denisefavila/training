from interview.interview.graph.shortest_path_no_tolls import shortest_path_no_tolls


def test_shortest_path_no_tolls():
    # Example graph: adjacency list representation
    # Each edge is (neighbor, weight, is_toll)
    graph = {
        "A": [("B", 2, False), ("C", 4, True)],
        "B": [("A", 2, False), ("C", 1, False), ("D", 7, False)],
        "C": [("A", 4, True), ("B", 1, False), ("D", 3, False)],
        "D": [("B", 7, False), ("C", 3, False)],
    }

    # Test cases
    assert shortest_path_no_tolls(graph, "A", "D") == 6  # A -> B -> C -> D
    assert shortest_path_no_tolls(graph, "A", "C") == 3  # A -> B -> C
    assert shortest_path_no_tolls(graph, "A", "A") == 0  # Start equals end
    assert shortest_path_no_tolls(graph, "A", "E") == -1  # No path exists
    assert (
        shortest_path_no_tolls(graph, "A", "C") == 3
    )  # Skips toll road A -> C directly
