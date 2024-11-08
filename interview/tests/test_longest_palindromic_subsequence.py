import pytest

from interview.interview.longest_palindromic_subsequence import (
    longest_palindromic_subsequence,
)


def test_single_character():
    # Single character should return length 1
    assert longest_palindromic_subsequence("a") == 1


def test_two_different_characters():
    # Two different characters, longest palindrome is either character itself
    assert longest_palindromic_subsequence("ab") == 1


def test_two_same_characters():
    # Two same characters, the entire string is a palindrome
    assert longest_palindromic_subsequence("aa") == 2


def test_long_palindromic_subsequence():
    # Standard case with a known palindromic subsequence
    assert (
        longest_palindromic_subsequence("bbbab") == 4
    )  # "bbbb" is the longest palindrome


def test_palindrome_string():
    # The entire string is already a palindrome
    assert longest_palindromic_subsequence("racecar") == 7


def test_non_palindromic_string():
    # String that is not a palindrome
    assert (
        longest_palindromic_subsequence("character") == 5
    )  # Longest palindrome is "carac" or "aceca"


def test_empty_string():
    # Edge case: Empty string should return 0
    assert longest_palindromic_subsequence("") == 0


def test_repeated_characters():
    # Edge case: String with repeated characters
    assert (
        longest_palindromic_subsequence("aaaa") == 4
    )  # All characters are the same, entire string is a palindrome


def test_mixed_case():
    # Mixed case string, assuming case sensitivity
    assert (
        longest_palindromic_subsequence("Aba") == 1
    )  # Longest palindromic subsequence is "A" or "a"
