from typing import Any, Dict, List


def get_max_distance_binary_strings(binary_strings: List[str]):
    """
    "1011000", "1011110"
    {'1': {'0': {'1': {'1': {'0': {'0': {'0': {'*': True}}}, '1': {'1': {'0': {'*': True}}}}}}}}
    {'1': {'0': {'1': {'1': {'0': {'0': {'0': {}}}, '1': {'1': {'0': {}}}}}}}}

    """

    def build_trie(strs: List[str]):
        trie = {}
        for string in strs:
            current = trie
            for char in string:
                if char not in current:
                    current[char] = {}
                current = current[char]
            current["*"] = True
        return trie

    def calculate_heights(trie):
        """
        Calculate the height of each subtree in a trie, where height is the maximum distance
        from the node to a leaf.

        :param trie: Dictionary representing the trie
        :return: Dictionary where each node's path gives its height
        """

        def dfs(node):
            # Base case: If the node has no children, its height is 0
            if (
                "*" in node or not node
            ):  # '*' signifies the end of a string, or empty node
                return 0

            # Calculate the height of each child recursively
            heights = {}
            for char, child in node.items():
                child_height = (
                    dfs(child) + 1
                )  # Add 1 to account for the edge to this child
                heights[char] = child_height

            # Store the maximum height among all children for the current node
            max_height = max(heights.values(), default=0)

            # Add height information to the current node in the form of a nested dictionary
            node["_heights"] = heights
            node["_max_height"] = max_height
            return max_height

        # Perform DFS from the root node
        dfs(trie)
        return trie

    trie = build_trie(binary_strings)

    heights = calculate_heights(trie)
    import pdb

    pdb.set_trace()
    same_prefix = trie
    while len(same_prefix) == 1:
        same_prefix = list(same_prefix.values())[0]


def get_max_distance_binary_strings_brute_fore(binary_strings: List[str]):
    """

    The distance between 2 binary strings is the sum of their lengths after
    removing the common prefix. For example: the common prefix of 1011000 and 1011110
    is 1011 so the distance is len("000") + len("110") = 3 + 3 = 6.

    Given a list of binary strings, pick a pair that gives you maximum distance among all possible pair and return that distance.
    """

    def common_prefix_length(str1: str, str2: str):
        # common preffix
        size_1 = len(str1)
        size_2 = len(str2)

        i = 0
        while i < size_1 and i < size_2 and str1[i] == str2[i]:
            i += 1

        return i

    if not binary_strings:
        return 0

    max_distance = 0
    for i in range(len(binary_strings)):
        for j in range(i + 1, len(binary_strings)):
            common_length = common_prefix_length(binary_strings[i], binary_strings[j])
            current_distance = (len(binary_strings[i]) - common_length) + (
                len(binary_strings[j]) - common_length
            )
            max_distance = max(max_distance, current_distance)

    return max_distance
