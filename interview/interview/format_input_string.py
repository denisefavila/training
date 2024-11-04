from typing import Dict


def format_input(input_str: str, map_dict: Dict[str, str]):
    """

    Given a string with any format containing only english letters,
    replace every percent-sign-sorrounded word (%EXAMPLE%)
     with the corresponding variable given inside a dictionary passed as an argument. Example:
    input = "home/usr/lib/%EXAMPLE%", {EXAMPLE: "testfile.tx"}
    output = "home/usr/lib/testfile.txt"

    input = "Hi %USER% how are you doing today %DATE%?", {USER: "John", DATE: "01/01/2024"}
    output = "Hi John how are you doing today 01/01/2024?"

    """
    # "home/usr/lib/%EXAMPLE%"
    start, idx = 0, 0
    result = []     # ["home/usr/lib/", "EXAMPLE"]
    while idx < len(input_str):
        if input_str[idx] == '%':
            result.append(input_str[start:idx])

            # skip the starting %
            idx += 1
            start = idx

            # look for the end of tag
            while idx < len(input_str) and input_str[idx] != '%':
                idx += 1

            tag = input_str[start:idx]
            if tag in map_dict:
                result.append(map_dict[tag])
            else:
                result.append(f"%{tag}%")

            # skip the closing %
            idx += 1
            start = idx

        else:
            idx += 1

    # append remaining chars
    result.append(input_str[start:])

    return "".join(result)
