import pytest

from interview.interview.is_valid_equation import is_valid_equation

# Valid test cases


# Invalid test cases
@pytest.mark.parametrize(
    "equation",
    [
        "a + b = ",  # Ends with '=' and lacks RHS
        "= a + b",  # Begins with '=' and lacks LHS
        "a + -x = b + c",  # Unary operator usage `-x`
        "a + (b + c",  # Missing closing parenthesis
        "a b + c = d",  # Operands without operators in between
        "a + (b - c)) = d",  # Unbalanced parentheses (extra closing parenthesis)
    ],
)
def test_invalid_equations(equation):
    assert not is_valid_equation(equation)
