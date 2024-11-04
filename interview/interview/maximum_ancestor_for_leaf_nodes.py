from interview.interview.general.tree_node import TreeNode


def max_ancestor_for_leaf_nodes(root: TreeNode):
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
