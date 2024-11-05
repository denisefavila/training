from interview.dp.cherry_pickups import cherry_pickups


def test_cherry_pickups():
    # Test case 1: No valid
    grid1 = [[1, 1, -1], [1, -1, 1], [-1, 1, 1]]
    assert cherry_pickups(grid1) == 0

    # Test case 3: No cherries to pick
    grid3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert cherry_pickups(grid3) == 0

    # Test case 4: All cells are valid and no obstacles
    grid4 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    assert cherry_pickups(grid4) == 8

    # Test case 5: Grid where there is a thorn on the path
    grid5 = [[1, 1, 1], [-1, 1, 1], [1, 1, 1]]
    assert cherry_pickups(grid5) == 7
