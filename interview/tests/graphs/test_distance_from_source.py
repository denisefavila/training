import pytest

from interview.interview.graph.distance_from_source import distance_from_source

# Test graph
graph_1 = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2],
}

# Disconnected graph
graph_2 = {0: [1], 1: [0], 2: [3], 3: [2]}

# Single node graph
graph_3 = {0: []}

# Linear graph
graph_4 = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}

# Complete graph
graph_5 = {0: [1, 2, 3], 1: [0, 2, 3], 2: [0, 1, 3], 3: [0, 1, 2]}

grid_graph = {
    "s": ["a", "c"],
    "a": ["s", "b", "d"],
    "b": ["a", "e"],
    "c": ["s", "d", "f"],
    "d": ["a", "c", "e", "g"],
    "e": ["b", "d", "h"],
    "f": ["c", "g"],
    "g": ["d", "f", "h"],
    "h": ["e", "g"],
}


def test_bfs():
    # Test graph 1
    expected_0_1 = {0: 0, 1: 1, 2: 1, 3: 2, 4: 2}
    distances, _ = distance_from_source(graph_1, 0)
    assert distances == expected_0_1

    expected_1_1 = {0: 1, 1: 0, 2: 2, 3: 1, 4: 1}
    distances, _ = distance_from_source(graph_1, 1)
    assert distances == expected_1_1

    expected_2_1 = {0: 1, 1: 2, 2: 0, 3: 3, 4: 1}
    distances, _ = distance_from_source(graph_1, 2)
    assert distances == expected_2_1

    expected_3_1 = {0: 2, 1: 1, 2: 3, 3: 0, 4: 2}
    distances, _ = distance_from_source(graph_1, 3)
    assert distances == expected_3_1

    expected_4_1 = {0: 2, 1: 1, 2: 1, 3: 2, 4: 0}
    distances, _ = distance_from_source(graph_1, 4)
    assert distances == expected_4_1

    # Test graph 2 (disconnected graph)
    expected_0_2 = {0: 0, 1: 1, 2: float("inf"), 3: float("inf")}
    distances, _ = distance_from_source(graph_2, 0)
    assert distances == expected_0_2

    expected_2_2 = {0: float("inf"), 1: float("inf"), 2: 0, 3: 1}
    distances, _ = distance_from_source(graph_2, 2)
    assert distances == expected_2_2

    # Test graph 3 (single node)
    expected_0_3 = {0: 0}
    distances, _ = distance_from_source(graph_3, 0)
    assert distances == expected_0_3

    # Test graph 4 (linear graph)
    expected_0_4 = {0: 0, 1: 1, 2: 2, 3: 3}
    distances, _ = distance_from_source(graph_4, 0)
    assert distances == expected_0_4

    expected_1_4 = {0: 1, 1: 0, 2: 1, 3: 2}
    distances, _ = distance_from_source(graph_4, 1)
    assert distances == expected_1_4

    expected_2_4 = {0: 2, 1: 1, 2: 0, 3: 1}
    distances, _ = distance_from_source(graph_4, 2)
    assert distances == expected_2_4

    expected_3_4 = {0: 3, 1: 2, 2: 1, 3: 0}
    distances, _ = distance_from_source(graph_4, 3)
    assert distances == expected_3_4

    # Test graph 5 (complete graph)
    expected_0_5 = {0: 0, 1: 1, 2: 1, 3: 1}
    distances, _ = distance_from_source(graph_5, 0)
    assert distances == expected_0_5

    expected_1_5 = {0: 1, 1: 0, 2: 1, 3: 1}
    distances, _ = distance_from_source(graph_5, 1)
    assert distances == expected_1_5

    expected_2_5 = {0: 1, 1: 1, 2: 0, 3: 1}
    distances, _ = distance_from_source(graph_5, 2)
    assert distances == expected_2_5

    expected_3_5 = {0: 1, 1: 1, 2: 1, 3: 0}
    distances, _ = distance_from_source(graph_5, 3)
    assert distances == expected_3_5


def test_bfs_grid():
    # Test graph 1 (previous graph)
    distances, predecessors = distance_from_source(grid_graph, "s")
    assert distances == {
        "s": 0,
        "a": 1,
        "b": 2,
        "c": 1,
        "d": 2,
        "e": 3,
        "f": 2,
        "g": 3,
        "h": 4,
    }
    assert predecessors == {
        "s": None,
        "a": "s",
        "b": "a",
        "c": "s",
        "d": "a",
        "e": "b",
        "f": "c",
        "g": "d",
        "h": "e",
    }


# Directed graphs for testing
# Directed graph with reachable nodes from source
directed_graph_1 = {
    0: [1, 2],
    1: [3],
    2: [4],
    3: [],
    4: [3],
}

# Directed graph with some unreachable nodes from source
directed_graph_2 = {
    0: [1],
    1: [],
    2: [3],
    3: [],
}

# Directed graph with a cycle
directed_graph_3 = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [],
}

# Directed graph where all nodes are reachable from the source
directed_graph_4 = {
    0: [1, 2],
    1: [2, 3],
    2: [3],
    3: [],
}

# Directed graph with only one node
directed_graph_5 = {0: []}


def test_bfs_directed():
    # Test directed_graph_1
    expected_0_1 = {0: 0, 1: 1, 2: 1, 3: 2, 4: 2}
    distances, _ = distance_from_source(directed_graph_1, 0)
    assert distances == expected_0_1
