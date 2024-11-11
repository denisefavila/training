def is_palindrome(word):
    return word == word[::-1]


def longest_palindromic_subsequence(word: str):
    """
    "character" -> carac, aceca


    """

    def longest_size(idx, left, right):

        if idx >= len(word):
            return 0

        add_current = None
        dont_add_current = longest_size(idx + 1, left, right)

        return max(add_current, dont_add_current)

    return longest_size(0, 0, len(word) - 1)
