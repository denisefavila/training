def assign_questions_to_volunteers(questions, volunteers):
    def have_common_elements(set1, set2):
        return not set1.isdisjoint(set2)

    def explore(question_idx, seen, matched_volunteers):
        """augmenting paths for maximum bipartite matching"""
        for volunteer_idx in range(num_volunteers):
            if (
                can_assign_matrix[question_idx][volunteer_idx]
                and not seen[volunteer_idx]
            ):
                seen[volunteer_idx] = True
                # If volunteer is unmatched or can reassign their previous question
                if matched_volunteers[volunteer_idx] == -1 or explore(
                    matched_volunteers[volunteer_idx], seen, matched_volunteers
                ):
                    matched_volunteers[volunteer_idx] = (
                        question_idx
                    )
                    return True
        return False

    num_questions = len(questions)
    num_volunteers = len(volunteers)

    can_assign_matrix = [
        [0] * num_volunteers for _ in range(num_questions)
    ]  # (num_volunteers x num_questions)

    for i, question in enumerate(questions):
        for j, volunteer in enumerate(volunteers):
            if have_common_elements(set(question["tags"]), set(volunteer["tags"])):
                can_assign_matrix[i][j] = 1

    # maximum bipartite matching using DFS
    matched_volunteers = [-1] * num_volunteers

    # Try to find an augmenting path for each question
    for question_idx in range(num_questions):
        seen = [False] * num_volunteers
        explore(question_idx, seen, matched_volunteers)

    assignments = {}
    for volunteer_idx, question_idx in enumerate(matched_volunteers):
        if question_idx != -1:
            id_question = questions[question_idx]["id"]
            id_volunteer = volunteers[volunteer_idx]["id"]
            assignments[id_question] = id_volunteer

    return assignments
