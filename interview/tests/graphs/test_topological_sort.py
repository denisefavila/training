from interview.interview.graph.topological_sort_kahn import topological_sort


def test_topological_sort():
    # Test 1: Normal case with no cycles
    graph_1 = {"A": ["B", "C"], "B": ["D"], "C": [], "D": ["E"], "E": []}
    assert topological_sort(graph_1) == ["A", "B", "C", "D", "E"]
