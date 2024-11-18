from typing import List


def generate_words(letters: List[str], mandatory: str) -> List[str]:
    n = len(letters)

    def explore(current_word, used):
        if len(current_word) >= 4 and mandatory in current_word:
            result.add(current_word)

        if len(current_word) > n:
            return

        for i in range(n):
            if i not in used:
                used.add(i)
                explore(current_word + letters[i], used)
                used.remove(i)

    result = set()

    explore("", set())

    return sorted(result)
