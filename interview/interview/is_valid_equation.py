def is_valid_equation(equation):
    """
    Validate if the equation is syntactically correct.

    Valid operators: +, -, a-z, (, )
    Test cases:
    Valid - a + x = b + (c + a)
    Invalid - a + x = (ending with =; doesn't have RHS)
    Invalid - a + -x = a + b (- in -x is a unary operator)
    """

    def validate_expression(expression):
        alpha = "abcdefghijklmnopqrstuvwxyz"
        dfa_map = {
            "#": ["(", alpha, "-", "+"],
            "(": [alpha, "-", "+", "("],
            ")": ["+", "-", ")"],
            alpha: ["+", "-", ")"],
            "+": ["(", alpha],
            "-": ["(", alpha],
        }

        stack_parenthesis = []

        for idx, char in enumerate(expression):

            char_class = alpha if char in alpha else char

            if idx == 0:
                if char_class not in dfa_map["#"]:
                    return False
            else:
                prev_char = expression[idx - 1]
                prev_class = alpha if prev_char in alpha else prev_char

                if char_class not in dfa_map.get(prev_class, []):
                    return False

            if char == "(":
                stack_parenthesis.append(char)
            elif char == ")":
                if not stack_parenthesis:
                    return False
                stack_parenthesis.pop()

        return len(stack_parenthesis) == 0

    equation = equation.replace(" ", "")

    sides = equation.split("=")
    if len(sides) != 2 or not sides[0] or not sides[1]:
        return False

    lhs, rhs = sides

    return validate_expression(lhs) and validate_expression(rhs)
