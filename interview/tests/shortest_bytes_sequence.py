from interview.interview.shortest_bytes_sequence import (
    find_shortest_missing_byte_sequence,
)


def test_find_shortest_missing_byte_sequence():
    # Test cases with letters only
    assert (
        find_shortest_missing_byte_sequence(b"aabcdf") == b"e"
    ), "Test case 1 failed"  # Missing single byte 'e'

    # Test case 2: Check for missing two-byte sequences
    expected_missing_sequences = {
        b"aa",
        b"ad",
        b"ae",
        b"af",
        b"ba",
        b"bb",
        b"bc",
        b"bd",
        b"be",
        b"bf",
        b"ca",
        b"cb",
        b"cd",
        b"ce",
        b"cf",
        b"da",
        b"db",
        b"dc",
        b"de",
        b"df",
        b"ea",
        b"eb",
        b"ec",
        b"ed",
        b"ef",
        b"fa",
        b"fb",
        b"fc",
        b"fd",
        b"fe",
        b"ff",
    }
    result = find_shortest_missing_byte_sequence(b"abcdefacbeddefd")
    assert result in expected_missing_sequences, f"Test case 2 failed. Found: {result}"

    # Test case 3: More complex input, look for missing two-byte sequences
    assert find_shortest_missing_byte_sequence(b"abcdefacbeddefdaabbccddeeff") in {
        b"ab",
        b"ac",
        b"ad",
        b"ae",
        b"af",
        b"ba",
        b"bb",
        b"bc",
        b"bd",
        b"be",
        b"bf",
        b"ca",
        b"cb",
        b"cd",
        b"ce",
        b"cf",
        b"da",
        b"db",
        b"dc",
        b"de",
        b"df",
        b"ea",
        b"eb",
        b"ec",
        b"ed",
        b"ef",
        b"fa",
        b"fb",
        b"fc",
        b"fd",
        b"fe",
        b"ff",
    }, "Test case 3 failed"
