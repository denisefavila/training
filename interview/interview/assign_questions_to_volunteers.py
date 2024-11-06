def have_common_elements(set1, set2):
    return not set1.isdisjoint(set2)


def assign_questions_to_volunteers(questions, volunteers):
    def backtrack(question_idx, assignments, assigned_volunteers):
        if question_idx == len(questions):
            return True

        question = questions[question_idx]
        assigned_any = False

        for volunteer_idx, volunteer in enumerate(volunteers):
            if volunteer_idx not in assigned_volunteers and have_common_elements(
                set(question["tags"]), set(volunteer["tags"])
            ):
                assignments[question["id"]] = volunteer["id"]
                assigned_volunteers.add(volunteer_idx)

                if backtrack(question_idx + 1, assignments, assigned_volunteers):
                    assigned_any = True
                    break

                del assignments[question["id"]]
                assigned_volunteers.remove(volunteer_idx)

        return assigned_any or backtrack(
            question_idx + 1, assignments, assigned_volunteers
        )

    assignments = {}
    assigned_volunteers = set()

    backtrack(0, assignments, assigned_volunteers)

    return assignments


def assign_questions_to_volunteers_dfs(questions, volunteers):
    """

    questions[
    {id:1, tags: ["MAC", "VSCODE"]},
    {id:2, tags: ["PY", "AI"]}
    {id:3, tags: ["JAVA", "OS"]}
    {id:4, tags: ["PY", "NW"]}
    ]

    Volunteer[
    {id: "1", tags:["PY",""NW], name: "A"},
    {id: "2", tags:["AI"], name: "B"},
    {id: "3", tags:["JAVA","NW], name: "C"},
    {id: "4", tags:["JAVA","NW"], name: "D"}
    ]

    Assign question to volunteers such that each question is assigned to at most one
    volunteer based on tags match.
    One volunteer can take at most one question and maximise the question assigned to volunteer.

    """

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
                    matched_volunteers[volunteer_idx] = question_idx
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
