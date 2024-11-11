from collections import defaultdict, deque


def topological_sort(graph):
    """
    "A": ["B", "C"], "B": ["D"], "C": [], "D": ["E"], "E": []}
    {'B': 1, 'C': 1, 'D': 1, 'E': 1})
    """

    result = []  # This will contain the sorted nodes
    temp_mark = set()
    perm_mark = set()

    has_cycle = False

    def visit(n):
        nonlocal has_cycle

        if n in perm_mark:
            return
        if n in temp_mark:
            has_cycle = True
            return

        temp_mark.add(n)

        for m in graph.get(n, []):
            visit(m)

        temp_mark.remove(n)
        perm_mark.add(n)
        result.insert(0, n)  # Add n to the head of L

    for node in graph:
        if node not in perm_mark:
            visit(node)
            if has_cycle:
                return []

    return result
