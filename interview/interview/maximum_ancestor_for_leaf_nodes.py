from interview.interview.general.tree_node import TreeNode


def max_ancestor_for_leaf_nodes(root: TreeNode):
    """

    Given a tree, calculate the maximum ancestor for all the leaf nodes.
    Maximum ancestor of a leaf node is the maximum of its ancestors and the leaf itself.

    Example:

            4
          /   \
         5     3
        /     / \
       1     2   6

    Output -
    1: 5
    2: 4
    6: 6

    """
    result = {}

    def explore(node: TreeNode, current_max: int):
        nonlocal result
        if not node:
            return

        current_value = max(current_max, node.value)
        # is leaf
        if not node.right and not node.left:
            result[node.value] = current_value
            return

        explore(node.right, current_value)
        explore(node.left, current_value)

    explore(root, root.value)
    return result
