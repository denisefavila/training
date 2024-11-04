from interview.strings_and_arrays.format_input_string import format_input


def test_single_placeholder():
    input_string = "home/usr/lib/%EXAMPLE%"
    variables = {"EXAMPLE": "testfile.txt"}
    expected_output = "home/usr/lib/testfile.txt"
    assert format_input(input_string, variables) == expected_output


def test_multiple_placeholders():
    input_string = "Hi %USER% how are you doing today %DATE%?"
    variables = {"USER": "John", "DATE": "01/01/2024"}
    expected_output = "Hi John how are you doing today 01/01/2024?"
    assert format_input(input_string, variables) == expected_output


def test_no_placeholders():
    input_string = "Hello, world!"
    variables = {"USER": "Alice"}
    expected_output = "Hello, world!"
    assert format_input(input_string, variables) == expected_output


def test_unmatched_placeholder_in_string():
    input_string = "Hello %USER%, welcome to %PLACE%."
    variables = {"USER": "Alice"}
    expected_output = "Hello Alice, welcome to %PLACE%."
    assert format_input(input_string, variables) == expected_output


def test_empty_string():
    input_string = ""
    variables = {"EXAMPLE": "test"}
    expected_output = ""
    assert format_input(input_string, variables) == expected_output


def test_empty_dictionary():
    input_string = "Hello %USER%"
    variables = {}
    expected_output = "Hello %USER%"
    assert format_input(input_string, variables) == expected_output


def test_placeholder_with_partial_match():
    input_string = "Welcome %USERNAME%"
    variables = {"USER": "Alice"}
    expected_output = "Welcome %USERNAME%"
    assert format_input(input_string, variables) == expected_output
