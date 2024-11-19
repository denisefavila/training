from interview.interview.graph.detect_cycle import detect_cycle


def test_no_cycles():
    graph = {"A": ["B"], "B": ["C"], "C": []}
    assert detect_cycle(graph) == False  # No cycles in this graph


def test_single_cycle():
    graph = {"A": ["B"], "B": ["C"], "C": ["A"]}  # Cycle exists: A -> B -> C -> A
    assert detect_cycle(graph) == True  # Cycle exists


def test_multiple_cycles():
    graph = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"],  # A -> B -> C -> A
        "D": ["E"],
        "E": ["D"],  # D -> E -> D
    }
    assert detect_cycle(graph) == True  # Multiple cycles: A-B-C-A and D-E-D


def test_empty_graph():
    graph = {}
    assert detect_cycle(graph) == False  # No nodes, no cycles


def test_single_node_no_edges():
    graph = {"A": []}
    assert detect_cycle(graph) == False  # No edges, no cycles


def test_single_node_with_self_edge():
    graph = {"A": ["A"]}  # A -> A (self-loop)
    assert detect_cycle(graph) == True  # Self-loop forms a cycle


def test_disconnected_graph():
    graph = {"A": ["B"], "B": [], "C": ["D"], "D": []}
    assert detect_cycle(graph) == False  # No cycles in any connected component


def test_cycle_in_large_graph():
    graph = {
        "A": ["B"],
        "B": ["C"],
        "C": ["D"],
        "D": ["A"],  # Cycle: A -> B -> C -> D -> A
    }
    assert detect_cycle(graph) == True  # Large graph with a cycle


def test_large_graph_without_cycle():
    graph = {"A": ["B"], "B": ["C"], "C": ["D"], "D": []}  # No cycle
    assert detect_cycle(graph) == False  # No cycle in a large acyclic graph


def test_graph_with_multiple_edges():
    graph = {"A": ["B", "C"], "B": ["C"], "C": ["A"]}  # Cycle exists: A -> B -> C -> A
    assert detect_cycle(graph) == True  # Cycle exists in the graph


def test_cycle_in_graph_with_parallel_edges():
    graph = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"],  # A -> B -> C -> A
        "D": ["A"],  # Parallel edge to A
    }
    assert detect_cycle(graph) == True  # Cycle exists (A -> B -> C -> A)
