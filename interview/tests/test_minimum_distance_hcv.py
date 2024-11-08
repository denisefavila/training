from interview.interview.minimum_distance_hcv import minimum_distance_hcv


def test_basic_case():
    # Example from the problem statement
    # Source: 0, Destination: 4
    # Expected Output: 19
    num_stops = 5
    credit = [2, 10, 5, 100, 3]
    num_roads = 8
    roads = [
        [0, 1, 2],
        [0, 3, 5],
        [0, 2, 1],
        [1, 3, 10],
        [1, 4, 15],
        [2, 3, 7],
        [2, 4, 90],
        [3, 4, 80],
    ]
    source = 0
    destination = 4
    expected_output = 19
    assert (
        minimum_distance_hcv(num_stops, credit, num_roads, roads, source, destination)
        == expected_output
    )
