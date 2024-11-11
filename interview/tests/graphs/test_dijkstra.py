import pytest

from interview.interview.graph.dijkstra import dijkstra


# Sample Dijkstra function (replace with your actual implementation)


# Test cases for Dijkstra's algorithm on an undirected graph
def test_basic_functionality():
    graph = {
        "A": {"B": 1, "C": 4},
        "B": {"A": 1, "C": 2, "D": 5},
        "C": {"A": 4, "B": 2, "D": 1},
        "D": {"B": 5, "C": 1},
    }
    expected_distances = {"A": 0, "B": 1, "C": 3, "D": 4}
    assert dijkstra(graph, "A") == expected_distances


def test_disconnected_graph():
    graph = {
        "A": {"B": 1},
        "B": {"A": 1, "C": 2},
        "C": {"B": 2},
        "D": {"E": 1},
        "E": {"D": 1},
    }
    expected_distances = {"A": 0, "B": 1, "C": 3, "D": float("inf"), "E": float("inf")}
    assert dijkstra(graph, "A") == expected_distances


def test_single_node_graph():
    graph = {"A": {}}
    expected_distances = {"A": 0}
    assert dijkstra(graph, "A") == expected_distances


def test_multiple_paths():
    graph = {
        "A": {"B": 1, "C": 5},
        "B": {"A": 1, "C": 1},
        "C": {"A": 5, "B": 1, "D": 1},
        "D": {"C": 1},
    }
    expected_distances = {"A": 0, "B": 1, "C": 2, "D": 3}
    assert dijkstra(graph, "A") == expected_distances


def test_basic_functionality_directed():
    graph = {"A": {"B": 1, "C": 4}, "B": {"C": 2, "D": 5}, "C": {"D": 1}, "D": {}}
    expected_distances = {"A": 0, "B": 1, "C": 3, "D": 4}
    assert dijkstra(graph, "A") == expected_distances


def test_disconnected_graph_directed():
    graph = {"A": {"B": 1}, "B": {"C": 2}, "C": {}, "D": {"E": 1}, "E": {}}
    expected_distances = {"A": 0, "B": 1, "C": 3, "D": float("inf"), "E": float("inf")}
    assert dijkstra(graph, "A") == expected_distances


def test_single_node_graph_directed():
    graph = {"A": {}}
    expected_distances = {"A": 0}
    assert dijkstra(graph, "A") == expected_distances


def test_multiple_paths_directed():
    graph = {"A": {"B": 1, "C": 5}, "B": {"C": 1}, "C": {"D": 1}, "D": {}}
    expected_distances = {"A": 0, "B": 1, "C": 2, "D": 3}
    assert dijkstra(graph, "A") == expected_distances
