from interview.interview.tree.min_weight_disconnect_leafs import (
    TreeNode,
    min_disconnect_weight,
)


def test_min_disconnect_weight():
    # Test case 1: Example 1
    A = TreeNode(0)  # Root node A
    B = TreeNode(2)  # Node B
    C = TreeNode(4)  # Node C
    D = TreeNode(2)  # Node D
    E = TreeNode(1)  # Node E

    # Build the tree as described in Example 1
    A.add_child(B)
    A.add_child(C)
    B.add_child(D)
    B.add_child(E)

    # Expected output: 6
    assert min_disconnect_weight(A) == 6

    # Test case 2: Example 2
    A = TreeNode(0)  # Root node A
    B = TreeNode(3)  # Node B
    C = TreeNode(4)  # Node C
    D = TreeNode(1)  # Node D
    E = TreeNode(1)  # Node E

    # Build the tree as described in Example 2
    A.add_child(B)
    A.add_child(C)
    B.add_child(D)
    B.add_child(E)

    # Expected output: 6
    assert min_disconnect_weight(A) == 6

    # Test case 3: Single node (no leaves to disconnect)
    A = TreeNode(0)  # Root node A

    # Expected output: 0 (no leaf to disconnect)
    assert min_disconnect_weight(A) == 0

    # Test case 4: Tree with only leaf nodes
    A = TreeNode(0)  # Root node A
    B = TreeNode(2)  # Leaf node B
    C = TreeNode(3)  # Leaf node C

    # Build the tree
    A.add_child(B)
    A.add_child(C)

    # Expected output: 5 (cut node A to disconnect B and C)
    assert min_disconnect_weight(A) == 5

    # Test case 5: Complex tree
    A = TreeNode(0)  # Root node A
    B = TreeNode(3)  # Node B
    C = TreeNode(4)  # Node C
    D = TreeNode(2)  # Node D
    E = TreeNode(1)  # Node E
    F = TreeNode(2)  # Node F

    # Build the tree
    A.add_child(B)
    A.add_child(C)
    B.add_child(D)
    B.add_child(E)
    C.add_child(F)

    # Expected output: 6 (cut C and B to disconnect all leaves)
    assert min_disconnect_weight(A) == 6
