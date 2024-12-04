from interview.interview.partition_votes import find_combinations

# Sample inputs
votesPower = [1, 5, 7, 8, 9, 10, 20]
states = ["California", "Texas", "Florida", "Indiana", "Alaska", "Ohio", "Hawaii"]


# Test cases
def test_balanced_combination_exists():

    assert find_combinations(votesPower, states) == [
        [["California", "Texas", "Florida", "Indiana", "Alaska"], ["Ohio", "Hawaii"]],
        [["California", "Alaska", "Hawaii"], ["Texas", "Florida", "Indiana", "Ohio"]],
        [["Texas", "Florida", "Indiana", "Ohio"], ["California", "Alaska", "Hawaii"]],
        [["Ohio", "Hawaii"], ["California", "Texas", "Florida", "Indiana", "Alaska"]],
    ]


def test_no_combinations():
    votesPower_no_combination = [1, 2, 4]
    states_no_combination = ["State1", "State2", "State3"]
    assert find_combinations(votesPower_no_combination, states_no_combination) == []


def test_all_states_single_combination():
    votesPower_single_combination = [5, 5, 10, 10]
    states_single_combination = ["A", "B", "C", "D"]
    combination = find_combinations(
        votesPower_single_combination, states_single_combination
    )

    assert combination == [[["A", "C"], ["B", "D"]], [["A", "D"], ["B", "C"]]]


def test_single_state_per_candidate():
    votesPower_simple = [10, 10]
    states_simple = ["X", "Y"]
    assert find_combinations(votesPower_simple, states_simple) == [
        [["X"], ["Y"]],
        [["Y"], ["X"]],
    ]


def test_uneven_number_of_states():
    votesPower_uneven = [3, 3, 4, 6]
    states_uneven = ["S1", "S2", "S3", "S4"]
    assert find_combinations(votesPower_uneven, states_uneven) == [
        [["S1", "S4"], ["S2", "S3"]],
    ]


def test_large_votes():
    votesPower_large = [100, 150, 200, 250, 300, 350]
    states_large = ["A", "B", "C", "D", "E", "F"]
    assert find_combinations(votesPower_large, states_large) == [
        # Expected combinations with equal sums
    ]


def test_negative_votes():
    votesPower_negative = [-5, 5, 10, -10]
    states_negative = ["N1", "N2", "N3", "N4"]
    assert find_combinations(votesPower_negative, states_negative) == [
        [["N1", "N3"], ["N2", "N4"]],
        [["N2", "N3"], ["N1", "N4"]],
    ]
