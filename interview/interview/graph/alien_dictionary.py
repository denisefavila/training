from collections import defaultdict, Counter, deque
from typing import List


def alien_dictionary(words: List[str]):
    """

    https://leetcode.com/problems/alien-dictionary/description/

    words = ["wrt","wrf","er","ett","rftt"]

    dependencies => {w: {e}, e: {r}, t: {f}, r: {t}}

    in_degree => {'r': 1, 't': 1, 'f': 1, 'e': 1, 'w': 0}

    topological sorting

    "wertf"

    """

    dependencies = defaultdict(set)
    in_degree = Counter({c: 0 for word in words for c in word})

    for idx in range(len(words) - 1):
        current_word, next_word = words[idx], words[idx + 1]
        j = 0
        if current_word.startswith(next_word) and len(current_word) > len(next_word):
            return ""
        while j < len(current_word) and j < len(next_word):
            if current_word[j] != next_word[j]:
                dependencies[current_word[j]].add(next_word[j])
                in_degree[next_word[j]] += 1
                break
            j += 1

    print(dependencies)
    print(in_degree)
    result = []
    queue = deque()
    for char, counter in in_degree.items():
        if counter == 0:
            queue.append(char)

    while queue:
        current_char = queue.popleft()
        result.append(current_char)

        next_dependant_chars = dependencies[current_char]
        for next_char in next_dependant_chars:
            in_degree[next_char] -= 1
            if in_degree[next_char] == 0:
                queue.append(next_char)

    print(result)
    if len(result) == len(in_degree):
        return "".join(result)
    else:
        return ""
