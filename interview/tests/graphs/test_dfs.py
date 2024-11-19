from interview.interview.graph.dfs import dfs


def test_single_node():
    graph = {1: []}
    distances, finish_times, predecessors = dfs(graph)

    # Test discovery and finish times for single node
    assert distances == {1: 1}
    assert finish_times == {1: 2}
    assert predecessors == {1: None}


def test_two_connected_nodes():
    graph = {1: [2], 2: []}
    distances, finish_times, predecessors = dfs(graph)

    # Test discovery and finish times for connected nodes
    assert distances == {1: 1, 2: 2}
    assert finish_times == {1: 4, 2: 3}
    assert predecessors == {1: None, 2: 1}


def test_disconnected_graph():
    graph = {1: [2], 2: [], 3: []}
    distances, finish_times, predecessors = dfs(graph)

    # Test discovery and finish times for disconnected graph
    assert distances == {1: 1, 2: 2, 3: 3}
    assert finish_times == {1: 4, 2: 3, 3: 6}
    assert predecessors == {1: None, 2: 1, 3: None}


def test_multiple_edges():
    graph = {1: [2, 3], 2: [4], 3: [4], 4: []}
    distances, finish_times, predecessors = dfs(graph)

    # Test discovery and finish times for multiple edges
    assert distances == {1: 1, 2: 2, 3: 3, 4: 4}
    assert finish_times == {1: 8, 2: 7, 3: 6, 4: 5}
    assert predecessors == {1: None, 2: 1, 3: 1, 4: 3}


def test_cyclic_graph():
    graph = {1: [2], 2: [3], 3: [1]}
    distances, finish_times, predecessors = dfs(graph)

    # Test for cycle detection (should fail or behave in an expected manner)
    # Currently, the dfs does not handle cycle detection, so this might result in an infinite loop.
    # If cycle detection is needed, we would need to modify the DFS function.
    assert distances == {1: 1, 2: 2, 3: 3}
    assert finish_times == {1: 6, 2: 5, 3: 4}
    assert predecessors == {1: None, 2: 1, 3: 2}


def test_empty_graph():
    graph = {}
    distances, finish_times, predecessors = dfs(graph)

    # Test an empty graph should return all None values
    assert distances == {}
    assert finish_times == {}
    assert predecessors == {}
