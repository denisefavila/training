from interview.interview.graph.dfs import dfs_stack

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


def test_bfs_grid():
    # Test graph 1 (previous graph)
    distances, predecessors = dfs_stack(grid_graph)

    import pdb

    pdb.set_trace()
