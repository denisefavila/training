import pytest

from interview.interview.graph.alien_dictionary import alien_dictionary


def test_valid_case_1():
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    expected = "wertf"
    # Test for a valid case where the alien language order is determined correctly
    assert alien_dictionary(words) == expected


def test_valid_case_2():
    words = ["z", "x", "z"]
    expected = ""
    # Test for a case where the order cannot be determined (duplicate words)
    assert alien_dictionary(words) == expected


def test_valid_case_3():
    words = ["abc", "ab"]
    expected = ""
    # Test for a case where a word is a prefix of another (invalid lexicographical order)
    assert alien_dictionary(words) == expected


def test_valid_case_4():
    words = ["abc", "acd", "bce"]
    # Test for a case with multiple valid orderings
    assert alien_dictionary(words) in ("adebc", "abcde")


def test_valid_case_5():
    words = ["abc", "ab", "acd"]
    expected = "abc"
    assert alien_dictionary(words) == ""


def test_single_word():
    words = ["z"]
    expected = "z"
    # Test for a case with only one word in the dictionary
    assert alien_dictionary(words) == expected


def test_empty_list():
    words = []
    expected = ""
    # Test for an empty list of words, which is a valid but trivial case
    assert alien_dictionary(words) == expected


def test_valid_case_multiple_solutions():
    words = ["abc", "bca", "cab"]
    expected = "abc"  # Or "acb", depending on valid ordering, both are possible.
    assert alien_dictionary(words) in ["abc", "acb"]
