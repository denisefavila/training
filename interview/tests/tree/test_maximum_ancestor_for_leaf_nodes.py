from interview.interview.general.tree_node import TreeNode
from interview.interview.tree.maximum_ancestor_for_leaf_nodes import \
    max_ancestor_for_leaf_nodes


def test_single_node_tree():
    root = TreeNode(10)
    result = max_ancestor_for_leaf_nodes(root)
    assert result == {10: 10}


def test_two_level_tree():
    root = TreeNode(20, TreeNode(10), TreeNode(30))
    result = max_ancestor_for_leaf_nodes(root)
    assert result == {10: 20, 30: 30}


def test_three_level_tree():
    root = TreeNode(
        15, TreeNode(10, TreeNode(5), TreeNode(12)), TreeNode(25, None, TreeNode(30))
    )
    result = max_ancestor_for_leaf_nodes(root)
    assert result == {5: 15, 12: 15, 30: 30}


def test_left_heavy_tree():
    root = TreeNode(40, TreeNode(35, TreeNode(30, TreeNode(25))))
    result = max_ancestor_for_leaf_nodes(root)
    assert result == {25: 40}


def test_right_heavy_tree():
    root = TreeNode(5, None, TreeNode(15, None, TreeNode(25, None, TreeNode(35))))
    result = max_ancestor_for_leaf_nodes(root)
    assert result == {35: 35}


def test_complex_tree():
    root = TreeNode(
        50,
        TreeNode(
            30,
            TreeNode(20, TreeNode(10), TreeNode(25)),
            TreeNode(40, None, TreeNode(45)),
        ),
        TreeNode(70, TreeNode(60), TreeNode(80, TreeNode(75), TreeNode(90))),
    )
    result = max_ancestor_for_leaf_nodes(root)
    expected = {10: 50, 25: 50, 45: 50, 60: 70, 75: 80, 90: 90}
    assert result == expected


def test_balanced_tree():
    root = TreeNode(
        50,
        TreeNode(30, TreeNode(20), TreeNode(40)),
        TreeNode(70, TreeNode(60), TreeNode(80)),
    )
    result = max_ancestor_for_leaf_nodes(root)
    expected = {20: 50, 40: 50, 60: 70, 80: 80}
    assert result == expected


def test_tree_1():
    # Construct the tree
    root = TreeNode(4, TreeNode(5, TreeNode(1)), TreeNode(3, TreeNode(2), TreeNode(6)))

    # Expected result
    expected = {1: 5, 2: 4, 6: 6}

    # Run the function and check the result
    assert max_ancestor_for_leaf_nodes(root) == expected
