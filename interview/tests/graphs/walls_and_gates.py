from interview.graph.walls_and_gates import walls_and_gates


def test_single_gate():
    rooms = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647],
    ]
    walls_and_gates(rooms)
    expected = [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
    assert rooms == expected


def test_multiple_gates():
    rooms = [
        [0, 2147483647, 2147483647],
        [2147483647, -1, 2147483647],
        [2147483647, 2147483647, 0],
    ]
    walls_and_gates(rooms)

    print(rooms)
    expected = [[0, 1, 2], [1, -1, 1], [2, 1, 0]]
    assert rooms == expected


def test_no_gates():
    rooms = [[2147483647, -1, 2147483647], [-1, -1, -1], [2147483647, -1, 2147483647]]
    walls_and_gates(rooms)
    expected = [
        [2147483647, -1, 2147483647],
        [-1, -1, -1],
        [2147483647, -1, 2147483647],
    ]
    assert rooms == expected


def test_all_walls():
    rooms = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
    walls_and_gates(rooms)
    expected = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
    assert rooms == expected


def test_no_walls():
    rooms = [
        [2147483647, 2147483647, 2147483647],
        [2147483647, 2147483647, 2147483647],
        [2147483647, 2147483647, 2147483647],
    ]
    walls_and_gates(rooms)
    expected = [
        [2147483647, 2147483647, 2147483647],
        [2147483647, 2147483647, 2147483647],
        [2147483647, 2147483647, 2147483647],
    ]
    assert rooms == expected
