from heapq import heappush


class TreeNode:
    def __init__(self, weight=0):
        self.weight = weight
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def min_disconnect_weight(root):
    # Helper function to calculate minimum weight recursively
    def dfs(node):
        if not node:
            return 0

        if not node.children:
            return 0  # No cost to disconnect a leaf node itself

        # Initialize minimum cost as a large value
        min_cost = float("inf")

        # Option 1: Disconnect the current node itself (cut edges to all children)
        cost_to_cut_node = sum(child.weight for child in node.children)
        min_cost = min(min_cost, cost_to_cut_node)

        # Option 2: Disconnect by removing the children
        for child in node.children:
            # Recursive call for the child subtree
            min_cost = min(min_cost, dfs(child))

        return min_cost

    return dfs(root)
