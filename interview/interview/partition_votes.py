def find_combinations(votes, states):
    """
    You are given a list of vote power and states

    votesPower = [1,5,7,8,9,10,20]
    states = ["California", "Texas", "Florida", "Indiana", "Alaska", "Ohio", "Hawaii"]

    And you have two candidates C1 and C2, you need to return a
    List of List of states that we can make in such an order
    that both candidates receive the same amount of votes.

    Example: [["California", "Texas", "Florida", "Indiana", "Alaska"], ["Ohio", "Hawaii"]]
    The list can have different combinations, you need to return all the lists of combinations.
    :return:
    """

    def get_partition(idx, current_a_partition, current_a_partition_sum):
        if current_a_partition_sum == target:
            # current_b_partition = list(set(states) - set(current_a_partition))
            current_b_partition = [
                state for state in states if state not in current_a_partition
            ]
            result.append([current_a_partition.copy(), current_b_partition])
            return

        if current_a_partition_sum > target or idx == len(votes):
            return

        # add current vote on current_a_partition
        current_a_partition.append(states[idx])
        get_partition(
            idx + 1,
            current_a_partition,
            current_a_partition_sum + votes[idx],
        )
        current_a_partition.pop()

        # dont add current vote on current_a_partition
        get_partition(
            idx + 1,
            current_a_partition,
            current_a_partition_sum,
        )

    result = []

    all_votes = sum(votes)
    if all_votes % 2 != 0:
        return []

    target = all_votes // 2

    get_partition(0, [], 0)
    return result
