from interview.interview.graph.can_broadcast import broadcast_message


def test_broadcast_message():
    # Test case 1: Basic case, reachable within distance
    routers_1 = {
        0: [(1, 5), (2, 10)],
        1: [(0, 5), (3, 8)],
        2: [(0, 10), (3, 2)],
        3: [(1, 8), (2, 2)],
    }
    src = 0
    des = 3
    max_distance = 12
    assert broadcast_message(routers_1, src, des, max_distance)

    # Test case 2: Destination is unreachable
    routers_2 = {
        0: [(1, 5)],
        1: [(0, 5)],
        2: [(3, 5)],
        3: [(2, 5)],
    }
    src = 0
    des = 3
    max_distance = 10
    assert not broadcast_message(routers_2, src, des, max_distance)

    # Test case 3: Destination reachable exactly at the max distance
    routers_3 = {
        0: [(1, 5), (2, 10)],
        1: [(0, 5), (3, 5)],
        2: [(0, 10), (3, 5)],
        3: [(1, 5), (2, 5)],
    }
    src = 0
    des = 3
    max_distance = 10
    assert broadcast_message(routers_3, src, des, max_distance) == True

    # Test case 4: Destination is unreachable with any path
    routers_4 = {
        0: [(1, 5)],
        1: [(0, 5)],
        2: [(3, 10)],
        3: [(2, 10)],
    }
    src = 0
    des = 3
    max_distance = 5
    assert broadcast_message(routers_4, src, des, max_distance) == False

    # Test case 5: Single node graph, no edges
    routers_5 = {0: []}
    src = 0
    des = 0
    max_distance = 10
    assert broadcast_message(routers_5, src, des, max_distance) == True

    # Test case 6: Single node graph, source and destination are the same, max distance is 0
    routers_6 = {0: []}
    src = 0
    des = 0
    max_distance = 0
    assert broadcast_message(routers_6, src, des, max_distance) == True

    # Test case 7: Multiple nodes, source is unreachable from destination
    routers_7 = {
        0: [(1, 5)],
        1: [(0, 5)],
        2: [(3, 2)],
        3: [(2, 2)],
    }
    src = 0
    des = 3
    max_distance = 10
    assert broadcast_message(routers_7, src, des, max_distance) == False

    # Test case 8: Large graph, destination reachable within distance
    routers_8 = {
        0: [(1, 2), (2, 4)],
        1: [(0, 2), (3, 3)],
        2: [(0, 4), (3, 1)],
        3: [(1, 3), (2, 1)],
    }
    src = 0
    des = 3
    max_distance = 6
    assert broadcast_message(routers_8, src, des, max_distance) == True

    # Test case 9: Large graph, destination not reachable within distance
    routers_9 = {
        0: [(1, 5), (2, 10)],
        1: [(0, 5), (3, 8)],
        2: [(0, 10), (3, 15)],
        3: [(1, 8), (2, 15)],
    }
    src = 0
    des = 3
    max_distance = 12
    assert broadcast_message(routers_9, src, des, max_distance) == False
