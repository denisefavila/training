from interview.interview.graph.topological_sort_dfs import topological_sort


def test_topological_sort():
    # Test 1: Normal case with no cycles
    graph_1 = {"A": ["B", "C"], "B": ["D"], "C": [], "D": ["E"], "E": []}
    assert topological_sort(graph_1) == ["A", "C", "B", "D", "E"]

    # Test 2: Single node, no dependencies
    graph_2 = {"A": []}
    assert topological_sort(graph_2) == ["A"]

    # Test 3: Multiple nodes with no edges
    graph_3 = {"A": [], "B": [], "C": []}
    assert topological_sort(graph_3) == ["C", "B", "A"]  # Order doesn't matter here

    # Test 4: Cyclic graph (should return cycle detected)
    graph_4 = {"A": ["B"], "B": ["C"], "C": ["A"]}
    assert topological_sort(graph_4) == []

    # Test 5: Multiple valid topological sorts
    graph_5 = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    # Multiple valid orders: ['A', 'B', 'C', 'D'] or ['A', 'C', 'B', 'D']
    result_5 = topological_sort(graph_5)
    assert result_5 == ["A", "B", "C", "D"] or result_5 == ["A", "C", "B", "D"]

    # Test 6: Single node with self-loop (invalid case)
    graph_6 = {"A": ["A"]}
    assert topological_sort(graph_6) == []

    # Test 7: Larger graph with multiple dependencies
    graph_7 = {"A": ["B"], "B": ["C"], "C": ["D"], "D": ["E"], "E": []}
    assert topological_sort(graph_7) == ["A", "B", "C", "D", "E"]

    # Test 8: A graph with a single node and no edges (minimum edge case)
    graph_8 = {"X": []}
    assert topological_sort(graph_8) == ["X"]
